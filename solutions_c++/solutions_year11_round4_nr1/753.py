#include <iostream>
#include <string>
#include <algorithm>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
using namespace std;

#define N 1010
#define M 1000010

int length;      //total length to walk
int vwalk;      //walk speed
int vrun;       //run speed
double trun;       //max time to run
int n;          //number of acc

struct acc
{
	int start;
	int end;
	int speed;
	int speedup;
};


acc a[N];
bool v[M];


bool Cmp(acc u, acc v)
{
	return (1.0 / u.speed  - 1.0 / u.speedup) >  (1.0 / v.speed  - 1.0 / v.speedup);
}

int main()
{
	/*freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);*/

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int total;
	cin >> total;

	for (int test = 1; test <= total; ++test)
	{
		memset(v, false, sizeof(v));
		
		double ans = 0;
		cin >> length >> vwalk >> vrun >> trun >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i].start >> a[i].end >> a[i].speed;
			for (int x = a[i].start; x < a[i].end; ++x)
				v[x] = true;

			a[i].speedup = a[i].speed + vrun;
			a[i].speed = a[i].speed + vwalk;
		}

		int noacc = 0;
		for (int i = 0; i < length; ++i)
			if (!v[i])
				++noacc;

		a[n].start = 0;
		a[n].end = noacc;
		a[n].speed = vwalk;
		a[n].speedup = vrun;

		++n;

		sort(a, a + n, Cmp);

		for (int i = 0; i < n; ++i)
		{
			double t = ((double)(a[i].end - a[i].start)) / a[i].speedup;
			if (trun >= t)
			{
				ans += t;
				trun -= t;
			}
			else
			{
				ans += trun + (double)(a[i].end - a[i].start - trun * a[i].speedup) / a[i].speed;
				trun = 0;
			}
		}
		
		cout.precision(15);
		cout << "Case #" << test << ": "  << ans << endl;
		//cerr << "Case #" << test << " finished!" << endl;
	}
	return 0;
}