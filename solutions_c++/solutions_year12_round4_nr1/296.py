#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
#include<complex>
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
typedef complex<double> pt;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int dp[11000],dis[11000],len[11000];
int main()
{
	int i,j,k,n,g,t;
	cin>>t;
	rep(i,t){
		cin>>n;int f=0;
		memset(dp,0,sizeof(dp));
		rep(j,n) scanf("%d %d",&dis[j],&len[j]);cin>>g;
		dp[0]=dis[0];
		rep(j,n){
			REP(k,j+1,n){
				if(dis[j]+dp[j]<dis[k]) break;
				dp[k]>?=min(len[k],dis[k]-dis[j]);
			}
		}
		rep(j,n){
			if(dp[j]>0 && dp[j]+dis[j]>=g) f=1;
		}
		if(f>0) printf("Case #%d: YES\n",i+1);
		else printf("Case #%d: NO\n",i+1);
	}
	return 0;
}
