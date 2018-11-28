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

int R,C,test[32],fin[32][32];

int chk(int a, int b, int c, int d) {
	int p=(fin[a][b]+1)%2;
	int l=c-a;
	l=l%2;
	if(l==1) l=0;
	else l=1;
	FOR (i,a,c) FOR (j,b,d) {
		if(fin[i][j]==999) return 0;
	}
	FOR (i,a,c) {
		FOR (j,b,d) {
			if(fin[i][j]==p) return 0;
			p=(p+1)%2;
		}
		p=(p+l)%2;
	}
	FOR (i,a,c) FOR (j,b,d) {
		fin[i][j]=999;
	}
	return 1;
}

int rec(int A) {
	int cnt=0;
	FOR (i,A,R+1) FOR (j,A,C+1)
		if(chk(i-A,j-A,i,j)) cnt++;
	return cnt;
}

VI m,n;

int main() {
	int T,cnt,sum,yay=0;
	for (int _=GI;_--;) {
		R=GI,C=GI;
		REP (i,R) scanf(" %x",&test[i]);
		REP (i,R) {
			REP (j,C) fin[i][j]= (test[i] &(1<<j)) ? 1 : 0;
			reverse(fin[i],fin[i]+C);
		}
/*		
		cout<<endl;
		REP (i,R) {
			REP (j,C) cout<<fin[i][j];
			cout<<endl;
		}
		cout<<endl;
*/
		T=min(R,C);
		sum=0;
		m.cl;
		n.cl;
		for (int i=T;i>=2;i--) {
			cnt=rec(i);
			sum += cnt*i*i;
			if(cnt) m.pb(i),n.pb(cnt);
		}
		printf("Case #%d: %d\n",++yay,(m.sz + ((R*C-sum>0)?1:0)) );
		REP (i,m.sz) printf("%d %d\n",m[i],n[i]);
		if(R*C-sum>0) printf("1 %d\n",R*C-sum);
	}
	return 0;
}

