#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <memory.h>
#include <cmath>

using namespace std;

#define fr(i,a,b) for(int i = (a); i <= (b); ++i)
#define frR(i,a,b) for(int i = (a); i >= (b); --i)
#define fi(a) for(int i = (0); i < (a); ++i)
#define fj(a) for(int j = (0); j < (a); ++j)
#define fk(a) for(int k = (0); k < (a); ++k)
#define CLR(a, b) memset((a), (b), sizeof((a)))
#define clr(a) CLR((a), 0)
#define pb push_back
#define mkp make_pair
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 5000;
const int inf = 1000000000 + 7;
const double eps = 1e-5;

struct tpnt
{
	double x, y;
	tpnt(double X = 0, double Y = 0)
	{
		x = X;
		y = Y;
	}
};

tpnt operator+(tpnt p1, tpnt p2)
{
	return (tpnt(p1.x + p2.x, p1.y + p2.y));
}

tpnt operator/(tpnt p, double val)
{
	return (tpnt(p.x / val, p.y / val));
}

int n;
tpnt c[100];
int r[100];

double dist(tpnt p1, tpnt p2)
{
	return (hypot(p1.x - p2.x, p1.y - p2.y));
}

void solve()
{
	cin >> n;
	fi(n)
		cin >> c[i].x >> c[i].y >> r[i];

	if (n == 1)
		printf("%.5lf\n", 1. * r[0]);
	if (n == 2)
		printf("%.5lf\n", 1. * max(r[0], r[1]));
	if (n == 3)
	{
		double best = 1e10;
		fi(3)
		{			
			double cur = dist(c[(i + 1) % n], c[(i + 2) % n]) + r[(i + 1) % n] + r[(i + 2) % n];
			cur /= 2.0;
			tpnt p = (c[(i + 1) % n] + c[(i + 2) % n]) / 2.0;
			if (dist(c[i], p) + r[i] > cur)
				cur = max(cur, (double)r[i]);
			if (best > cur)
				best = cur;				
		}
		printf("%.5lf\n", best);
	}
}

void initf()
{
	freopen("in.txt", "r",  stdin);
	freopen("out.txt", "w",  stdout);
}

int main()
{
	//initf();
	int t;
	scanf("%d", &t);
	fi(t)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return (0);
}#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <memory.h>

using namespace std;

#define fr(i,a,b) for(int i = (a); i <= (b); ++i)
#define frR(i,a,b) for(int i = (a); i >= (b); --i)
#define fi(a) for(int i = (0); i < (a); ++i)
#define fj(a) for(int j = (0); j < (a); ++j)
#define fk(a) for(int k = (0); k < (a); ++k)
#define CLR(a, b) memset((a), (b), sizeof((a)))
#define clr(a) CLR((a), 0)
#define pb push_back
#define mkp make_pair
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 5000;
const int inf = 1000000000 + 7;
const double eps = 1e-5;

int n, a[100][100];
char s[1000];

void Swap(int i, int j)
{
	fk(n)
		swap(a[i][k], a[j][k]);
}

void solve()
{
	scanf("%d\n", &n);
	fi(n)
	{
		gets(s);
		fj(n)
			a[i][j] = s[j] - '0';
	}

	int ans = 0;
	fi(n)
	{
		for(int j = i; j < n; ++j)
		{
			bool ok = true;
			for(int k = i + 1; k < n; ++k)
				if (a[j][k] == 1)
				{
					ok = false;
					break;
				}
			if (ok)
			{
				for(int k = j; k > i; --k)
					Swap(k, k - 1);
				ans += j - i;
				break;
			}
		}
	}
	cout << ans << endl;
}

void initf()
{
	freopen("in.txt", "r",  stdin);
	freopen("out.txt", "w",  stdout);
}

int main()
{
	//initf();
	int t;
	scanf("%d", &t);
	fi(t)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return (0);
}