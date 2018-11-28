#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define maxl 510
#define ll long long
#define INF 0x3f3f3f3f

using namespace std;

char s[5][5];
int sum;

bool check(char ch) {
	int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
	for(int i=0; i<4; ++i) {
		c1 = c2 = 0;
		for(int j=0; j<4; ++j) {
			if(s[i][j] == ch || s[i][j] == 'T') c1++;
			if(s[j][i] == ch || s[j][i] == 'T') c2++;
		}
		if(c1 == 4 || c2 == 4) return 1;
		if(s[i][i] == ch || s[i][i] == 'T') c3++;
		if(s[i][3-i] == ch || s[i][3-i] == 'T') c4++;
	}
	if(c3 == 4 || c4 == 4) return 1;
	return 0;
}

void solve() {
	sum = 0;
	for(int i=0; i<4; ++i) for(int j=0; j<4; ++j) sum += (s[i][j] != '.');
	if(check('X')) puts("X won");
	else if(check('O')) puts("O won");
	else if(sum == 16) puts("Draw");
	else puts("Game has not completed");
}

int main() {
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		for(int i=0; i<4; ++i) scanf("%s", s[i]);
		printf("Case #%d: ", q);
		solve();
	}
	return 0;
}

