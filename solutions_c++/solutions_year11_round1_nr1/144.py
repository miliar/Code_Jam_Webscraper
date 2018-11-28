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


string solve() {
	ll N, PD, PG ;
	cin >> N >> PD >> PG;
	DBG(PD);
	if (PG == 100 && PD < 100) return "Broken";
	if (PG == 0 && PD > 0) return "Broken";
	int f2, f5;
	f2 = PD%4 == 0? 1:PD%2==0?2:4;
	DBG(f2);
	f5 = PD%25 == 0? 1:PD%5==0?5:25;
	DBG(f5);
	DBG(N);
	if(N < f2*f5)return "Broken";
	//getline(cin,line);
	return "Possible";
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
