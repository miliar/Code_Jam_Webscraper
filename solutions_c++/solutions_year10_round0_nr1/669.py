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

vector <bool> sn;
int n,k;

void Load()
{
	cin >> n >> k;
	sn.resize(n+1);
	for (int i = 0; i <= n; i++)
		sn[i] = 0;
}

void Solve()
{
	int i, fl = 1, j;
	if (n == 1)
	{
		if (k % 2 == 1)
			fl = 0;
	}
	else
	if (k > 1)
	{
		i = 1;
		for (j = 1; j <= n; j++)
			i *= 2;
		k -= (i - 1);
		if (k >= 0 && k % i == 0)
			fl = 0;
	}
	if (fl)
		cout << "OFF\n";
	else
		cout << "ON\n";

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
