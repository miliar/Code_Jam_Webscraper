/*
 * A.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Mostafa Saad
 */

#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<numeric>
#include<utility>
#include <functional>
#include<stdio.h>
#include<assert.h>
#include<memory.h>
using namespace std;

#define all(v)				((v).begin()), ((v).end())
#define sz(v)				((int)((v).size()))
#define clr(v, d)			memset(v, d, sizeof(v))
#define rep(i, v)		for(int i=0;i<sz(v);++i)
#define lp(i, n)		for(int i=0;i<(int)(n);++i)
#define lpi(i, j, n)	for(int i=(j);i<(int)(n);++i)
#define lpd(i, j, n)	for(int i=(j);i>=(int)(n);--i)


bool win(vector<string> &v, char c) {
	rep(i, v) {
		bool ok = 1;
		rep(j, v)
			ok &= (v[i][j] == c || v[i][j] == 'T');
		if (ok)
			return 1;
	}

	rep(j, v) {
		bool ok = 1;
		rep(i, v)
			ok &= (v[i][j] == c || v[i][j] == 'T');
		if (ok)
			return 1;
	}

	bool ok = 1;
	rep(i, v)
		ok &= (v[i][i] == c || v[i][i] == 'T');

	if (ok)
		return 1;

	ok = 1;
	rep(i, v)
		ok &= (v[i][sz(v)-i-1] == c || v[i][sz(v)-i-1] == 'T');

	if (ok)
		return 1;

	return 0;
}

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out.txt", "wt", stdout);

	int cases;
	cin >> cases;

	lp(cc, cases) {
		vector<string> v(4);
		bool dot = false;
		rep(i, v) {
			cin >> v[i];
			dot |= (int) v[i].find('.') != -1;
		}

		printf("Case #%d: ", cc + 1);

		if (win(v, 'X'))
			printf("X won");
		else if (win(v, 'O'))
			printf("O won");
		else if (dot)
			printf("Game has not completed");
		else
			printf("Draw");

		printf("\n");
	}

	return 0;
}
