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
int a[1100];
int mark[1100];
int pr[1100];

void Load()
{
	scanf ("%d", &n);
	for (int i = 1; i <= n; i++)
		scanf ("%d", &a[i]);

}

void Solve()
{
	memset (mark, 0, sizeof (mark));
	int sum = 0;
	int m = 1;
	for (int i = 1; i <= n; i++)
		if (!mark[i])
		{
			int j = i;
			while (!mark[j])
			{
				mark[j] = m;
				j = a[j];
			}
			m++;
		}

	/*for (int i = 1; i <= n; i++)
		cerr << mark[i] << " ";
	cerr << "\n"	;*/

	for (int i = 1; i < m; i++)
		for (int j = 1; j <= n; j++)
			if (mark[j] == i)
			{
				int cnt = 0;
				int len = 0;
				int k = j;
				do
				{
					len++;
					k = a[k];
				} while (k != j);

				/*k = j;
				int x = a[k];
				while (k != x)
				{
					cnt++;
					k = a[k];
				}*/
				if (len > 1)
					sum += (len);

				break;
			}
	cout << sum << "\n";
}
                
int main()
{
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);
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
