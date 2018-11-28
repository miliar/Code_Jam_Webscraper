#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
const int INF = 1 << 29;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
#ifdef WIN32
typedef __int64 ll;
#else
typedef long long ll;
#endif

/////////////////////////////////////////////////////////////////////////////////////////////////////////////// 

ifstream fin("input.in");
ofstream fout("output.out");
//FILE *fin  = fopen ("input.in", "r");
//FILE *fout = fopen ("output.out", "w");

const int MOD = 10007;
int board[147][147];

int dr[] = {1, 2};
int dc[]  ={2, 1};

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		int H, W, R;
		fin >> H >> W >> R;

		memset(board, 0, sizeof(board));
		FOR(i, 0, R)
		{
			int r, c;
			fin >> r >> c;
			board[r-1][c-1] = -1;
		}

		board[0][0] = 1;
		FOR(r, 0, H)
			FOR(c, 0, W)
				if (board[r][c] != -1)
				{
					FOR(d, 0, 2)
					{
						int rr = r + dr[d], cc = c + dc[d];
						if (rr < H && cc < W && board[rr][cc] != -1)
							board[rr][cc] = (board[rr][cc] + board[r][c]) % MOD;
					}
				}
		fout << "Case #" << step+1 << ": " << board[H-1][W-1] << endl;
	}

	return 0;
}
