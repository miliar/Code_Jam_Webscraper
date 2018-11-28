#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <complex>
#include <map>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <queue>
#include <cmath>
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");
const double EPS = 1e-10;

int R, C;
vector< vector<int> > res;
vector<string> m;
queue<pair<int, int> > q;

bool iswall(int x, int y)
{
	return (m[x][y]=='#');
}

pair<int, int> getwall(int x, int y, int dx, int dy)
{
	while (!iswall(x, y)) { x+=dx; y+=dy; }
	return pair<int, int>(x-dx, y-dy);
}

void move_to(pair<int, int> p, int v)
{
	if (iswall(p.first, p.second)) return;
	if (res[p.first][p.second] != -1) return;
	q.push(p);
	res[p.first][p.second] = v;
}


int main(void)
{
	int number_of_tests;
	fin >> number_of_tests;
	for (int test_case = 1; test_case <= number_of_tests; test_case++)
	{
		fin >> R >> C;
		m.clear();
		res.clear();
		m.resize(R+2, string(C+2, '#'));
		for (int i = 1; i <= R; i++)
		{
			string str;
			fin >> str;
			m[i] = "#"+str+"#";
		}
		res.resize(R+2, vector<int>(C+2, -1));
		for (int i = 1; i <= R; i++)
		{
			for (int j = 1; j <= C; j++)
			{
				if (m[i][j] == 'O') move_to(pair<int, int>(i, j), 0);
			}
		}
		while (!q.empty())
		{
			pair<int, int> p = q.front();
			q.pop();
			int x = p.first; int y = p.second;
			int v = res[x][y] + 1;
			move_to(pair<int, int>(x+1, y), v);
			move_to(pair<int, int>(x-1, y), v);
			move_to(pair<int, int>(x, y+1), v);
			move_to(pair<int, int>(x, y-1), v);
			if ((iswall(x+1, y))||(iswall(x-1, y))||(iswall(x, y+1))||(iswall(x, y-1)))
			{
				move_to(getwall(x, y, 1, 0), v);
				move_to(getwall(x, y, -1, 0), v);
				move_to(getwall(x, y, 0, 1), v);
				move_to(getwall(x, y, 0, -1), v);
			}
		}
		fout << "Case #" << test_case << ": ";
		for (int i = 1; i <= R; i++)
		{
			for (int j = 1; j <= C; j++)
			{
				if (m[i][j] == 'X')
				{
					if (res[i][j] == -1) fout << "THE CAKE IS A LIE"; else fout << res[i][j];
				}
			}
		}
		fout << endl;
	}
	return 0;
}
