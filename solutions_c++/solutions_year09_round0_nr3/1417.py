#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>

using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf(" %d",&t);t;})
#define GC(x) scanf(" %c",&x)
#define sz size()
#define rz resize
#define inf 1e9
#define pb push_back
#define MOD 10000

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double D;
typedef long long LL;

string test,T;
int dp[505][20];

int rec(int a, int b) {
	int t=0;
	int &ret=dp[a][b];
	if(ret!=-1) return ret;
	if(b==T.sz) return 1;
	FOR (i,a,test.sz)
		if(test[i]==T[b]) { t+=rec(i+1,b+1); t%=MOD; }
	ret= t;
	return ret;
}

string f(int a) {
	string test;
	while(a!=0) {
		test.pb(a%10+'0');
		a/=10;
	}
	reverse(test.begin(), test.end());
	while(test.sz<4) test.insert(test.begin(),'0');
	return test;
}

int main() {
	int p=1,_=GI;
	getchar();
	T="welcome to code jam";
	for(;_--;) {
		getline(cin,test,'\n');
		memset(dp,-1,sizeof(dp));
		cout<<"Case #"<<p++<<": "<<f(rec(0,0))<<endl;
	}
	return 0;
}

