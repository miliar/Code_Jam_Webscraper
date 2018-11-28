#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define fo(a,n) for(a=0;a<n;a++)
#define memset0(v) memset(v,0,sizeof(v))
typedef vector<string> vs;
typedef vector<int> vi;

const int MAXN=10002;

const int INF=1000000;

int best[MAXN][2];
int nodevals[MAXN];
int gates[MAXN];
int canchange[MAXN];
int child[MAXN][2];
int M,V;

void solve(int node)
{
	if(child[node][0]<0)
	{
		if(nodevals[node]==0)
			best[node][0]=0;
		else
			best[node][1]=0;
		return;
	}

	int left=child[node][0];
	int right=child[node][1];

	solve(left);
	solve(right);

	for(int change=0;change<2;change++)
	{
		int cbest0, cbest1;
		if(gates[node]==0) // OR gate
		{
			cbest0=best[left][0]+best[right][0];
			cbest1=min( min(best[left][0]+best[right][1], best[left][1]+best[right][0]), best[left][1]+best[right][1]);
		}
		else // AND gate
		{
			cbest0=min( min(best[left][0]+best[right][1], best[left][1]+best[right][0]), best[left][0]+best[right][0]);
			cbest1=best[left][1]+best[right][1];
		}

		cbest0=min(INF, cbest0+change);
		cbest1=min(INF, cbest1+change);

		best[node][0]=min(cbest0, best[node][0]);
		best[node][1]=min(cbest1, best[node][1]);
		
		if(canchange[node]==0) break;
		gates[node]=1-gates[node];
	}
}

int main()
{
	int a,b,c,d,tests;

	const string strFile = "a-small";
	string fin = strFile+".in";
	string fout = strFile+".out";

	freopen(fin.c_str(), "rt", stdin);
	freopen(fout.c_str(), "wt", stdout);

	scanf("%d", &tests);

for(int test=1;test<=tests;test++)
{

	scanf("%d%d", &M, &V);
	for(a=1;a<=(M-1)/2;a++)
	{
		scanf("%d%d",&gates[a],&canchange[a]);
		child[a][0]=2*a;
		child[a][1]=2*a+1;
	}
	for(a=(M-1)/2+1;a<=M;a++)
	{
		scanf("%d",&nodevals[a]);
		canchange[a]=0;
		child[a][0]=child[a][1]=-1;
		gates[a]=-1;
	}

	for(a=1;a<=M;a++) best[a][0]=best[a][1]=INF;

	solve(1);

	if(best[1][V]<INF)
		printf("Case #%d: %d\n", test, best[1][V]);
	else
		printf("Case #%d: IMPOSSIBLE\n", test);

}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
