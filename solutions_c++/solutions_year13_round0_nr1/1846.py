#include <list>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ext/hash_map>
#include <stdint.h>
#include <ctime>
#include <queue>
#include <sstream>
#include <sys/time.h>
#include <fstream>
#include <vector>

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned char BYTE;

#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define FORU(i, s, e) for (int i = (s); i <= (e); ++i)
#define FORD(i, s, e) for (int i = (s); i >= (e); --i)
#define ALL(x) x.begin(),x.end()
#define FOREACH(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define SIZE(x) ((int)x.size())
#define MP make_pair
#define PB push_back
#define BIT(x, b) (((x) >> (b)) & 1)
#define SWAP(a, b, t) do {t = a; a = b; b = t;} while (0);
#define INF 1000000000
#define EPS 1e-9
#define TIME_LEFT_UNTIL(end) ((curTime=getTime()-startTime) < (end))
#define TIME_LEFT() TIME_LEFT_UNTIL(MAX_TIME)
#define INIT_TIME() startTime = getTime()

inline double getTime () {
   timeval tv;
   gettimeofday(&tv, 0);
   return tv.tv_sec + tv.tv_usec * 1e-6;
}


char board[4][4];

int main () {
	int T;
	scanf("%d", &T);
	FOR(itr, T) {
		FOR(i, 4)
			FOR(j, 4)
				scanf(" %c", &board[i][j]);

		string out = "Draw";
		FOR(i, 4) {
			int cntX = 0, cntT = 0, cntO = 0;
			FOR(j, 4) {
				if (board[i][j] == 'X')
					++cntX;
				else if (board[i][j] == 'O')
					++cntO;
				else if (board[i][j] == 'T')
					++cntT;
			}
			if (cntT <= 1) {
				if (cntX+cntT == 4) {
					out = "X won";
					break;
				}
				else if (cntO+cntT == 4) {
					out = "O won";
					break;
				}
			}
			if (cntX+cntO+cntT < 4)
				out = "Game has not completed";
		}
		FOR(j, 4) {
			int cntX = 0, cntT = 0, cntO = 0;
			FOR(i, 4) {
				if (board[i][j] == 'X')
					++cntX;
				else if (board[i][j] == 'O')
					++cntO;
				else if (board[i][j] == 'T')
					++cntT;
			}
			if (cntT <= 1) {
				if (cntX+cntT == 4) {
					out = "X won";
					break;
				}
				else if (cntO+cntT == 4) {
					out = "O won";
					break;
				}
			}
		}
		int cntX = 0, cntT = 0, cntO = 0;
		FOR(i, 4) {
			if (board[i][i] == 'X')
				++cntX;
			else if (board[i][i] == 'O')
				++cntO;
			else if (board[i][i] == 'T')
				++cntT;
		}
		if (cntT <= 1) {
			if (cntX+cntT == 4)
				out = "X won";
			else if (cntO+cntT == 4)
				out = "O won";
		}
		cntX = 0; cntT = 0; cntO = 0;
		FOR(i, 4) {
			if (board[i][3-i] == 'X')
				++cntX;
			else if (board[i][3-i] == 'O')
				++cntO;
			else if (board[i][3-i] == 'T')
				++cntT;
		}
		if (cntT <= 1) {
			if (cntX+cntT == 4)
				out = "X won";
			else if (cntO+cntT == 4)
				out = "O won";
		}

		printf("Case #%d: %s\n", itr+1, out.c_str());
	}
}
