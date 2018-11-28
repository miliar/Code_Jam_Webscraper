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

ll ms=0, mt=0;

ll sco=0, tu=1;
int c[80], s[80], t[80];
int n, m;
int gone[80];

void go(int x);

void next(int x) {
		bool found=false;
		FOR(i,0,n-1){
			if(gone[i]==0 && t[i]>0) {
				go(i);
				found=true;
				break;
			}
		}

		if(!found){
			int hs=0;
			FOR(i,0,n-1){
				if(gone[i]==0&&c[i]==2)maxi(hs,s[i]);
			}
			FOR(i,0,n-1){
				if(c[i]!=2)continue;
				if(gone[i]==0 && s[i]==hs) {
					go(i);
					found=true;
					break;
				}
			}

			hs=0;
			FOR(i,0,n-1){
				if(gone[i]==0&&c[i]==1)maxi(hs,s[i]);
			}
			FOR(i,0,n-1){
				if(c[i]!=1)continue;
				if(gone[i]==0 && s[i]==hs) {
					go(i);
					found=true;
					break;
				}
			}

			hs=0;
			FOR(i,0,n-1){
				if(gone[i]==0&&c[i]==0)maxi(hs,s[i]);
			}
			if(hs>0) {
				FOR(i,0,n-1){
					if (c[i]!=0)continue;
					if(gone[i]==0 && s[i]==hs) {
						go(i);
						found=true;
						break;
					}
				}
			}
		}

		if(!found)maxi(ms,sco);
}

void go(int x) {
	sco += s[x];
	tu += t[x] - 1;
	int n_ = n;
	n += c[x];
	mini(n,m);
	gone[x] = 1;

	if(tu == 0) {
		maxi(ms,sco);
	}
	else {
		next(x);	
	}

	sco -= s[x];
	tu -= t[x] - 1;
	n = n_;
	gone[x] = 0;
}

ll solve() {
	sco=0, tu=1;
	ms=0, mt=0;
	CLR(gone, 0);
	cin >> n;
	REP(i,n) cin >> c[i] >> s[i] >>t[i];
	cin >> m;
	m+=n;
	FOR(i,n,m-1) cin >> c[i] >> s[i] >>t[i];
	DBG(n);
	DBG(m);
	//getline(cin,line);

	REP(i,m)if(c[i]+t[i]+s[i]==0)gone[i]=1;

	next(-1);

	return ms;
}

int main(int argc, char ** argv) { ios::sync_with_stdio(false);
	COND = argc >= 2 && argv[1][0] == 'q' ? (int)1e9 : 0;
	int caseCount; cin >> caseCount;
	string temp; getline(cin,temp);
	FOR (c, 1, caseCount) {
			DBG(c);
printf("Case #%lld: %lld\n", c, solve());
	}
	return 0;
}
