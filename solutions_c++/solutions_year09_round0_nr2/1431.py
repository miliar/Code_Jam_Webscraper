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
#define small(a,b,c,d) min((a),min((b),min((c),(d))))

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef double D;
typedef long long LL;

int H,W,test[105][105];
char ans[105][105],p;

char rec(int a, int b) {
	int n,w,e,s,t;
	char c;
	n=w=e=s=1e9;
	if(ans[a][b]!='.') return ans[a][b];
	if(a-1>=0) n=test[a-1][b];
	if(a+1<H) s=test[a+1][b];
	if(b-1>=0) w=test[a][b-1];
	if(b+1<W) e=test[a][b+1];
	t=small(n,s,w,e);
	if(t>=test[a][b]) { p++; ans[a][b]=p; return p; }

	if(n==t)
		c=rec(a-1,b);
	else if(w==t)
		c=rec(a,b-1);
	else if(e==t)
		c=rec(a,b+1);
	else
		c=rec(a+1,b);
	ans[a][b]=c;
	return c;
}

void orderify() {
	char h='a',ind[26];
	REP (i,26) ind[i]='.';
	REP (i,H) REP (j,W) {
		if(ind[ans[i][j]-'a']=='.') ind[ans[i][j]-'a']=h++;
		ans[i][j]=ind[ans[i][j]-'a'];
	}
}

int main() {
	char c;
	int cnt=1;
	for(int _=GI;_--;) {
		H=GI;
		W=GI;
		REP (i,H) REP (j,W) test[i][j]=GI;
		REP (i,105) REP (j,105) ans[i][j]='.';
		p='a'-1;
		REP (i,H) REP (j,W)
			if(ans[i][j]=='.') {
				c=rec(i,j);
				ans[i][j]=c;
			}
		orderify();
		printf("Case #%d:\n",cnt++);
		REP (i,H) {
			REP (j,W) printf("%c ",ans[i][j]);
			printf("\n");
		}
	}
	return 0;
}

