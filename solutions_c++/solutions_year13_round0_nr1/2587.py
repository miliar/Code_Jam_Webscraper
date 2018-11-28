#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(__typeof(S.begin()) it = S.begin(); it != S.end(); ++it)
#ifdef WIN32
	#define I64d "%I64d"
#else
	#define I64d "%lld"
#endif

typedef pair <int, int> pi;
char s[11][11];
int n = 4;

bool wins(char ch) {
	for (int i = 0; i < 4; ++i) {
		bool ok = true;
		for (int j = 0; j < 4; ++j) {
			if (s[i][j] != ch && s[i][j] != 'T') ok = false;
		}
		if (ok) return true;
	}
	for (int j = 0; j < 4; ++j) {
		bool ok = true;
		for (int i = 0; i < 4; ++i) {
			if (s[i][j] != ch && s[i][j] != 'T') ok = false;
		}
		if (ok) return true;
	}
	bool ok = true;
	for (int i = 0; i < 4; ++i) if (s[i][i] != ch && s[i][i] != 'T')
		ok = false;
	if (ok) return true;
	ok = true;
	for (int i = 0; i < 4; ++i) if (s[i][n - i - 1] != ch && s[i][n - i - 1] != 'T')
		ok = false;
	if (ok) return true;

	return false;
}

int main() {
	int tests;
	scanf("%d", &tests);	
	for (int casenum = 1; casenum <= tests; ++casenum) {
		bool full = true;
		for (int i = 0; i < n; ++i) {
			scanf("%s", &s[i]);
			for (int j = 0; j < n; ++j) if (s[i][j] == '.')
				full = false;
		}
		printf("Case #%d: ", casenum);
		if (wins('X')) puts("X won");
		else if (wins('O')) puts("O won");
		else if (full) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;		
}
