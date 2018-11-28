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

int a[100],dp[101][256];

int main()
{
	int CS; cin>>CS;
	rep(cs,CS)
	{
		int d,ins,m,n; cin>>d>>ins>>m>>n;
		rep(i,n)cin>>a[i];
		int ans=inf;
		
		rep(i,n)cerr<<a[i]<<(i==n-1?"\n":" ");
		
		rep(i,n+1)rep(j,256)dp[i][j]=inf;
		rep(i,256)dp[0][i]=0;
		
		for(int i=1;i<=n;i++)for(int j=0;j<=255;j++)
		{
			//del
			dp[i][j]=min(dp[i][j],dp[i-1][j]+d);
			
			//change ai-1 to x and insert appropriate terms to k
			for(int x=max(0,j-m);x<=min(255,j+m);x++)for(int k=0;k<=255;k++)
			{
				if(m==0&&k!=x)continue;
				
				int iscost;
				if(m==0)iscost=0;
				else iscost=abs(x-k)/m+(abs(x-k)%m!=0);
				
				if(iscost<0)iscost=0;
				else iscost*=ins;
				
				dp[i][k]=min(dp[i][k],dp[i-1][j]+abs(a[i-1]-x)+iscost);
			}
		}
		
		rep(i,256)ans=min(ans,dp[n][i]);
		cout<<"Case #"<<cs+1<<": "<<ans<<endl;
	}
	
	return 0;
}
