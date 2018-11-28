#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define REP(i, s, e) for (int i = (s); i < (e); i++)
#define REPI(i, s, e) for (int i = (s); i <= (e); i++)
#define rep(i, n) REP(i, 0, n)
#define repi(i, n) REPI(i, 0, n)
#define ALL(v) (v).begin(), (v).end()

typedef long long ll;

char brd[4][4];
int dx[] = { 1, 1,  0, -1 };
int dy[] = { 0, 1,  1,  1 };

bool won(char ch, int y, int x, int d)
{
	rep(i, 4) {
		int ny = y+i*dy[d];
		int nx = x+i*dx[d];

		if (!(0 <= ny && ny < 4)) return false;
		if (!(0 <= nx && nx < 4)) return false;
		if (!(brd[ny][nx] == ch || brd[ny][nx] == 'T')) return false;
	}
	return true;
}

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		char *str;

		rep(j, 4)
			rep(i, 4)
				cin >> brd[j][i];

		bool dot = false;
		rep(j, 4) {
			rep(i, 4) {
				if (brd[j][i] == '.') {
					dot = true;
					continue;
				}
				rep(k, 4) {
					if (won('X', j, i, k)) {
						str = (char*)"X won";
						goto END;
					} else if (won('O', j, i, k)) {
						str = (char*)"O won";
						goto END;
					}
				}
			}
		}
		if (dot)
			str = (char*)"Game has not completed";
		else
			str = (char*)"Draw";
END:
		printf("Case #%d: %s\n", t+1, str);
	}
	return 0;
}
