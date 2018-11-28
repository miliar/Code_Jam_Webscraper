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

char T[55][55];

void testcase(int zzz) {
    int r, c; scanf("%d%d", &r, &c);
    FOR(i,0,r) {
	scanf("%s", T[i]);
    }
    bool flag = true;
    FOR(i,0,r) {
	FOR(j,0,c) {
	    if('a' <= T[i][j] && T[i][j] <= 'd') continue;
	    bool ok = false;
	    if(i != 0) {
		if(T[i - 1][j] == 'a' && T[i - 1][j + 1] == 'b') {
		    if(T[i][j] != '#' || T[i][j + 1] != '#') flag = false;
		    T[i][j] = 'c', T[i][j + 1] = 'd';
		    ok = true;
		}
	    }
	    if(!ok) {
		if(T[i][j] == '#' && T[i][j + 1] == '#') {
		    T[i][j] = 'a', T[i][j + 1] = 'b';
		    if(i == r - 1) flag = false;
		}
	    }
	    if(T[i][j] == '#') flag = false;
	}
    }
    printf("Case #%d:\n", zzz);
    if(flag) {
	FOR(i,0,r) {
	    FOR(j,0,c) {
		if(T[i][j] == 'a' || T[i][j] == 'd') T[i][j] = '/';
		if(T[i][j] == 'b' || T[i][j] == 'c') T[i][j] = '\\';
		printf("%c", T[i][j]);
	    }
	    printf("\n");
	}
    } else printf("Impossible\n");
}

int main() {
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
