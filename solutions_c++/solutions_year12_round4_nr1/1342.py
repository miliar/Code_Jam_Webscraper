#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000


//typedef long long LL;

int D[100005],L[100005],n;
int LL,sol;
char vis[10005][10005];
void visit(int now,int x)
{
	int h = MIN(L[now], D[now]-D[x]);
	int i;

	if(D[now]+h>=LL) { sol=1; return ; }
	if(vis[now][x]) return;
	vis[now][x]=1;
	//printf("%d %d %d\n",now,x,h);
	
	for(i=now+1;i<=n;i++)
	{
		//printf("%d\n",D[i]-D[now]);
		if(D[i]-D[now]>h) break;
		visit(i,now);
		if(sol) return  ;
	}
}


int main()
{
	int i,j,k,l,tests,cs=0,m;
	

	freopen("E:\\A-small-attempt0.in","r",stdin);
	freopen("E:\\A-small-attempt0(1)e.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d%d",&D[i],&L[i]);
		scanf("%d",&LL);
		MEM(vis,0);
		sol=0;
		visit(1,0);

		printf("Case #%d: ",++cs);
		if(sol)
			puts("YES");
		else
			puts("NO");

	}

	return 0;
} 


