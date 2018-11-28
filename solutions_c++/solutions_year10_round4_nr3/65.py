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
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 1000;
bool board[MAX][MAX];

void Solve(int tc)
{	
	memset(board, 0, sizeof(board));
	int R;
	cin >> R;
	FOR(step, 0, R)
	{
		int r1, c1, r2, c2;
		cin >> c1 >> r1 >> c2 >> r2;
		FOR(r, r1, r2+1)
			FOR(c, c1, c2+1)
				board[r][c] = true;
	}

	int alive = 1, res = 0;
	while (alive)
	{
		++res;
		alive = 0;
		FOR2(r, MAX-1, 0)
			FOR2(c, MAX-1, 0)
			{
				if ((r == MAX-1 || c == MAX-1) && board[r][c]) DEBUG("AAAAAAAA");
				if (board[r][c])
				{
					if (!board[r-1][c] && !board[r][c-1]) board[r][c] = false;
					else ++alive;
				}
				else
				{
					if (board[r-1][c] && board[r][c-1]) { board[r][c] = true; ++alive; }
				}
			}
	}
	cout << "Case #" << tc << ": " << res << endl;
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}