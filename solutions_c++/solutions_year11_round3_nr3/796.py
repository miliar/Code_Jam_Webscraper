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

int A[111];

void testcase(int zzz) {
    int n, l, h; scanf("%d%d%d", &n, &l, &h);
    FOR(i,0,n) scanf("%d", A + i);
    bool flag = false; int res;
    FOR(i,l,h+1) {
	bool ok = true;
	FOR(j,0,n) {
	    if(i % A[j] != 0 && A[j] % i != 0) ok = false;
	}
	if(!ok) continue;
	res = i; flag = true;
	break;
    }
    printf("Case #%d: ", zzz);
    if(!flag) printf("NO\n");
    else printf("%d\n", res);
}

int main() {
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
