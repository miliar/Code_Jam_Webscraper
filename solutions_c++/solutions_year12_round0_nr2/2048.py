#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

void testcase(int zzz) {
    int res = 0, T, S, p;
    scanf("%d%d%d", &T, &S, &p);
    FOR(i,0,T) {
	int x; scanf("%d", &x);
	if(x%3 == 0 && S > 0 && x/3 < p && x != 0 && x != 30) {
	    if(x/3 + 1 >= p) --S, ++res;
	} else if(x%3 == 0) {
	    if(x/3 >= p) ++res;
	}
	if(x%3 == 1) {
	    if(x/3 + 1 >= p) ++res;
	}
	if(x%3 == 2 && S > 0 && x/3 + 1 < p && x != 29) {
	    if(x/3 + 2 >= p) --S, ++res;
	} else if(x%3 == 2) {
	    if(x/3 + 1 >= p) ++res;
	}
    }
    printf("Case #%d: %d\n", zzz, res);
}

int main() {
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
