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

#define BIG (12345678 / 50) * 9

LG S[555];
int X[555];

void testcase(int zzz) {
    int n;
    scanf("%d", &n);
    bool flag = false;
    FOR(i,0,n) scanf("%lld", &S[i]);
    FOR(i,0,BIG) {
	FOR(i,0,n) X[i] = rand() % 859;
	LG s1 = 0, s2 = 0;
	FOR(i,0,n) {
	    if(X[i] < 320) s1 += S[i];
	    else if(X[i] < 640) s2 += S[i];
	}
	if(s1 == s2) { flag = true; break; }
    }
    printf("Case #%d:\n", zzz);
    if(flag) {
	FOR(i,0,n) {
	    if(X[i] < 320) printf("%lld ", S[i]);
	} printf("\n");
	FOR(i,0,n) {
	    if(320 <= X[i] && X[i] < 640) printf("%lld ", S[i]);
	} printf("\n");
    }
    else printf("Impossible\n");
}

int main() {
    srand(time(NULL));
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
