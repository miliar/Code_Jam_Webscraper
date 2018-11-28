#pragma comment(linker, "/STACK:256000000")
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <cassert>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)
#define ALL(a) a.begin(), a.end()
#define REP(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define SQR(a) ((a) * (a))

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;
typedef pair<int, int> pii ;
typedef vector<int> vint;
typedef vector<LL> vLL;

char b[10][10];

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	FOR(I, 1, T) {
		REP(i, 4)
			scanf("%s", b[i]);

		int r[4][2];
		int c[4][2];
		int d1[2], d2[2];
		MEM(r, 0);
		MEM(c, 0);
		MEM(d1, 0);
		MEM(d2, 0);
		int com = 0;
		REP(i, 4) {
			REP(j, 4) {
				com += b[i][j] != '.';
				if (b[i][j] == 'X' || b[i][j] == 'T') {
					r[i][0]++;
					c[j][0]++;
					d1[0] += i == j;
					d2[0] += i + j == 3;
				}
				if (b[i][j] == 'O' || b[i][j] == 'T') {
					r[i][1]++;
					c[j][1]++;
					d1[1] += i == j;
					d2[1] += i + j == 3;
				}
			}
		}
		bool w1 = (d1[0] == 4 || d2[0] == 4), w2 = (d1[1] == 4 || d2[1] == 4);
		REP(i, 4) {
			if (r[i][0] == 4 || c[i][0] == 4)
				w1 = true;
			if (r[i][1] == 4 || c[i][1] == 4)
				w2 = true;
		}
		string ans;
		if (w1) {
			assert(w2 == false);
			ans = "X won";
		}
		if (w2) {
			assert(w1 == false);
			ans = "O won";
		}
		if (!w1 && !w2) {
			ans = com == 16 ? "Draw" : "Game has not completed";
		}
		cout << "Case #" << I << ": " << ans << endl;
	}
	return 0;
}

