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
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
//typedef __int64 LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

int f[25][25];
int now[25],n,m;
vi edges[2005];
int can[25][25],tim,ans;

int check(int pos,int mask)
{
	int i,j;

	++tim;
	for(i=0;i<pos;i++)
	{
		int a=now[i],b=now[(i+1)%pos];
		//if(mask==14) printf("=%d %d\n",a,b);
		can[a][b]=can[b][a]=tim;
	}

	for(i=0;i<n;i++) if(mask&(1<<i))
		for(j=i+1;j<n;j++) if(mask&(1<<j))
		{
			if(f[i][j] && can[i][j]!=tim) return 0;
		}
	return 1;	
}

vi all;

void solve(int u,int s,int tot,int mask)
{
	int i;

	if(u>=n) return ;

	//printf("%d %d %d %d\n",u,s,tot,mask);

	for(i=u+1;i<n;i++)
	{
		if(!f[u][i]) continue;
		now[tot]=i;
		solve(i,s,tot+1,mask|(1<<i));
	}

	if(f[u][s] && tot>2)
	{
		if(check(tot,mask))
		{
			//printf("%d %d\n",mask,tot);
			all.pb(mask);
			ans=MIN(ans,tot);
		}
	}
}

int sol,color[10];
vi res;

void bktk(int pos,int maxc)
{
	int i,j,allc= (1<<maxc) -1;

	if(pos==n)
	{
		int ok=1;

		for(i=0;i<all.size() && ok;i++)
		{
			int mask=all[i],flag=0;

			for(j=0;j<n;j++)
				if(mask&(1<<j)) 
					flag|=(1<<color[j]);

			if(flag!=allc) ok=0;
		}

		if(!ok) return ;

		for(i=0;i<n;i++)
			res.pb(color[i]);
		
		sol=1;
		return ;
	}

	for(i=0;i<maxc;i++)
	{
		color[pos]=i;
		bktk(pos+1,maxc);
		if(sol) return ;
		if(pos==0) break;
	}
}

int A[2005],B[2005];

int main()
{
	int i,j,k,tests,cs=0;

	//freopen("E:\\GCJ\\Asmall.in","r",stdin);
	freopen("E:\\GCJ\\Clarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		cin>>n>>m;
		MEM(f,0);

		for(i=0;i<m;i++) cin>>A[i];
		for(i=0;i<m;i++) cin>>B[i];

		for(i=0;i<m;i++)
		{
			int u=A[i],v=B[i];
			--u;--v;
			f[u][v]=f[v][u]=1;
		}

		for(i=0;i<n;i++)
		{
			f[i][(i+1)%n]=1;
		}

		ans=inf;
		all.clear();

		for(i=0;i<n;i++)
		{
			now[0]=i;
			solve(i,i,1,(1<<i));
		}

		//for(i=0;i<all.size();i++)
		//	printf("%d\n",all[i]);

		sol=0;
		res.clear();

		for(i=ans;i>=1;i--)
		{
			ans=i;
			bktk(0,i);
			if(sol) break;
		}


		printf("Case #%d: %d\n",++cs,ans);
		for(i=0;i<res.size();i++)
		{
			if(i) printf(" ");
			printf("%d",res[i]+1);
		}
		puts("");
	}

	return 0;
} 


