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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include<climits>
using namespace std;
#define SZ(a) int((a).size())
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(),(c).end()
#define TR(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define FOR(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define REV(i,a,b) for(int i=(int)a;i>(int)b;i--)
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define SETBIT(a,b) a|=(1<<b)
#define UNSETBIT(a,b) a&=~(1<<b)
#define GETBIT(a,b) a&(1<<b)
#define FILL(a,b) memset(a,b,sizeof(a))
#define NBITS(a) __builtin_popcount(a)
#define INF 1000000000
#define EPS 1e-9
typedef long long LL;
typedef pair<int,int> PII;
vector<int> VI;
vector<vector<int> > VVI;
vector<string> VS;
////////// ACUTAL CODE STARTS HERE /////////
int D,I,M,N,A[105],dp[105][260];

int cost_insert(int x,int y)
{
	int ret;
	if(abs(x-y)%M!=0) return abs(x-y)/M;
	if(x==y) 
		return 0;
	return (abs(x-y)/M)-1;
}

int find()
{
	REP(i,100) REP(j,256) dp[i][j]=INF;
	
	///////////////////////////BASE CASE/////////////////////////
	
	//modify to some number
	for(int j=0;j<256;j++) dp[1][j]=min(dp[1][j],abs(A[1]-j));
	//delete
	
	REP(j,256) dp[1][j]=min(dp[1][j],D);
	
	
	////////////////////////////DP/////////////////////////////
	
	for(int i=2;i<=N;i++)
	{
		//modify to some number
		
		for(int j=0;j<=255;j++)
		{
			for(int k=max(0,j-M);k<=min(255,j+M);k++)
			{
				dp[i][j]=min(dp[i][j],dp[i-1][k]+abs(A[i]-j));
			}
		}	
		//delete
		for(int j=0;j<=255;j++)
		{
			dp[i][j]=min(dp[i][j],dp[i-1][j]+D);
		}
		
		
		//insert
		if(M>0)
		{
			for(int j=0;j<=255;j++)
			{
				for(int k=0;k<=255;k++)
				{
					dp[i][j]=min(dp[i][j],dp[i-1][k]+ I*cost_insert(k,j) +abs(j-A[i]) );
				}
			}	
		}
	}
	
	
	/*for(int i=1;i<=N;i++)
	{
		for(int j=0;j<=255;j++)
			cout<<dp[i][j]<<" ";
		cout<<endl;	
	}
	*/
	int ans=INF;
	REP(i,256) ans=min(ans,dp[N][i]);
	return ans;	
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bsmall.txt","w",stdout);
	int T;
	cin>>T;
	REP(tests,T)
	{
		cin>>D>>I>>M>>N;
		REP(i,N) cin>>A[i+1];
		cout<<"Case #"<<tests+1<<": "<<find()<<endl;
	}
	
 	return 0;
}
