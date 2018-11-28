#define fr(i, a, x) for(int(i) = a; i <= x; ++i)
#define rfr(i, a, x) for(int(i) = a; i >= x; --i)
#define all(a) a.begin(), a.end()
#define Min(a, b) (a < b) ? a : b
#define Max(a, b) (a > b) ? a : b
#define pb push_back
#define MY_DEBUG 1

#include <cstdio>
#include <string>
#include <map>
#include <ctime>
#include <stack>
#include <deque>
#include <cstdlib>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

#ifdef MY_DEBUG
#include <fstream>
ifstream cin("input.txt");
ofstream cout("output.txt");
#else 
#include <iostream>
#endif

const double pi = acos(-1.0);
const double eps = 1e-9;
const int inf = 1e9;
const long long linf = 1e18;
const int prost = 51;

struct Treap
{
	int x, y, count;
	int sum[5];
	Treap * left, * right;
};

typedef Treap * pt;

int size(pt & t)
{
	if (t == NULL)
		return 0;
	return t->count;
}

int co(pt & t, int k)
{
	if (t == NULL)
		return 0;
	return t->sum[k];
}

void recalc(pt & t)
{
	t->count = size(t->left) + size(t->right) + 1;
	int c = size(t->left);
	for(int i = 0; i < 5; ++i)
		t->sum[i] = co(t->left, i) + co(t->right, 5 - (c + 1 + i) % 5);
	t->sum[c % 5] += t->x;
}

void merge(pt l, pt r, pt & t)
{
	if (l == NULL)
		t = r;
	else if (r == NULL)
		t = l;
	else if (l->y > r->y)
		merge(l->right, r, l->right), t = l;
	else
		merge(l, r->left, r->left), t = r;
	recalc(t);
}

void split(int x, pt t, pt & l, pt & r)
{
	if (t == NULL)
		l = r = NULL;
	else if (t->x < x)
		split(x, t->right, t->right, r), l = t, recalc(l);
	else
		split(x, t->left, l, t->left), r = t, recalc(r);
}

void insert(pt & t, pt & x)
{
	Treap l, r;
	pt pl = & l, pr = & r;
	split(x->x, t, pl, pr);
	merge(x, pr, pr);
	merge(pl, pr, t);
}

void erase(pt & t, int x)
{
	Treap l, r, h;
	pt pl = & l, pr = & r, ph = & h;
	split(x, t, pl, pr);
	split(x + 1, pr, ph, pr);
	merge(pl, pr, t);
}

void fcout(pt & t)
{
	if (!t)
		return;
	fcout(t->left);
	cout << t->x << ' ' << t->count << '\n';
	fcout(t->right);
}

long long hight, low;

long long nod(long long a, long long b)
{
	while(a > 0 && b > 0)
	{
		if (a > b)
			a %= b;
		else 
			b %= a;
	}
	return (a + b);
}

long long nok(long long a, long long b)
{
	long long c = nod(a, b);
	double d = a / c, ans;
	if (d * (double)b > (double)hight)
		return linf;
	return (a / c) * b;
}

int main()
{
#ifdef MY_DEBUG
	freopen("output.txt", "w", stdout);
#endif
	int counttest;
	cin >> counttest;
	for(int test = 1; test <= counttest; ++test)
	{
		long long n;
		cin >> n >> low >> hight;
		vector<long long> nk(n), nd(n), a(n);
		for(int i = 0; i < n; ++i)
			cin >> a[i];
		sort(a.begin(), a.end());
		nk[0] = a[0];
		for(int i = 1; i < n; ++i)
			nk[i] = nok( nk[i - 1], a[i] );
		nd[n - 1] = a[n - 1];
		for(int i = n - 2; i >= 0; --i)
			nd[i] = nod(nd[i + 1], a[i]);
		long long ans = linf;
		for(int i = 0; i < n - 1; ++i)
			if (nd[i + 1] >= low && nk[i] <= hight && nd[i + 1] >= nk[i])
			{
				if (nd[i + 1] % nk[i] == 0)
				{
					long long u = nd[i + 1] / nk[i], mn = linf;
					for(long long j = 1; j * j <= u; ++j)
						if (j > 0 && u % j == 0)
						{
							if (nk[i] * j >= low && nk[i] * j <= hight)
							{
								mn = j;
								break;
							}
							else if (nk[i] * (u / j) >= low && nk[i] * (u / j) <= hight)
							{
								if ( (u / j) < mn)
									mn = (u / j);
							}
						}
					if (mn < linf && nk[i] * mn < ans)
						ans = nk[i] * mn;
				}
			}
		if (nk[n - 1] <= hight)
		{
			long long mn = linf;
			for(long long j = (low / nk[n - 1]) + (low % nk[n - 1] != 0); j <= (hight / nk[n - 1]); ++j)
				if (j > 0)
				{
					mn = j;
					break;
				}
			if (mn < linf && nk[n - 1] * mn < ans)
				ans = nk[n - 1] * mn;
		}
		if (nd[0] >= low)
		{
			long long mn = linf;
			for(long long j = 1; j * j <= nd[0]; ++j)
				if (j > 0 && nd[0] % j == 0)
				{
					if (j >= low && j <= hight)
					{
						mn = j;
						break;
					}
					else if (nd[0] / j >= low && nd[0] / j <= hight)
					{
						if (nd[0] / j < mn)
							mn = nd[0] / j;
					}
				}
			if (mn < linf && mn < ans)
				ans = mn;
		}
		if (ans == linf)
			cout << "Case #" << test << ": NO\n";
		else
			cout << "Case #" << test << ": " << ans << '\n';
	}
}

/*long long l, t, n, c, t0, ans = 0, lans = 0, s = 0;
		cin >> l >> t >> n >> c;
		vector<int> a(c);
		for(int i = 0; i < c; ++i)
		{
			cin >> a[i];
			s += a[i];
			lans += a[i];
		}
		lans *=	(n / c);
		for(int i = 0; i < n % c; ++i)
			lans += a[i];
		lans *= 2;
		ans = lans;
		s *= 2;
		long long to = (t / s);
		if (t >= lans)
		{
			cout << "Case #" << test << ": " << lans << '\n';
			continue;
		}
		t -= to * s;
		long long pos = c, help = 0;
		for(int i = 0; i < c; ++i)
			if (2 * a[i] <= t)
				t -= a[i];
			else 
			{
				pos = i + 1;
				help = a[i] - (t + 1) / 2;
				t = 0;
				break;
			}
		long long kolkr = (n / c);
		long long r = (kolkr - to - 1);
		vector< pair<long long, long long> > v(c);
		for(int i = 0; i < c; ++i)
			v[i] = pair<long long, long long>(a[i], r);
		v.push_back( pair<long long, long long>(help, 1) );
		for(int i = pos; i < c; ++i)
			++v[i].second;
		for(int i = 0; i < n % c; ++i)
			++v[i].second;
		sort(v.rbegin(), v.rend());
		for(int i = 0; i < v.size(); ++i)
			if (l > 0)
			{
				long long d = v[i].second;
				if (d > l)
					d = l;
				l -= d;
				ans -= v[i].first * d;
			}
		cout << "Case #" << test << ": " << ans << '\n';*/