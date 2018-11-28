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

char a[200][200];
int n;
ldb OWP[200];
ldb ans[200];


void Load()
{
	cin >> n;
	nextline();
	for (int i = 0; i < n; i++)
		gets (a[i]);
}

void Solve()
{
	
	for (int i = 0; i < n; i++)	
	{
		ldb cur = 0;
		ldb k = 0;
		ldb wn = 0;
		for (int j = 0; j < n; j++)
			if (a[i][j] != '.')
			{
				k++;
				if (a[i][j] == '1')
					wn++;
			}
		cur += 0.25 * (wn / k);

		ldb owp = 0;
		ldb ok = 0;
		for (int t = 0; t < n; t++)
			if (t != i && a[i][t] != '.')
			{
				k = 0;
				wn = 0;
				for (int j = 0; j < n; j++)		
					if (a[t][j] != '.' && j != i)
					{
						k++;
						if (a[t][j] == '1')
							wn++;
					}
			   owp += (wn / k);
			   ok++;
			}
	   	OWP[i] = owp / (ok);
		cur += 0.5 * OWP[i];
		ans[i] = cur;
	}

	for (int i = 0; i < n; i++)
	{
		ldb cur;
		cur = 0;
		ldb ok = 0;
		for (int j = 0; j < n; j++)
			if (a[i][j] != '.')
			{
				cur += OWP[j];
				ok++;
			}
		cout << ans[i] + 0.25 * cur / (ok) << "\n";
	}
}
                
int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
	cout.setf(ios::showpoint | ios ::fixed);
	cout.precision (10);
	int t, T;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ":\n";
		Load();
		Solve();
	}
	return 0;
	return 0;
}
