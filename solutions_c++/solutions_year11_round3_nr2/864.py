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

struct pr {
    int val, num;
} Acopy[1111];

bool operator < (const pr &x, const pr &y) {
    return x.val - y.val < 0;
}

int A[1111], B[1000007], Count[1111];

void testcase(int zzz) {
    int l, n, c; LG t; scanf("%d%lld%d%d", &l, &t, &n, &c);
    int sum = 0; LG res = 0, theway = 0;
    FOR(i,0,c) {
	scanf("%d", A + i), sum += A[i];
	Acopy[i] = (pr){ A[i], i };
	Count[i] = 0;
    }
    FOR(i,0,n) {
	B[i] = A[i % c], theway += B[i];
    }
    int ind;
    FOR(i,0,n) {
	if(res < t) res += 2 * B[i];
	if(res >= t) {
	    ind = i;
	    break;
	}
    }
    
    if(t >= theway * 2 || l == 0) {
	printf("Case #%d: %lld\n", zzz, theway * 2);
	return;
    }
    sort(Acopy, Acopy + c);
    FOR(i,ind+1,n) ++Count[i % c];
    
    // start immediately
    LG res1 = theway * 2; int l1 = (res == t ? l : l - 1);
    res1 -= (res - t) / 2;
    FORD(i,c,0) {
	if(l1 > Count[Acopy[i].num]) {
	    l1 -= Count[Acopy[i].num];
	    res1 -= LG(Count[Acopy[i].num]) * Acopy[i].val;
	} else {
	    res1 -= LG(l1) * Acopy[i].val;
	    break;
	}
    }
    
    // start form the next point
    LG res2 = theway * 2;
    
    if(res != t) {
    
    FORD(i,c,0) {
	if(l > Count[Acopy[i].num]) {
	    l -= Count[Acopy[i].num];
	    res2 -= LG(Count[Acopy[i].num]) * Acopy[i].val;
	} else {
	    res2 -= LG(l) * Acopy[i].val;
	    break;
	}
    }
    
    }
    
    printf("Case #%d: %lld\n", zzz, min(res1, res2));
}

int main() {
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
