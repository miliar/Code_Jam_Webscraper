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

int main () {
	int test;
	cin >> test;
	for(int t=1 ; t<=test ; t++) {
	
		ll n, l , h;
		cin >> n >> l >> h;
	
		vector<ll> notes(n);
		REP(i, n) cin >> notes[i];

		int ret;
		bool found = false;
		for(int i=l ; i<=h && !found ; i++) {
			bool valid = true;
			for(int j=0 ; j<SZ(notes) && valid ; j++)
				valid = valid && (notes[j]%i==0 || i%notes[j] == 0);
		
			if(valid) {
				found = true;
				ret = i;
			}
		}
	
		printf("Case #%d: ", t);
		if(!found) printf("NO\n");
		else printf("%d\n", ret);
	
	
	
	}

	return 0;
}
