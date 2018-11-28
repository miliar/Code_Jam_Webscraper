/**											Be name Khoda											**/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <bitset>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <memory.h>
using namespace std;

#define ll long long
#define un unsigned
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define VAL(x) #x << " = " << x << "   "
#define SQR(a) ((a) * (a))
#define SZ(x) ((int) x.size())
#define ALL(x) x.begin(), x.end()
#define CLR(x, a) memset(x, a, sizeof x)
#define FOREACH(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define X first
#define Y second
#define SAL cerr << "Salam!\n"
#define PI (3.141592654)

//#define cout fout
//#define cin fin

//ifstream fin("problem.in");
//ofstream fout("problem.out");

const int MAXN = 1000 * 1 + 10, INF = 1e9 + 10;

int n = 4;
char a[10][10];

bool check(char c)
{
	for (int i = 0; i < n; i ++)
	{
		int cnt = 0;
		for (int j = 0; j < n; j ++)
			if (a[i][j] == c || a[i][j] == 'T')
				cnt ++;
		if (cnt == 4)
			return true;
	}
	for (int i = 0; i < n; i ++)
	{
		int cnt = 0;
		for (int j = 0; j < n; j ++)
			if (a[j][i] == c || a[j][i] == 'T')
				cnt ++;
		if (cnt == 4)
			return true;
	}
	int cnt = 0;
	for (int i = 0; i < n; i ++)
		if (a[i][i] == c || a[i][i] == 'T')
			cnt ++;
	if (cnt == 4) 
		return true;

	cnt = 0;
	for (int i = 0; i < n; i ++)
		if (a[i][n - i - 1] == c || a[i][n - i - 1] == 'T')
			cnt ++;
	if (cnt == 4) 
		return true;
	return false;
}

int main ()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc ++)
	{
		bool end = true;
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < n; j ++)
			{
				cin >> a[i][j];
				if (a[i][j] == '.')
					end = false;
			}
		cout << "Case #" << tc << ": ";
		if (check('X'))
			cout << "X won\n";
		else if (check('O'))
			cout << "O won\n";
		else if (!end)
			cout << "Game has not completed\n";
		else cout << "Draw\n";
	}
	return 0;
}

