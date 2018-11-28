#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

char board[6][6];

char evaluate() {
	int o = 0, x = 0, t = 0;
	for (int i = 0; i < 4; ++i) {
		switch (board[i][i]) {
		case 'X':
			x++;
			break;
		case 'O':
			o++;
			break;
		case 'T':
			t++;
			break;
		default:
			break;
		}
	}
	if (x == 4 || (x == 3 && t == 1))
		return 'x';
	if (o == 4 || (o == 3 && t == 1))
		return 'o';
	o = 0, x = 0, t = 0;

	for (int i = 0; i < 4; ++i) {
		switch (board[3 - i][i]) {
		case 'X':
			x++;
			break;
		case 'O':
			o++;
			break;
		case 'T':
			t++;
			break;
		default:
			break;
		}
	}
	if (x == 4 || (x == 3 && t == 1))
		return 'x';
	if (o == 4 || (o == 3 && t == 1))
		return 'o';

	for (int i = 0; i < 4; ++i) {
		o = 0, x = 0, t = 0;
		for (int j = 0; j < 4; ++j) {
			switch (board[i][j]) {
			case 'X':
				x++;
				break;
			case 'O':
				o++;
				break;
			case 'T':
				t++;
				break;
			default:
				break;
			}
		}
		if (x == 4 || (x == 3 && t == 1))
			return 'x';
		if (o == 4 || (o == 3 && t == 1))
			return 'o';

		o = 0, x = 0, t = 0;
		for (int j = 0; j < 4; ++j) {
			switch (board[j][i]) {
			case 'X':
				x++;
				break;
			case 'O':
				o++;
				break;
			case 'T':
				t++;
				break;
			default:
				break;
			}
		}
		if (x == 4 || (x == 3 && t == 1))
			return 'x';
		if (o == 4 || (o == 3 && t == 1))
			return 'o';
	}
	return 'd';
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int dots = 0;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf(" %c ", &board[i][j]);
				dots += (board[i][j] == '.');
			}
		}
		char res = evaluate();
		switch (res) {
		case 'x':
			printf("Case #%i: X won\n", t + 1);
			break;
		case 'o':
			printf("Case #%i: O won\n", t + 1);
			break;
		case 'd': {
			if (dots)
				printf("Case #%i: Game has not completed\n", t + 1);
			else
				printf("Case #%i: Draw\n", t + 1);

		}
			break;
		}
	}
	return 0;
}
