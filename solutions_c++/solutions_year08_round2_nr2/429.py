#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef int LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(0)printf
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))


template<typename T>
T gcd(T x, T y) {
	while ( y != 0 ) {
		T z = x % y;
		x = y;
		y = z;
	}
	return x;
}


vector<LL> primos;

void genera_primos(LL maxprimo){
	primos.PB(2);
	for (LL i=3; i<=maxprimo; i++) {
		bool es=true;
		FOREACH(it, primos) {
			if (i%(*it)==0) {es=false; break;}
		}
		if (es) {primos.PB(i);}
	}
}

bool same(LL x, LL y, LL p) {
	if (gcd(x, y)<p) return false;
	vector<LL>::iterator it;
	it=lower_bound(primos.begin(), primos.end(), p);
	while (*it<=x && *it<=y) {
		if (x%(*it)==0 && y%(*it)==0) {debug("(%d %d):%d\n", x, y, *it);return true;}
		it++;
	}
	return false;
}
	

LL A, B, P;
int t[10000];
int group[10000];

int main() {
	int ncaso;
	genera_primos(10000);
	//printf("%d\n", primos.size());
	//FOREACH(it, primos) printf("-->%lld\n", *it);		

	scanf(" %d", &ncaso);
	FOR(icaso, 1, ncaso) {
		printf("Case #%d: ", icaso);
		cin >> A >> B >> P;
		memset(t, 0, sizeof(t));
		for (int i=0; i<=B-A; i++) group[i]=i;
		for (LL  i=A; i<B; i++) {
			for (LL j=i+1; j<=B; j++) {
				if (same(i, j, P)) {
					int temp=min(group[i-A], group[j-A]);
					int temp2=max(group[i-A], group[j-A]);
					for (int k=0; k<=B-A; k++) if (group[k]==temp2) group[k]=temp;
				}
			}
		}
		//for (int qq=0; qq<=B-A; qq++) printf(" %d", group[qq]);
		int dist=B-A+1;
		for (int i=0; i<=B-A; i++) {
			if (group[i]!=i) dist--;
		}
		printf("%d\n", dist);
	}

	return 0;
}
