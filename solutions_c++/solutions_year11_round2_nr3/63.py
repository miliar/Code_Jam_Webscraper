//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>


//Other Includes
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

using namespace std;

#define FOR(i,a,b)					for(int i=a;i<b;i++)
#define REP(i,n)					FOR(i,0,n)
#define pb						 	push_back
#define mp						 	make_pair
#define s(n)						scanf("%d",&n)
#define sl(n) 						scanf("%lld",&n)
#define sf(n) 						scanf("%lf",&n)
#define ss(n) 						scanf("%s",n)
#define fill(a,v) 					memset(a, v, sizeof a)
#define sz							size()
#define INF							(int)1e9
#define EPS							1e-9
#define bitcount					__builtin_popcount
#define all(x)						x.begin(), x.end()
#define gcd							__gcd
#define maX(a,b)					(a>b?a:b)
#define miN(a,b)					(a<b?a:b)

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef pair<int, int > PII;

/*Main code begins now */
int testnum;
int N,M;
int u[10];
int v[10];
vector<vector<int> > pt;
bool adj[10][10];
vector<int> masks;

vector<int> bestsoln;
int best;
vector<int> soln;

bool walled(int a,int b,int x,int y)
{
	if(a>b) return walled(b,a,x,y);
	if(a<x && x<b && (y>b || y<a)) return true;
	if(a<y && y<b && (x>b || x<a)) return true;
	return false;
}

void preprocess()
{

}

int bitcount(int n)
{
	if(n==0) return 0;
	return 1+bitcount(n&(n-1));
}

bool done[10];
bool feasible(int c)
{

	for(int i=0;i<pt.size();i++)
	{
		fill(done,false);
		for(int j=0;j<pt[i].size();j++)
			done[ soln[pt[i][j]] ] =true;
		for(int j=0;j<c;j++)
			if(!done[j])
				return false;
	}
	return true;
}
		

void solve()
{
	pt.clear();
	
	for(int i=0;i<N;i++)
		for(int j=i;j<N;j++)
		{
			adj[i][j]=true;
			for(int k=0;k<M;k++)
				if(walled(i,j,u[k],v[k]))
				{
					adj[i][j]=false;
					break;
				}
			adj[j][i]=adj[i][j];
		}
		
	
		
	masks.clear();
	
	for(int mask=(1<<N)-1;mask>=0;mask--)
	{
		if(bitcount(mask)<3) continue;
		bool good=true;
		for(int i=0;i<masks.size();i++)
		{
			if((mask & (~masks[i])) == 0)
			{
				good=false;
				break;
			}
		}
		if(!good) continue;
		
		bool ok=true;
		for(int i=0;i<N;i++)
		{
			if((mask&(1<<i))==0) continue;
			for(int j=0;j<N;j++)
			{
				if((mask&(1<<j))==0) continue;
				
				if(!adj[i][j])
				{
					ok=false;
					break;
				}
			}
			if(!ok) break;
		}
		
		if(ok)
		{
			vector<int> temp;
			for(int i=0;i<N;i++)
				if(mask&(1<<i))
					temp.pb(i);
			pt.pb(temp);
			masks.pb(mask);
		}
			
		
	}
	
	// for(int i=0;i<pt.size();i++)
	// {
		// for(int j=0;j<pt[i].size();j++)
			// printf("%d ",pt[i][j]);
		// printf("\n");
	// }
	// printf("\n");
	
	soln.resize(N);
	bestsoln.resize(N);
	
	int col=5;
	int lim =(int)(pow(col,8));
	for(int mask=0;mask<lim;mask++)
	{
		int x=mask;
		for(int i=0;i<N;i++)
		{
			soln[i]=x%col;
			x=x/col;
		}
		
		if(feasible(col))
		{
			printf("Case #%d: %d\n",testnum,col);
			for(int i=0;i<N;i++)
				printf("%d%c",1+soln[i],(i==N-1)?'\n':' ');
			return;
		}
	}
	
	
	col=4;
	lim =(int)(pow(col,8));
	for(int mask=0;mask<lim;mask++)
	{
		int x=mask;
		for(int i=0;i<N;i++)
		{
			soln[i]=x%col;
			x=x/col;
		}
		
		if(feasible(col))
		{
			printf("Case #%d: %d\n",testnum,col);
			for(int i=0;i<N;i++)
				printf("%d%c",1+soln[i],(i==N-1)?'\n':' ');
			return;
		}
	}
	
	
	col=3;
	lim =(int)(pow(col,8));
	for(int mask=0;mask<lim;mask++)
	{
		int x=mask;
		for(int i=0;i<N;i++)
		{
			soln[i]=x%col;
			x=x/col;
		}
		
		if(feasible(col))
		{
			printf("Case #%d: %d\n",testnum,col);
			for(int i=0;i<N;i++)
				printf("%d%c",1+soln[i],(i==N-1)?'\n':' ');
			return;
		}
	}

}

bool input()
{
	s(N); s(M);
	for(int i=0;i<M;i++)
	{
		s(u[i]); 
		u[i]--;
	}
	for(int i=0;i<M;i++)
	{
		s(v[i]); 
		v[i]--;
	}
		
	return true;
}


int main()
{
	preprocess();
	int T; s(T);
	for(testnum=1;testnum<=T;testnum++)
	{
		if(!input()) break;
		solve();
	}
}
