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
#define cl clear()
#define inf (int)1e9
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double DD;
typedef long long LL;

int N,K;
VS test;

bool ok(int a,int b) {
	if(a>=0 && a<N && b>=0 && b<N) return 1;
	return 0;
}

int check() {
	string temp,R,B;
	int r,b;
	r=b=0;
	R=B="";
	REP (i,K) {
		R.pb('R');
		B.pb('B');
	}
	REP (i,N) REP (j,N) {
		temp="";
		REP (k,K) {
			if(ok(i,k+j)) temp.pb(test[i][k+j]);
		}
		if(temp==R) r=1;
		if(temp==B) b=2;
		temp="";
		REP (k,K) {
			if(ok(k+i,k+j)) temp.pb(test[k+i][k+j]);
		}
		if(temp==R) r=1;
		if(temp==B) b=2;
	}
	return r+b;
}

int main() {
	string temp;
	int a,b,yay=0;
	for (int _=GI;_--;) {
		N=GI,K=GI;
		test.rz(N);
		REP (i,N) {
			cin>>test[i];
			temp="";
			REP (j,test[i].sz) {
				if(test[i][j]=='.') continue;
				temp.pb(test[i][j]);
			}
			while(temp.sz<N) temp="."+temp;
			test[i]=temp;
		}
		a=check();
		VS x;
		x.rz(N);
		REP (j,test[0].sz) REP (i,test.sz) x[j].pb(test[i][j]);
		test=x;
		REP (i,test.sz) reverse(test[i].begin(),test[i].end());
		b=check();
		if(a==3 || b==3) printf("Case #%d: Both\n",++yay);
		else if(a+b==3) printf("Case #%d: Both\n",++yay);
		else if(a==1 || b==1) printf("Case #%d: Red\n",++yay);
		else if(a==2 || b==2) printf("Case #%d: Blue\n",++yay);
		else printf("Case #%d: Neither\n",++yay);
	}
	return 0;
}

