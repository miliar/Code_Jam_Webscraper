#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>

#define rep(i,n) for(int i=0;i<n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define rp(i,c) rep(i,(c).size())
#define fr(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pi;
const int inf=1<<28;
const double INF=1e12,EPS=1e-9;

int nm[1024],cost[1024],ans;
int dp[11][1024][11];

int main()
{
	int CS; cin>>CS;
	rep(cs,CS)
	{
		int p; cin>>p;
		
		int begin[11]; begin[0]=0;
		rep(i,10)begin[i+1]=begin[i]+(1<<(p-i-1));
		
		//rep(i,10)dbg(begin[i]);
		
		rep(i,1<<p)
		{
			int t; cin>>t;
			nm[i]=p-t;
		}
		rep(i,p)rep(j,1<<(p-i-1))cin>>cost[begin[i]+j];
		
		rep(i,p+1)rep(j,1<<p)rep(k,p+1)dp[i][j][k]=inf;
		rep(i,1<<p)for(int j=nm[i];j<=p;j++)dp[0][i][j]=0;
		
		
		for(int i=1;i<=p;i++)rep(j,1<<(p-i))rep(k,p+1)
		{
			assert(begin[i]+j<(1<<p));
			
			dp[i][j][k]=min(dp[i][j][k],
				cost[begin[i-1]+j]+dp[i-1][2*j][min(p,k+1)]+dp[i-1][2*j+1][min(p,k+1)]);
			dp[i][j][k]=min(dp[i][j][k],dp[i-1][2*j][k]+dp[i-1][2*j+1][k]);
		}
		
		//dbg(dp[2][0][0]);
		
		cout<<"Case #"<<cs+1<<": "<<dp[p][0][0]<<endl;
	}
	
	return 0;
}
