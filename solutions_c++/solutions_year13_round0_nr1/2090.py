//Seikang

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <stdlib.h>
#include <assert.h>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>

#include <cmath>
#include <complex>
#include <algorithm>

#include <ctime>
#define gtime clock()

using namespace std;

#define SZ(cont) (int)(cont.size())
#define ALL(cont) (cont).begin(), (cont).end()
#define DEBUG(x) cerr << ">" << #x << ":" << x << endl

typedef long long int64;
typedef pair<int64, int64> ii;
typedef vector<int64> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo32 = 1ll << 30, oo64 = 1ll << 60;
const double pi = acos(-1.0), eps = 1e-9;
inline bool equal(const double &a, const double &b){return abs(a - b) < eps;}

vs grid;
bool check(char c, char joker)
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(grid[i][j] != c && grid[i][j] != joker)
				break;
			if(j == 3)
				return true;
		}
	}

	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(grid[j][i] != c && grid[j][i] != joker)
				break;
			if(j == 3)
				return true;
		}
	}

	for(int i = 0; i < 4; i++)
	{
		if(grid[i][i] != c && grid[i][i] != joker)
			break;
		if(i == 3)
			return true;
	}

	for(int i = 0; i < 4; i++)
	{
		if(grid[i][3 - i] != c && grid[i][3 - i] != joker)
			break;
		if(i == 3)
			return true;
	}
	return false;
}
int main()
{
	//freopen ("in.txt", "rt", stdin);
	//freopen ("out.txt", "wt", stdout);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		cout << "Case #" << t + 1 << ": ";
		grid = vs(4);
		for(int i = 0; i < 4; i++)
		{
			cin >> grid[i];
		}
		if(check('X', 'T'))
		{
			cout << "X won" << endl;
			continue;
		}
		if(check('O', 'T'))
		{
			cout << "O won" << endl;
			continue;
		}
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(grid[i][j] == '.')
				{
					cout << "Game has not completed" << endl;
					goto ending;
				}
			}
		}
		cout << "Draw" << endl;
		ending:;
	}
	return 0;
}
