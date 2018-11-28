#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GI64 ({int64 t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GS ({string s;cin>>s;s;})
#define f(i,a,b) for(int i=a;i<b;i++)
#define rf(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-9

typedef long long int64;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

#define is istringstream
#define os ostringstream

const int MOD=10000;
string a,b;
int dp[1005][1005];
int n,m;

int go(int i,int j){
	if(i==n)return 1;
	if(j==m)return 0;
	if(dp[i][j]>=0)return dp[i][j]%MOD;
	int m1=0;
	if(a[i]==b[j])m1=go(i+1,j+1)%MOD;
	return dp[i][j]=((m1%MOD)+(go(i,j+1)%MOD))%MOD;
}

//char ch;
int main(){
	a="welcome to code jam";
	n=sz(a);
	int cnt=0;
	int t=GI;
	cin.get();
	while(t--){
		cnt++;
		SET(dp,-1);
		getline(cin,b);
		m=sz(b);
		int ans=go(0,0)%MOD;
		os s;
		s<<"0000"<<ans;
		string temp1=s.str(),temp2="";
		int x=sz(temp1);
		f(i,0,4)temp2+=temp1[x-i-1];
		reverse(all(temp2));
		cout<<"Case #"<<cnt<<": "<<temp2<<endl;
	}
	return 0;	
}
