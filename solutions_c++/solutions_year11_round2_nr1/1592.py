#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

typedef vector<int> row;
typedef vector<row> board;
typedef vector<double> stats;

typedef struct { board b; stats wp, owp, oowp, rpi; int teams; } state; 

state getinput(int teams)
{
	char buffer;
	board b;
	for (int i = 0; i < teams; ++i)
	{
		row r;
		for (int j = 0; j < teams; ++j)
		{
			cin >> buffer;
			if (buffer == '.') r.push_back(0);
			else if (buffer == '0') r.push_back(-1);
			else r.push_back(1);
		}
		b.push_back(r);
	}
	state s;
	s.b = b;
	s.teams = teams;
	s.wp = vector<double>(teams);
	s.owp = vector<double>(teams);
	s.oowp = vector<double>(teams);
	s.rpi = vector<double>(teams);
	return s;
}

void getwp(state& s)
{
	for (int i = 0; i < s.teams; ++i)
	{
		double played = 0, won = 0;
		for (int j = 0; j < s.teams; ++j)
		{
			if (s.b[i][j] == 0) continue;
			played++;
			if (s.b[i][j] == -1) continue;
			won++;
		}
		s.wp[i] = won / played;
	}
}

void getowp(state& s)
{
	for (int i = 0; i < s.teams; ++i)
	{
		double owpsum = 0, op = 0;
		for (int j = 0; j < s.teams; ++j)
		{
			if (s.b[i][j] != 0)
			{
				op++;
				double played = 0, won = 0;
				for (int k = 0; k < s.teams; ++k)
				{
					if (k == i) continue;
					if (s.b[j][k] == 0) continue;
					played++;
					if (s.b[j][k] == -1) continue;
					won++;
				}
				owpsum += won / played;
			}
		}
		s.owp[i] = owpsum / op;
	}
}

void getoowp(state& s)
{
	for (int i = 0; i < s.teams; ++i)
	{
		double oowp = 0, op = 0;
		for (int j = 0; j < s.teams; ++j)
		{
			if (s.b[i][j] != 0)
			{
				op++;
				oowp += s.owp[j];
			}
		}
		s.oowp[i] = oowp / op;
	}
}

void getrpi(state& s)
{
	for (int i = 0; i < s.teams; ++i)
	{
		s.rpi[i] = s.wp[i] * 0.25 + 0.5 * s.owp[i] + s.oowp[i] * 0.25;
	}
}

void printres(int c, state& s)
{
	cout << "Case #" << c << ":" << endl;
	for (int i = 0; i < s.teams; ++i)
	{
		cout << s.rpi[i] << endl;
	}
}

void solve(int a)
{
	int teams;
	cin >> teams;
	state s = getinput(teams);
	getwp(s);
	getowp(s);
	getoowp(s);
	getrpi(s);
	printres(a, s);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int cases = 0;
	cin >> cases;
	for (int a = 1; a <= cases; ++a)
	{
		solve(a);
	}
	//system("pause");
}
