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

const int MAX = 500;
int input[MAX][MAX];
int board[MAX][MAX];

//line - [1, 2*K-1]
inline int lineLen(int K, int line) { return min(line, 2*K-line); }

int getSize(int K)
{
	int res = 0;
	FOR(i, 0, 2*K-1) res += lineLen(K, i+1);
	return res;
}

bool check(int K, int KK, int r, int c)
{
	memset(board, -1, sizeof(board));
	FOR(i, 0, 2*K-1)
	{
		FOR(j, 0, lineLen(K, i+1))
		{
			board[r][c+j] = input[i][j];
		}
		++r;
		if (r < KK && i+1 >= K)
			++c;
		else if (r >= KK && i+1 < K)
			--c;
	}

	FOR(i, 0, 2*KK-1)
		FOR(j, 0, lineLen(KK, i+1))
		{
			//horizontal
			int a = board[i][j], b = board[i][lineLen(KK, i+1)-1-j];
			if (a != -1 && b != -1 && a != b) return false;
			//vertical
			b = board[2*KK-1-1-i][j];
			if (a != -1 && b != -1 && a != b) return false;
		}
	return true;
}

bool check2(int K, int KK, int r, int c)
{
	memset(board, -1, sizeof(board));
	FOR(i, 0, 2*K-1)
	{
		FOR(j, 0, lineLen(K, i+1))
		{
			board[r][c+j] = input[2*K-1-1-i][j];
		}
		++r;
		if (r < KK && i+1 >= K)
			++c;
		else if (r >= KK && i+1 < K)
			--c;
	}

	FOR(i, 0, 2*KK-1)
		FOR(j, 0, lineLen(KK, i+1))
		{
			//horizontal
			int a = board[i][j], b = board[i][lineLen(KK, i+1)-1-j];
			if (a != -1 && b != -1 && a != b) return false;
			//vertical
			b = board[2*KK-1-1-i][j];
			if (a != -1 && b != -1 && a != b) return false;
		}
	return true;
}

void Solve(int tc)
{	
	int K;
	cin >> K;
	FOR(i, 0, 2*K-1)
		FOR(j, 0, lineLen(K, i+1))
			cin >> input[i][j];

	int KK = K, res;
	while (1)
	{
		FOR(r, 0, KK-K+1)
			FOR(c, 0, lineLen(KK, r+1))
			{
				if (check(K, KK, r, c) || check2(K, KK, r, c))
				{
					res = getSize(KK) - getSize(K);
					goto found;
				}
			}
		++KK;
	}
found:
	cout << "Case #" << tc << ": " << res << endl;
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}