//80081TU
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 10E-9;
const double PI = acos(-1.0);

ll mem[1010];

int main () {
	int test;
	cin >> test;
	for(int q=1 ; q<=test ; q++) {
	
		memset(mem, 0, sizeof(mem));

		ll L, t, N, C;
		cin >> L >> t >> N >> C;
		vector<int> as(C);
		REP(i, C) cin >> as[i];

		ll ret = 0;		
		for(int i=0 ; i<N ; i++) {
			ret += as[i%C]*2;
			mem[i+1] = ret;
//			cout << mem[i+1] << " ";
		}
//		cout << endl;

		if( L == 1) {
			ll mn = 1000000000;
			for(int i=0 ; i<N ; i++) {
				ll nret = ret;
				ll tmp = 0;
				if(mem[i] >= t ) {
					nret -= (mem[i+1]-mem[i])/2;
					tmp = -(mem[i+1]-mem[i])/2;
				}else {
					ll d = (mem[i+1]-mem[i])/2;
					nret -= (mem[i+1]-mem[i]);
					tmp -= (mem[i+1]-mem[i]);
					
					ll timel = (t-mem[i]);
					nret += timel;
					tmp += timel;
					d -= timel/2;
					if(d > 0) {
						nret += d;
						tmp += d;
					}
				}
				mn = min(mn, nret);
			}
			ret = mn;
		} else if(L == 2) {
			ll mn = 1000000000;
			for(int i=0 ; i<N ; i++) for(int j=i+1 ; j<N ; j++){
				ll nret = ret;
				ll tmp = 0;
				if(mem[i] >= t ) {
					nret -= (mem[i+1]-mem[i])/2;
					tmp = -(mem[i+1]-mem[i])/2;
				}else {
					ll d = (mem[i+1]-mem[i])/2;
					nret -= (mem[i+1]-mem[i]);
					tmp -= (mem[i+1]-mem[i]);
					
					ll timel = (t-mem[i]);
					nret += timel;
					tmp += timel;
					d -= timel/2;
					if(d > 0) {
						nret += d;
						tmp += d;
					}
				}

				if(mem[j]+tmp >= t ) {
					nret -= (mem[j+1]-mem[j])/2;
				}else {
					ll d = (mem[j+1]-mem[j])/2;
					nret -= (mem[i+1]-mem[i]);
					
					ll timel = (t-(mem[j]+tmp));
					nret += timel;
					d -= timel/2;
					if(d > 0) {
						nret += d;
						tmp += d;
					}
				}
				mn = min(mn, nret);
			}
			ret = mn;
		}
	
		printf("Case #%d: %lld\n", q, ret);
	
	}

	return 0;
}
