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
#include <string>

using namespace std;

#define ldb long double
#define lng long long
#define nextline {int c; while ((int c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-12

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int inf = 1000 * 1000 * 1000;
const lng inf64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

int n;
int a[50][50];
int deg[50];
int pos[50];

void Load()
{
	int i, j;
	string s;
	cin >> n;
	for (i = 1; i <= n; i++)
	{
		cin >> s;
		for (j = 1; j <= n; j++)
			a[i][j] = s[j - 1] - '0';
	}
}
int ans = inf;

void rec(int pos, int steps)
{
	int i, j, l;
    if (pos == n)
    {
    	int f = 1;
    	for (i = 1; i <= n; i++)	
    		for (j = i + 1; j <= n; j++)
    			if (a[i][j] == 1)
    			{
    				f = 0;
    				break;
    			}
    	if (f)
    		if (steps < ans)
    		{
    			ans = steps;
    		}
    	return;
    }
	
	int b[10][10];
	
	for (i = 1; i <= n; i++)
		for (j = 1; j <= n; j++)
			b[i][j] = a[i][j];

	rec(pos + 1, steps);
	for (i = pos + 1; i <= n; i++)
	{
		int x = steps;
		for (l = i; l > pos; l--)
		{                	
			x++;
			for (j = 1; j <= n; j++)	
				swap(a[l][j], a[l-1][j]);
		}
		rec(pos + 1, x);
		for (l = 1; l <= n; l++)
			for (j = 1; j <= n; j++)
				a[l][j] = b[l][j];
	}
}

void Solve()
{
	ans = inf;
    rec(1, 0);
	cout << ans;
}
                
int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	int T, tt;
	cin >> T;
	for (tt = 1; tt <= T; tt++)
	{
		memset(a, 0, sizeof(a));
		memset(deg, 0, sizeof(deg));
		memset(pos, 0xFF, sizeof(pos));
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
		cout << "\n";
	}
	return 0;
}
