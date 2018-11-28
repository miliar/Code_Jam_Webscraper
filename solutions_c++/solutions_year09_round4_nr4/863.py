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

class points
{
public:
	ldb x, y, r;
};
vector <points> a;



void Load()
{
	cin >> n;
	points q;
	for (int i= 1; i <= n; i++)
	{
		cin >> q.x >> q.y >> q.r;
		a.push_back(q);
	}
		

}

ldb dist(points a, points b)
{
	return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}

void Solve()
{
	cout.setf(ios::showpoint|ios::fixed);
	cout.precision(10);
	if (n == 1)
	{
		cout << a[0].r;
		return;
	}
	if (n == 2)
	{
		cout << max(a[0].r, a[1].r);
		return;
	}

	vector <int> q;
	q.push_back(0);q.push_back(1);	q.push_back(2);
	ldb ans = inf, l;
	do
	{
		l = (dist(a[q[1]], a[q[2]]) + a[q[1]].r + a[q[2]].r) / 2.0;
		l = max(a[q[0]].r, l);
		ans = min(l, ans);
	} while (next_permutation(q.begin(), q.end()));
	cout << ans;
}
                
int main()
{
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);
	int T, tt;
	cin >> T;
	for (tt = 1; tt <= T; tt++)
	{
		a.clear();
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
		cout << "\n";
	}
	return 0;
}
