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

char Tab[5][5];
int A[5][5];

const char Ans[4][30] = {
	"X won",
	"O won",
	"Draw",
	"Game has not completed"
};

bool checker_hor(char a) {
	FOR(i,0,4) {
		int cc = 0;
		FOR(j,0,4) {
			if(Tab[i][j] == a || Tab[i][j] == 'T') ++cc;
		}
		if(cc == 4) return true;
	}
	return false;
}

bool checker_ver(char a) {
	FOR(j,0,4) {
		int cc = 0;
		FOR(i,0,4) {
			if(Tab[i][j] == a || Tab[i][j] == 'T') ++cc;
		}
		if(cc == 4) return true;
	}
	return false;
}

bool checker_diag(char a) {
	int cc = 0;
	FOR(i,0,4) if(Tab[i][i] == a || Tab[i][i] == 'T') ++cc;
	if(cc == 4) return true;
	cc = 0;
	FOR(i,0,4) if(Tab[i][3-i] == a || Tab[i][3-i] == 'T') ++cc;
	if(cc == 4) return true;
	return false;
}

void testcase(int zzz) {
	FOR(i,0,4) scanf("%s", Tab[i]);
	int counter = 0, ans = -1;
	if(checker_hor('X') || checker_ver('X') || checker_diag('X')) ans = 0;
	else if(checker_hor('O') || checker_ver('O') || checker_diag('O')) ans = 1;
	else {
		FOR(i,0,4) FOR(j,0,4) {
			if(Tab[i][j] != '.') ++counter;
		}
		if(counter == 16) ans = 2;
		else ans = 3;
	}
	printf("Case #%d: %s\n", zzz, Ans[ans]);
}

int main() {
	int ZZZ; scanf("%d", &ZZZ);
	FOR(zzz,0,ZZZ) testcase(zzz + 1);
	return 0;
}
