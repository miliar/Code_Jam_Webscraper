#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
using namespace std;

const int MAXN = 3000 + 10;

int n, w, l;
pair<int, int> r[MAXN];
int x[MAXN], y[MAXN];

#define L first.first
#define R first.second
#define H second

/*
bool putbox(int w, int l)
{
	pair<pair<int, int>, int> a[1000];
	int cnt;

	cnt = 1;
	a[0].L = 0; a[0].R = w; a[0].H = l;
	for (int i = 0; i < n; ++i)
	{
		bool find = false;
		for (int j = 0; j < cnt; ++j)
			if (a[j].H >= r[i])	{
				// left edge
				if (a[j].L == 0)
				{
					if (a[j].R >= r[i])
					{
						if (a[j].R == r[i])
						{
							if (a[j].H == l)
								a[j].H -= r[i];
							else 
								a[j].H -= r[i] * 2;
						}
						else {
							a[j].L = r[i];
							a[j].H -= r[i] * 2;
							a[cnt].L = 0; a[cnt].R = r[i];
							if (a[j].H == l)
								a[cnt].H = a[j].h - r[i];
							else 
								a[cnt].H = a[j].h - r[i] * 2;
							++cnt;
						}
					}
					
				}
				// right edge
				else if (a[i].R == w)
				{
					if (a[j].< < r[i])
					{
						if (a[j].R == r[i])
						{
							if (a[j].H == l)
								a[j].H -= r[i];
							else 
								a[j].H -= r[i] * 2;
						}
						else {
							a[j].L = r[i];
							a[j].H -= r[i] * 2;
							a[cnt].L = 0; a[cnt].R = r[i];
							if (a[j].H == l)
								a[cnt].H = a[j].h - r[i];
							else 
								a[cnt].H = a[j].h - r[i] * 2;
							++cnt;
						}
					}

				}
		}
	}
	return true;
}
*/

bool cmp(pair<int, int> x, pair<int, int> y)
{
	return x.first > y.first;
}
bool cmp2(pair<int, int> x, pair<int, int> y)
{
	return x.second < y.second;
}

int main()
{
	int T;
	freopen("b-large.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &r[i].first);
			r[i].second = i;
		}
		printf("Case #%d:", tt);
		sort(r, r + n, cmp);
		int hor = 0, far = 0, hh = 0;
		bool can = true;
		for (int i = 0; i < n; ++i)
		{
			//printf("%d %d %d\n", hor, far, r[i]);
			if (hor != 0)
				x[r[i].second] = hor + r[i].first; 
			else 
				x[r[i].second] = hor;
			y[r[i].second] = far;
			if (far == 0)
			{
				if (hor == 0)
					hh += r[i].first;
				else 
					hh += r[i].first * 2;
			}
			far += r[i].first;
			if (i != n - 1)
				far += r[i + 1].first;
			if (far > l)
			{
				far = 0;
				hor = hh;
			}
		}
		for (int i = 0; i < n; ++i)
		{
			if (x[i] > w || y[i] > l)
				can = false;
				
		}
		if (!can)
			puts("xxxx");
		else
		{
		for (int i = 0; i < n; ++i)
		{
			printf(" %d %d", x[i], y[i]);
		}
		puts("");
		}
		/*
		if (!putbox(w, l))
		{
			if (!putbox(l, w))
			{
				sort(r, r + n, cmp);
			}
		}
		*/
	}
	return 0;
}
