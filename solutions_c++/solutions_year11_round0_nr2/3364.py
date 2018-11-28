#include <cmath>
#include <string>
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
#define LET(a,b) typeof(b) a=(b)
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
#define FORE(a,b) for(LET(a,(b).begin());a!=(b).end();++a)

#define two(X) (((ll)1)<<(X))

template<class T> inline void ORD(T &a,T &b){if(a>b){T x=a;a=b;b=x;}}

template<class T> inline void mini(T &a,T b){if(b<a)a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a)a=b;}
template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T gcd(T a,T b){if(a<0)a=-a;if(b<0)b=-b;return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){if(a<0)a=-a;if(b<0)b=-b;return a*(b/gcd(a,b));}
template<class T> inline VV<pair<T,int>> factorize(T n)
	{VV<pair<T,int>> R;T _i=1;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.PUB(MP(i,C));}
	i+=_i;_i=2;if (i*i>n) i=n;}if (n>1) R.PUB(MP(n,1));return R;}
template<class T> inline bool prime(T n)
	{if(n<=1)return false;T _i=1;for (T i=2;i*i<=n;i+=_i,_i=2) if (n%i==0) return false;return true;}

//----------------------------------------------


int go() {
	return 0;
}

string solve() {
	char c[40][3];
	char d[30][2];
	char dm[30];

	char res[100];
	int rp = 0;

	CLR(res,0);CLR(dm,0);rp=0;

	int C; cin >> C;
	REP(i, C) {cin >> c[i]; ORD(c[i][0], c[i][1]); DBG(c[i]); }
	int D; cin >> D;
	REP(i, D) {cin >> d[i]; ORD(d[i][0], d[i][1]); DBG(d[i]);}
	int N; cin >> N;

	char last; cin >> last; //DBG(last);
	if(N>1) {
	char x; cin >> x; //DBG(x);
	FOR(i, 1, N) {
		bool br = false;
		if (last != 0) {
			char mi = min(x,last);
			char ma = max(x,last);
			if(!br)
				REP(j,D)
					if(d[j][0]==last||d[j][1]==last) {
						if(dm[j]!=0&&last!=dm[j]) {
							CLR(res,0);CLR(dm,0);rp=0;
							last=x;
							br=true;
							break;
						}
					}
			if(!br)
				REP(j,C)
					if (c[j][0]==mi && c[j][1]==ma){
						last=0;
						res[rp++]=c[j][2];
						br=true;
						break;
					}
			if(!br)
				REP(j,D)
					if(d[j][0]==last||d[j][1]==last) {
						if(dm[j]!=0&&last!=dm[j]) {
						}
						else {
							dm[j]=last;
						}
					}
			if(!br) res[rp++]=last;
		}
		if(!br)last = x;
		if (i==N-1)break;
		cin >> x; //DBG(x);
	}
	if(last!=0)
		REP(j,D)
			if(d[j][0]==last||d[j][1]==last) {
				if(dm[j]!=0&&last!=dm[j]) {
					CLR(res,0);CLR(dm,0);rp=0;
					last=0;
					break;
				}
			}
	}
	if(last!=0) res[rp++]=last;
	DBG(res);

	string s;
	s="[";
	REP(i,rp-1){s.append(&res[i],1);s.append(", ");}
	if (rp>0)s.append(&res[rp-1],1);
	s.append("]");

	//getline(cin,line);
	return s;
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
	COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
	int caseCount; cin >> caseCount;
	string temp; getline(cin,temp);
	FOR (c, 1, caseCount) {
		DBG(c);
		printf("Case #%lld: ", c);
		cout << solve() <<endl;
	}
	return 0;
}
