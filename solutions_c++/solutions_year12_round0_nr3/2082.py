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

int len10(int x) {
    if(x > 999999) return 1000000;
    if(x > 99999) return 100000;
    if(x > 9999) return 10000;
    if(x > 999) return 1000;
    if(x > 99) return 100;
    if(x > 9) return 10;
    else return 1;
}

int cut(int x, int k) {
    return x%10 * k + x/10;
}

void testcase(int zzz) {
    int a, b, res = 0;
    scanf("%d%d", &a, &b);
    FOR(i,a,b) {
	int n = len10(i), y = cut(i, n);
	while(i != y) {
	    if(i < y && y <= b) ++res;
	    y = cut(y, n);
	}
    }
    printf("Case #%d: %d\n", zzz, res);
}

int main() {
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
