//#pragma comment(linker,"/STACK:256000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <ctime>
#include <cassert>
#include <stdio.h>
#include <string>
#include <memory.h>

using namespace std;

#define ldb long double
#define lng long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int inf = 1000 * 1000 * 1000;
const lng inf64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

int dx[8] = {0, 0, 1, 1, 1, -1, -1, -1};
int dy[8] = {1, -1, -1, 0, 1, -1, 0, 1};

string a[60];
string b[60];
int n, k;

void Load()
{
	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
		b[i] = a[i];
	}
}

void Solve()
{
	int i, j, l;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
			b[j][n - 1 - i] = a[i][j];

/*	for (i = 0; i < n; i++)
		cerr << b[i] << "\n";
	cerr << "->\n";              */

	for (j = 0; j < n; j++)
	{
		for (i = 0; i < n; i++)
			for (l = n - 2; l >= 0; l--)
				if (b[l][j] != '.' && b[l + 1][j] == '.')
					swap (b[l][j], b[l + 1][j]);
	}

/*	for (i = 0; i < n; i++)
		cerr << b[i] << "\n";
	cerr << "----------------\n";*/
	
	int fl[4] = {0,0,0,0};
	for (j = 0; j < n; j++)
		for (i = n - 1; i >= 0; i--)
		for (int q = 0; q < 8; q++)
		{
			int y = j;
			int x = i;
			int k1, k2;
			k1 = k2 = 0;
			for (l = 0; l < k; l++)
			{
				if (x >= 0 && y >= 0 && x < n && y < n)
					if (b[x][y] == 'B')
						k1++;
					else
						if (b[x][y] == 'R')
							k2 ++;
				x += dx[q];
				y += dy[q]; 
			}
			if (k1 == k)
				fl[1] = 1;
			if (k2 == k)
				fl[2] = 1;
			if (k1 != k && k2 != k)
				fl[0] = 1;
		}
	if (fl[1] == 1 && fl[2] == 1)
		cout << "Both\n";
	else
		if (fl[1] == 1)
			cout << "Blue\n";
		else
			if (fl[2] == 1)
				cout << "Red\n";
			else
				cout << "Neither\n";
}
                
int main()
{
	//ios_base::sync_with_stdio(0);
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int t, T;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		Load();
		Solve();
	}
	return 0;
}
