/*
 * TicTacTo
 * Apr 13, 2013,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include <climits>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)
#define MOD(a,b) ((((a)%(b))+(b))%(b))
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0.0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { 0, 1, 1, 1 };
int DJ[] = { 1, 0, 1, -1 };

string g[4];

bool win(char x) {
	loop(i,4)
		loop(j,4)
			if (g[i][j] == x || g[i][j] == 'T') {
				loop(k,4)
				{
					int c = 1;
					for (int s = 1; s <= 3; s++) {
						int ni = i + DI[k] * s, nj = j + DJ[k] * s;
						if (ni >= 4 || nj >= 4 || ni < 0 || nj < 0)
							continue;
						if (g[ni][nj] == x || g[ni][nj] == 'T')
							c++;
					}
					if (c == 4)
						return true;
				}
			}
	return false;
}
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	cin >> t;

	loop2(id,1,t+1)
	{
		int dot = 0;

		loop(i,4)
		cin >> g[i];

		loop(i,4)
		loop(j,4)
		if (g[i][j] == '.')
		dot++;

		cout << "Case #" << id << ": ";
		if (win('X'))
		cout << "X won";
		else if (win('O'))
		cout << "O won";

		else if (dot == 0)
		cout << "Draw";

		else if (dot != 0)
		cout << "Game has not completed";

		cout << endl;

	}
	return 0;
}
