#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <utility>
#include <sstream>

#define FOR(i,a,n) for(i=(a);i<(n);++i)
#define FORIT(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define f0(a) memset(a,0,sizeof(a))
#define fx(a,x) memset(a,(x),sizeof(a))

#define _bc(i) __builtin_popcount(i)
#define all(v) v.BE,v.EN
#define sz size()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define BE begin()
#define EN end()
#define IT iterator

using namespace std;
typedef vector <int> 	VI;
typedef vector < VI > 	VVI;
typedef vector<string> 	VS;
typedef pair<int,int> 	II;
typedef vector<II > 	VII;
typedef map<int,int> 	MII;
typedef long long 	lint;

#define INF (1<<30)		//or 0x7ffffff0 for 2^31-16 = 2147483647 
#define MINF 0x80000000		//-2^31
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
template<class T> string i2s(T x) { ostringstream o; o<<x; return o.str(); }
int s2i(string x) {int r=0;istringstream sin(x);sin>>r;return r; }
template<class T>
inline void _min(T &mn, T x)
{
	if(mn > x) mn=x;
}
template<class T>
inline void _max(T &mx, T x)
{
	if(mx < x) mx=x;
}
/*******************/


int n,p,s,T[111];
void solve()
{
	int i,j,k,l,best,sur;
	scanf("%d %d %d",&n,&s,&p);
	for(i=0; i<n; i++)
		T[i]=SS;
	bool dp[101][5];
	memset(dp,false,sizeof(dp));
	
	for(i=0; i<n; i++){
		for(j=0; j<=10; j++)
			for(k=j; k<=j+2 && k<=10; k++)
				for(l=k; l<=k+2 && l<=j+2 && l<=10; l++)
					if(j+k+l==T[i]){
						if(k==j+2 ||l==j+2 || l==k+2)			
							sur=1;
						else
							sur=0;
						if(l>=p)
							best=1;
						else
							best=0;
						dp[i][sur*2+best]=true;
						//printf("dp[%d][%d]=%d\n",i,sur*2+best,dp[i][sur*2+best]);
					}
	}
	int ans[111][111];
	memset(ans,0,sizeof(ans));
	
	if(dp[0][2]||dp[0][3])
		ans[0][1]=(dp[0][3]==true)?1:0;
		
	if(dp[0][0] || dp[0][1])
		ans[0][0]=(dp[0][1]==true)?1:0;
	for(i=1; i<n; i++)
		for(j=0; j<=i+1; j++)
		{
			int mx=0;
			if(dp[i][0] || dp[i][1]){
				mx=ans[i-1][j];
				if(dp[i][1])
					mx++;
			}
			if(j>0 && (dp[i][2] || dp[i][3])){
				int mx1=ans[i-1][j-1];
				if(dp[i][3])
					mx1++;
				_max(mx,mx1);
			}
			ans[i][j]=mx;
		}			
	printf("%d\n",ans[n-1][s]);
}

int main()
{
	int t,test;
	scanf("%d\n",&test);
	for(int t=1; t<=test; t++)
	{
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
