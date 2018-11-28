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

int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};

vector<int> lines1[6047], lines2[6047];
bool visited[6047][6047];

int main()
{
	int T;
	fin >> T;

	FOR(step, 0, T)
	{
		int L;
		fin >> L;

		int x = 3002, y = 3002, d = 0;
		FOR(i, 0, 6047) { lines1[i].clear(); lines2[i].clear(); }
		FOR(i, 0, L)
		{
			string str;
			int num;
			fin >> str >> num;

			FOR(j, 0, num)
				FOR(k, 0, str.size())
				{
					if (str[k] == 'F')
					{
						if (d == 0 || d == 2)
							lines1[min(y, y+dy[d])].push_back(x);
						else
							lines2[min(x, x+dx[d])].push_back(y);
						x += dx[d];
						y += dy[d];
					}
					else if (str[k] == 'R')
						d = (d+1) % 4;
					else if (str[k] == 'L')
						d = (d+3) % 4;
				}
		}

		FOR(i, 0, 6047) FOR(j, 0, 6047) visited[i][j] = false;
		FOR(i, 0, 6047)
		{
			sort(lines1[i].begin(), lines1[i].end());
			for (int j = 2; j < lines1[i].size(); j += 2)
				FOR(k, lines1[i][j-1], lines1[i][j])
					visited[i][k] = true;
		}

		FOR(i, 0, 6047)
		{
			sort(lines2[i].begin(), lines2[i].end());
			for (int j = 2; j < lines2[i].size(); j += 2)
				FOR(k, lines2[i][j-1], lines2[i][j])
					visited[k][i] = true;
		}

		int res = 0;
		FOR(i, 0, 6047) FOR(j, 0, 6047) if (visited[i][j]) ++res;

		fout << "Case #" << step+1 << ": " << res << endl;
	}

	return 0;
}
