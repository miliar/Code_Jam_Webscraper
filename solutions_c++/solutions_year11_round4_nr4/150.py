#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <string>
#include <numeric>
#include <iostream>
#include <sstream> 
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define ll long long
#define ull unsigned long long
#define ld long double
#define VV vector
#define VI VV<int>
#define VL VV<ll>
#define VS VV<string>
#define MP(x,y) make_pair(x,y)
#define SS(a) ((int)((a).size()))
#define PUB push_back
#define POF pop_front
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND=0;
#define DBG(x){if(COND>0){COND--;cerr<<__LINE__<<" "<<#x<<" "<<x<<endl;cerr.flush();}}

#define REP(i,n) FOR(i,0,(n)-1)
#define FOR(i,a,b) for(ll i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(ll i=(a),_b=(b);i>=_b;--i)

#define two(X) (((ll)1)<<(X))
template<class T> inline void mini(T &a,T b){if(b<a)a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a)a=b;}
template<class T> inline void ord(T &a,T &b){if(a>b){T x=a;a=b;b=x;}}
template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T gcd(T a,T b){if(a<0)a=-a;if(b<0)b=-b;return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){if(a<0)a=-a;if(b<0)b=-b;return a*(b/gcd(a,b));}
template<class T> inline VV<pair<T,int>> factorize(T n)
	{VV<pair<T,int>> R;T _i=1;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.PUB(MP(i,C));}
	i+=_i;_i=2;if (i*i>n) i=n;}if (n>1) R.PUB(MP(n,1));return R;}
template<class T> inline bool prime(T n)
	{if(n<=1)return false;T _i=1;for (T i=2;i*i<=n;i+=_i,_i=2) if (n%i==0) return false;return true;}

//----------------------------------------------

bool w[401][401];
bool con[401];
int P,W;
int di[401];
int ti[401];
bool tr[401][401];

bool co[401][401];

int bc, bt;

void setb() {
	int c = 0, t = 0;
	bool tr[401];
	CLR(tr, false);
	FOR(i, 1, P-1) {
		if(con[i]) c++;
		else
			REP(j,P) {
				if(w[i][j] && con[j]) {tr[i]=true; break;}
			}
	}
	REP(i,P) if(tr[i]) t++;
	if (bc > c || (bc == c && bt < t)) {bc=c;bt=t;}
}

void doit() {
	int c = 0;
	REP(i, P) 
		if(con[i]) {
			if(w[i][1]) { setb(); return; }
			c++;
			if(c> bc) return;
		}
	FOR(i, 0, P-1){
		if(!con[i]) continue;
		FOR(j, 1, P-1){
			if(con[j]) continue;
			if(w[i][j]) {
				con[j] = true;
				doit();
				con[j] = false;
			}
		}
	}

}

void solve() {
	cin >> P >>W;
	CLR(w,false);
	CLR(con,false);
	con[0] = true;
	CLR(di,P+1);
	CLR(ti,0);
	CLR(tr, false);
	CLR(co,false);
	bc=P+12;bt=0;
	int x,y;
	char c;
	REP(i,W){
		cin >> x >> c>>y;
		w[x][y] = w[y][x] = true;
	}

	di[0] = 0;
	//FOR(i,1,P-1) if(w[0][i]) {ti[0]++; tr[0][i] = true;}
	bool t3[401];
	CLR(t3, false);
	FOR(i, 1, P-1) {
		REP(j, P) {
			if(di[j]<i) {
				REP(k,P) {
					if(di[k]>=i && w[j][k]) {
						di[k] = i;
						CLR(t3, false);
						int t = 0;
						REP(l, P) {
							if(!co[j][l] && j != l && (tr[j][l] || w[j][l])) {t3[l]=true; t++;}
						}
						if(t>ti[k]) {
							memcpy(co[k], co[j], sizeof(co[j]));
							co[k][j] = true;
							memcpy(tr[k], t3, sizeof(t3));
							ti[k] = t;
						}
					}
				}
			}
		}
	}
	bc = di[1] - 1;
	bt = ti[1];


//	doit();

	//getline(cin,line);
	//return 0;
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
	COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
	int caseCount; cin >> caseCount;
	string temp; getline(cin,temp);
	FOR (c, 1, caseCount) {
		solve();
		printf("Case #%lld: %d %d\n", c, bc, bt);
	}
	return 0;
}
