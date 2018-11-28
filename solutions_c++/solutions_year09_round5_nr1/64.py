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

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

//FILE * fin = fopen("vstup.txt", "r");
//FILE * fout = fopen("vystup.txt", "w");

ifstream fin("vstup.txt");
ofstream fout("vystup.txt");

const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};

int R, C;
string board[12];

inline bool check(int r, int c) { return r >= 0 && r < R && c >= 0 && c < C; }

int boxes[12][12];

void dfs(int r, int c)
{
	boxes[r][c] = -1;
	FOR(d, 0, 4)
	{
		int rr = r+dr[d], cc = c+dc[d];
		if (check(rr, cc) && boxes[rr][cc] == 1)
			dfs(rr, cc);
	}
}

bool connected(const vector<int> & pos)
{
	FOR(i, 0, pos.size())
		boxes[pos[i]/C][pos[i]%C] = 1;

	dfs(pos[0]/C, pos[0]%C);

	bool res = true;
	FOR(i, 0, pos.size())
	{
		if (boxes[pos[i]/C][pos[i]%C] == 1) res = false;
		boxes[pos[i]/C][pos[i]%C] = 0;
	}
	return res;
}

bool can_move(int r, int c, int dir)
{
	int r1 = r+dr[dir], c1 = c+dc[dir];
	int r2 = r-dr[dir], c2 = c-dc[dir];
	return check(r1, c1) && board[r1][c1] == '.' && check(r2, c2) && board[r2][c2] == '.';
}

void Solve(int tc)
{
	//nacita vstup
	fin >> R >> C;
	FOR(i, 0, R) fin >> board[i];

	//nacita suradnice krabic a koncow
	vector<int> start, final;
	FOR(i, 0, R)
		FOR(j, 0, C)
		{
			if (board[i][j] == 'x')
				final.push_back(i*C+j);
			else if (board[i][j] == 'o')
				start.push_back(i*C+j);
			else if (board[i][j] == 'w')
			{
				final.push_back(i*C+j);
				start.push_back(i*C+j);
			}

			if (board[i][j] != '#')
				board[i][j] = '.';
		}
	
	//spusti bfs-ko
	set<vector<int> > visited;
	queue<pair<vector<int>, int> > manage;
	manage.push(make_pair(start, 0));

	int result = -1;
	if (start == final)
		result = 0;
	while (!manage.empty() && result == -1)
	{
		vector<int> pos = manage.front().first;
		int steps = manage.front().second;
		manage.pop();

		//rozhodi skatule po ploche
		FOR(i, 0, pos.size())
			board[pos[i]/C][pos[i]%C] = 'o';
		//kazdu skatulu posunie nejakym smerom
		FOR(i, 0, pos.size())
			FOR(d, 0, 4)
				if (can_move(pos[i]/C, pos[i]%C, d))
				{
					vector<int> next = pos;
					next[i] += dr[d]*C+dc[d];

					bool con = connected(next);
					if (steps < 0 && !con) continue; //nebol spojeny a uz je

					sort(next.begin(), next.end());
					if (con && next == final)
					{
						result = abs(steps)+1;
						goto found;
					}

					set<vector<int> >::iterator iter = visited.find(next);
					if (iter != visited.end()) continue;
					visited.insert(next);

					manage.push(make_pair(next, (abs(steps)+1)*(con?1:-1)));
				}
		FOR(i, 0, pos.size())
			board[pos[i]/C][pos[i]%C] = '.';
	}
found:
	fout << "Case #" << tc << ": " << result << endl;
}

int main()
{
	int T;
	fin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}