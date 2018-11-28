#pragma comment(linker, "/STACK:100000000")
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;
#define int64 long long
#define ldb long double
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define taskname "task_a"
const ldb pi = acos(-1.0);

char a[4][4];
int t;

bool win(char c) {
	for (int i = 0; i < 4; ++i) {
		bool good = true;
		for (int j = 0; j < 4; ++j)
			good &= (a[i][j] == c) || (a[i][j] == 'T');
		if (good)
			return true;
		good = true;
		for (int j = 0; j < 4; ++j)
			good &= (a[j][i] == c) || (a[j][i] == 'T');
		if (good)
			return true;
	}
	bool good = true;
	for (int j = 0; j < 4; ++j)
		good &= (a[j][j] == c) || (a[j][j] == 'T');
	if (good)
		return true;
	good = true;
	for (int j = 0; j < 4; ++j)
		good &= (a[j][4 - j - 1] == c) || (a[j][4 - j - 1] == 'T');
	return good;
}

int main() {
//	assert(freopen(taskname".in", "r", stdin));
//	assert(freopen(taskname".out", "w", stdout));
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		bool empty = false;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				scanf(" %c", &a[i][j]);
				empty |= (a[i][j] == '.');
			}
		printf("Case #%d: ", it + 1);
		if (win('X'))
			printf("X won\n");
		else if (win('O'))
			printf("O won\n");
		else if (empty)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}	
	return 0;
}