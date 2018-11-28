#include <algorithm>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)

string grid[4];

const string xwin = "X won";
const string owin = "O won";
const string draw = "Draw";
const string incomplete = "Game has not completed";

bool won(char p)
{
	FOR(r,0,4) {
		int cnt = 0;
		FOR(c,0,4) if (grid[r][c] == p || grid[r][c] == 'T') ++cnt;
		if (cnt == 4) return true;
	}
	FOR(c,0,4) {
		int cnt = 0;
		FOR(r,0,4) if (grid[r][c] == p || grid[r][c] == 'T') ++cnt;
		if (cnt == 4) return true;
	}
	{
		int cnt = 0;
		FOR(i,0,4) if (grid[i][i] == p || grid[i][i] == 'T') ++cnt;
		if (cnt == 4) return true;
	}
	{
		int cnt = 0;
		FOR(i,0,4) if (grid[3-i][i] == p || grid[3-i][i] == 'T') ++cnt;
		if (cnt == 4) return true;
	}
	return false;
}

int main() 
{
	int TC; cin >> TC;
	FOR(tc,1,TC+1) {
		FOR(i,0,4) cin >> grid[i];

		string result = draw;
		FOR(r,0,4) FOR(c,0,4) if (grid[r][c] == '.') {
			result = incomplete;
			break;
		}

		if (won('X')) result = xwin;
		if (won('O')) result = owin;

		printf("Case #%d: %s\n", tc, result.c_str());
	}
}
