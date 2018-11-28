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
#define LL long long
#define nextline() {int c; while ((c = getchar()) != 10 && c != EOF);}

#define PI 3.1415926535897932384626433832795
#define EPS 1e-9

#define sqr(x) ((x) * (x))
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)

#define all(a) a.begin(), a.end()
#define two(i) (1 << (i))
#define has(mask, i) ((((mask) & two(i)) == 0) ? false : true)

const int INF = 1000 * 1000 * 1000;
const LL INF64 = 1000LL * 1000LL * 1000LL * 1000LL * 1000LL * 1000LL;


#define MAXN 1000

int n;
int a[2000];


void Load()
{
	scanf ("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf ("%d", &a[i]);
	}
}

void Solve()
{
	int sum = 0;
	int xr = 0;
	int mn = a[0];
	for (int i = 0; i < n; i++)
	{
		sum += a[i];
		xr ^= a[i];
		mn = min (mn, a[i]);
	}
	if (xr)
	{
		cout << "NO\n";
	}
	else
	{
		cout << sum - mn << "\n";
	}
}
                
int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int t, T;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		Load();
		Solve();
	}
	return 0;
	return 0;
}
