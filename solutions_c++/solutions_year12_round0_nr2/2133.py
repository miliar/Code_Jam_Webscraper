#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <memory.h>
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 

int usuall[50],awesome[50];
int n,s,p;
int ar[100];
int dp[100][100];
int DP(int pos, int ost)
{
	if (ost < 0)
		return -inf;
	if (pos == n)
	{
		if (ost > 0)
			return -inf;
		else
			return 0;
	}
	if (dp[pos][ost] != -1)
		return dp[pos][ost];
	int res = -inf;
	if (awesome[ar[pos]] != -1)
	{
		int add = awesome[ar[pos]] >= p;
		res = max(res,DP(pos+1,ost-1)+add);
	}
	if (usuall[ar[pos]] != -1)
	{
		int add = usuall[ar[pos]] >= p;
		res = max(res, DP(pos+1,ost) + add);
	}
	return dp[pos][ost] = res;
}
void Solve()
{
	scanf("%d%d%d",&n,&s,&p);
	FOR(i,n)
		scanf("%d",&ar[i]);
	CL(dp,-1);
	int res = DP(0,s);
	printf("%d\n",res);
}
int main() 
{ 
	CL(usuall,-1);
	CL(awesome,-1);
	FOR(i,11)
	{
		FOR(j,11)
		{
			FOR(k,11)
			{
				if (max(i,max(j,k)) - min(i,min(j,k)) > 2)
					continue;
				if (max(i,max(j,k)) - min(i,min(j,k)) == 2)
					awesome[i+j+k] = max(max(i,max(j,k)),awesome[i+j+k]);
				else
					usuall[i+j+k] = max(max(i,max(j,k)),usuall[i+j+k]);
			}
		}
	}
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);
		Solve();
		cerr << "Solved " << i+1 << endl;
	}
	return 0; 
}
