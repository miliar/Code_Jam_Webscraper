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

const int ADD = 2*100000;

ldb pos[500];
ldb v[500];
int n, d;


void Load()
{
	int x, y;
	scanf ("%d%d", &n, &d);
	for (int i = 0; i < n; i++)
	{
		scanf ("%d%d", &x, &y)	;
		pos[i] = x;
		v[i] = y;

	//	cerr << pos[i] << " and " << v[i] << "\n" ;
	}
}

void Solve()
{
	ldb l = 0;
	ldb r = 1e15;
	ldb mid;

	cerr.setf(ios::showpoint | ios ::fixed);
	cerr.precision (10);

	for (int t = 0; t <= 300; t++)
	{
	//	cerr << l << " "<< r << "\n" ;
		mid = (l + r) / 2;
		ldb cur_pos;

		cur_pos = pos[0] - mid + (v[0] - 1) * d;
		ldb ans = fabs(cur_pos - pos[0]);

	//	cerr << "mid:" << mid << "\n";
	//	cerr << "cur_pos: " << cur_pos << "\n";

		for (int i = 1; i < n; i++)
		{
			if (pos[i] - mid < cur_pos + d + EPS)
			{
				cur_pos += v[i] * d;
			}
			else
			{
				cur_pos = pos[i] - mid + (v[i] - 1) * d;
			}
			ans = max (ans, fabs(cur_pos - pos[i]));
		//	cerr << cur_pos << "\n";
		}

	//	cerr << "ans: "<< ans << "\n";
	//	cerr << ans - mid << "\n";
		if (ans < mid + EPS || fabs (ans - mid) < EPS)
		{
			r = mid;
	//		cerr << "OK\n";
		}
		else
			l = mid;
	}
	cout << (l + r) / 2 << "\n";
}
                
int main()
{
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	cout.setf(ios::showpoint | ios ::fixed);
	cout.precision (10);
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
