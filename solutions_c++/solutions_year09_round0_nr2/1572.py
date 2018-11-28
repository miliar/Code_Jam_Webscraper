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

/*class 
{
private:
	
public:
	
};*/

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

ifstream fin("B-large.in");
ofstream fout("vystup.txt");

int R, C;

int input[147][147];
char output[147][147];

int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

bool check(int r, int c) { return r >= 0 && r < R && c >= 0 && c < C; }
char mark;
char get(int r, int c)
{
	if (output[r][c]) return output[r][c];

	int best = input[r][c], next = -1;
	FOR(d, 0, 4)
	{
		int rr = r+dr[d], cc = c+dc[d];
		if (check(rr, cc) && input[rr][cc] < best)
		{
			best = input[rr][cc];
			next = d;
		}
	}

	if (next == -1)
		output[r][c] = mark++;
	else
		output[r][c] = get(r+dr[next], c+dc[next]);

	return output[r][c];
}

int main()
{
	int T;

	fin >> T;
	FOR(step, 0, T)
	{
		fin >> R >> C;
		FOR(i, 0, R)
			FOR(j, 0, C) 
			{
				fin >> input[i][j];
				output[i][j] = 0;
			}

		mark = 'a';
		fout << "Case #" << step+1 << ":" << endl;
		FOR(i, 0, R)
		{
			FOR(j, 0, C)
			{
				if (j) fout << " ";
				fout << get(i, j);
			}
			fout << endl;
		}
	}

	return 0;
}
