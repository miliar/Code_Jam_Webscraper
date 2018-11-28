#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
#include <complex>
#include <list>

using namespace std;
 
void ASS(bool b)
{
    if (!b)
    {
        ++*(int*)0;
    }
}
 
#define FOR(i, x) for (int i = 0; i < (int)(x); ++i)
#define CL(x) memset(x, 0, sizeof(x))
#define CLX(x, y) memset(x, y, sizeof(x))
 
#pragma comment(linker, "/STACK:106777216")
 
typedef vector<int> vi;

typedef unsigned long long LL;

char a[16][16];

bool Win(char c) {
	bool ok = 1;
	FOR(i, 4) {
		ok = 1;
		FOR(j, 4)
			ok = ok && (a[i][j] == c || a[i][j] == 'T');
		if (ok)
			return 1;
	}
	FOR(i, 4) {
		ok = 1;
		FOR(j, 4)
			ok = ok && (a[j][i] == c || a[j][i] == 'T');
		if (ok)
			return 1;
	}
	ok = 1;
	FOR(i, 4)
		ok = ok && (a[i][i] == c || a[i][i] == 'T');
	if (ok)
		return 1;
	ok = 1;
	FOR(i, 4)
		ok = ok && (a[i][3 - i] == c || a[i][3 - i] == 'T');
	if (ok)
		return 1;
	return 0;
}

void Solve() {
	FOR(i, 4)
		cin >> a[i];
	if (Win('X')) {
		cout << "X won";
		return;
	}
	if (Win('O')) {
		cout << "O won";
		return;
	}
	int cnt = 0;
	FOR(i, 4)
		FOR(j, 4)
			cnt += a[i][j] == '.';
	if (cnt == 0)
		cout << "Draw";
	else
		cout << "Game has not completed";
}

int main()
{
	freopen("c://my//in.txt", "r", stdin);
	freopen("c://my//out.txt", "w", stdout);

	int T;
	cin >> T;

	FOR(i, T) {
		cout << "Case #" << (i + 1) << ": ";
		Solve();
		cout << "\n";
	}

	return 0;
}
