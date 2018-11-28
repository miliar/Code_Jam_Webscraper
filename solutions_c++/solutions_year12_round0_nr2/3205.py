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

int n, m, p;
int a[200];

int dp[200][200];

void Load()
{
	scanf ("%d%d%d", &n, &m, &p);
	for (int i = 0; i < n; i++)
		scanf ("%d", &a[i]); 
}

int rec (int pos, int ost) {
 	if (pos == n)
 		return (ost == 0 ? 0 : -INF);
 	if (dp[pos][ost] != -1)
 		return dp[pos][ost];

 	int mx = 0;

 	if (ost > 0) {
 		for (int i1 = 0; i1 <= 10; i1++) {
 			int i2 = i1 + 2;
 			if (i1 + i2 > a[pos])
 				continue;
 			int i3 = a[pos] - i1 - i2;
 			if (i3 > 10 || i3 < i1 || i3 > i2)
 				continue;
			mx = max (mx, (i2 >= p ? 1 : 0) + rec (pos + 1, ost - 1));
		}

 	}

 	int b = -1;
 	for (int i1 = 0; i1 <= 10; i1++)
 		for (int i2 = i1; i2 <= 10; i2++)
 			for (int i3 = i2; i3 <= 10; i3++)
 				if (i1 + i2 + i3 == a[pos] && i3 - i1 < 2) {
					b = max (b, i3); 					
 				}

 	if (b != -1)
	 	mx = max (mx, (b >= p ? 1 : 0) + rec (pos + 1, ost));

 	dp[pos][ost] = mx;
	return mx;
}

void Solve()
{
	memset (dp, 0xFF, sizeof (dp));
	cout << rec (0, m) << "\n";
}
                
int main()
{
	//ios_base::sync_with_stdio(0);
#ifndef ONLINE_JUDGE
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
#endif
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		Load();
		printf ("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}
