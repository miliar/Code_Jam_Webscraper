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
/*
class 
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

ifstream fin("vstup.txt");
ofstream fout("vystup.txt");

//FILE * fin = fopen("vstup.txt", "r");
//FILE * fout = fopen("vystup.txt", "w");

const int dc[] = {-1, 1};

int R, C, F;
string input[57];

inline bool check(int r, int c) { return r >= 0 && r < R && c >= 0 && c < C; }

const int NO = 1<<6;

struct State
{
	State(): digs(0), d1(NO), d2(NO) { }

	int r, c, digs;
	int d1, d2;

	bool operator<(const State & st) { return digs < st.digs; }
};

bool visited[50][50][(1<<6)+1][(1<<6)+1];

inline bool visit(State & st) 
{
	bool res = visited[st.r][st.c][st.d1][st.d2];
	visited[st.r][st.c][st.d1][st.d2] = true;
	return res;
}

inline bool dug(const State & st, int r, int c)
{
	if (r == st.r)
		return test(st.d1, c);
	else
		return test(st.d2, c);
}

void Solve(int tc)
{
	//nacita vstup
	fin >> R >> C >> F;
	FOR(i, 0, R) fin >> input[i];

	memset(visited, 0, sizeof(visited));

	State temp;
	temp.r = 0;
	temp.c = 0;
	
	queue<State> manage[2];
	int act = 0;
	manage[act].push(temp);

	int result = -1;
	while (result == -1 && !manage[act].empty())
	{
		while (!manage[act].empty())
		{
			temp = manage[act].front();
			manage[act].pop();

			if (temp.r == R-1)
			{
				result = temp.digs;
				break;
			}
			if (visit(temp))
				continue;

			//pohne sa do bokov
			FOR(d, 0, 2)
			{
				State temp2 = temp;
				temp2.c = temp.c + dc[d];
				if (!check(temp2.r, temp2.c) || (input[temp2.r][temp2.c] == '#' && !dug(temp2, temp2.r, temp2.c)))
					continue;
				//spadne
				int jump = 0;
				while (check(temp2.r+1, temp2.c) && (input[temp2.r+1][temp2.c] == '.' || dug(temp2, temp2.r+1, temp2.c)))
				{
					++jump;
					++temp2.r;
					
					temp2.d1 = temp2.d2;
					temp2.d2 = NO;
				}
				if (jump <= F)
					manage[act].push(temp2);
			}

			//zacne kopat do bokov
			FOR(d, 0, 2)
			{
				State temp2 = temp;

				int digc = temp2.c + dc[d];
				if (!check(temp2.r+1, digc) || input[temp2.r+1][digc] != '#' || (input[temp2.r][digc] == '#' && !dug(temp2, temp2.r, digc)))
					continue;

				++temp2.digs;
				set_bit(temp2.d2, digc);
				manage[1-act].push(temp2);
			}
		}

		act = 1-act;
	}


	//fout << F << endl;
	//FOR(i, 0, R) fout << input[i] << endl;
	fout << "Case #" << tc << ": ";
	if (result == -1)
		fout << "No" << endl;
	else
		fout << "Yes " << result << endl;
	//fout << endl;
}

int main()
{
	int T;
	fin >> T;
	FOR(step, 0, T)
		Solve(step+1);

	return 0;
}