#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

int n, k;

vector<string> m;
set<int> SS;

template<class T> T Abs(T x) { return x < 0 ? -x : x; }
bool Inside(int r, int c)
{
	return r >= 0 && r < n && c >= 0 && c < n;
}
bool RR(int r, int c)
{
	int d = Abs(r - (k - 1)) + Abs(c - (k - 1));
	if (d < k)
	{
		if (k & 1)
		{
			return d % 2 == 0;
		}
		else
		{
			return d % 2 == 1;
		}
	}
	return 0;
}
bool RRRR(int r, int c)
{
	if (RR(r, c))
		return 0;
	int d = Abs(r - (k - 1)) + Abs(c - (k - 1));
	if (k & 1)
	{
		return d % 2 == 0;
	}
	else
	{
		return d % 2 == 1;
	}
	return 0;
}
void GG(int r1, int c1, int r2, int c2, int& w, int& r)
{
	w -= RR(r1, c1);
	w -= RR(r2, c2);
	r += RRRR(r1, c1);
	r += RRRR(r2, c2);
}
bool GGGG(int r1, int c1, int r2, int c2)
{
	if (RR(r1, c1) && RR(r2, c2) && m[r1][c1] != m[r2][c2])
	{
		return 1;
	}
	return 0;
}
void Go()
{
	cin >> k;
	n = 2 * k - 1;
	m.clear();
	m.resize(n);
	getline(cin, m[0]);
	for (int i = 0; i < n; i++)
	{
		getline(cin, m[i]);
		m[i].resize(n, ' ');
	}
	int best = -1;
	for (int i = -10; i < n + 10; i++)
	{
		for (int j = -10; j < n + 10; j++)
		{
			int r = 0;
			int w = k * k;
			int d = 1;
			w -= RR(i, j);
			r += RRRR(i, j);
			while (w > 0)
			{
				for (int h = 0; h <= d; h++)
				{
					if (GGGG(i - d + h, j + h, i + d - h, j + h) || 
						GGGG(i - d + h, j - h, i + d - h, j - h) ||
						GGGG(i - d + h, j + h, i - d + h, j - h) ||
						GGGG(i + d - h, j + h, i + d - h, j - h))
					{
						r = -1;
						break;
					}
				}
				if (r == -1)
					break;
				else
				{
					for (int h = 0; h < d; h++)
					{
						GG(
							i - d + h,
							j + h,
							i + d - h,
							j - h,
							w, r);
						GG(
							i + h, 
							j + d - h,
							i - h,
							j - d + h,
							w, r);
					}
				}
				d++;
			}
			if (r != -1)
			{
				if (best == -1 || r < best)
					best = r;
			}
		}
	}
	/*cerr << best + k * k << endl;
	if (SS.count(best + k * k) == 0)
	throw 0;*/
	if (best == -1)
		throw 0;
	cout << best;
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "A-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int d = 1;
	int c = 0;
	for (int i = 0; i < 10000; i++)
	{
		c += d;
		d += 2;
		SS.insert(c);
	}
	int t;
	scanf("%d", &t);
	for (int yy = 1; yy <= t; yy++)
	{
		printf("Case #%d: ", yy);
		Go();
		printf("\n");
	}
	return 0;
}