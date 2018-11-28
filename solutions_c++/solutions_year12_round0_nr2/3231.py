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
using namespace std;
#define pb push_back
#define pf push_front
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
#define All(s) s.begin(),s.end()
#define rAll(s) s.rbegin(),s.rend()
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
int dp[110][110];
int main()
{
	int i,j,k,n,s,p,t,ti;
	cin>>t;
	rep(i,t){
		cin>>n>>s>>p;int ret=0;
		rep(j,110) rep(k,110) dp[j][k]=0;
		rep(j,n){
			cin>>ti;
			rep(k,s+1){
				if(ti<1){
					if(p<1) dp[j+1][k]>?=dp[j][k]+1;
				}
				else if(ti%3==2 || ti%3==0){
					int x=(ti+1)/3;
					if(x>=p) dp[j+1][k]>?=dp[j][k]+1;
					if(x+1==p) dp[j+1][k+1]>?=dp[j][k]+1;
				}
				else{
					if(ti/3+1>=p) dp[j+1][k]>?=dp[j][k]+1;
				}
				dp[j+1][k]>?=dp[j][k];
			}
		}
		rep(j,s+1) ret>?=dp[n][j];
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}
