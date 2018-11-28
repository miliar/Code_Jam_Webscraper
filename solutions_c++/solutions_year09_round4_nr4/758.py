#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

const int maxn = 40;
const double zero = 1e-5;

struct circle
{
	int x, y, r;
};

circle a[maxn];
long long bitmap[maxn * maxn * maxn];
double r[maxn * maxn * maxn];
int n, top;

double getd(circle t, double x, double y)
{
	return t.r + sqrt((t.x - x) * (t.x - x) + (t.y - y) * (t.y - y));
}

bool cover(circle t, double x, double y, double r)
{
	return getd(t, x, y) <= r + zero;
}

double getr(circle t1, circle t2, circle t3, double x, double y)
{
	double r1 = getd(t1, x, y);
	double r2 = getd(t2, x, y);
	double r3 = getd(t3, x, y);
	if (r2 > r1) r1 = r2;
	if (r3 > r1) r1 = r3;
	return r1;
}

void getbitmap(circle t1, circle t2, circle t3)
{
	double x = (double) (t1.x + t2.x + t3.x) / 3;
	double y = (double) (t1.y + t2.y + t3.y) / 3;
	double delta = 5000;
	double ra = getr(t1, t2, t3, x, y);
	double t;
	double dx, dy;
	while (delta > 1e-10)
	{
		for (int i = 0; i < 200; i++)
		{
			dx = ((double) rand() / RAND_MAX * 2 - 1) * delta;
			dy = ((double) rand() / RAND_MAX * 2 - 1) * delta;
			int cnt = 0;
			while ((t = getr(t1, t2, t3, x + dx, y + dy)) < ra || cnt != 0)
			{
				if (t < ra)
				{
					++cnt;
					ra = t;
					x += dx;
					y += dy;
					dx *= 2;
					dy *= 2;
				}
				else
				{
					--cnt;
					dx /= 2;
					dy /= 2;
				}
			}
		}
		delta /= 1.2;
	}
	long long bm = 0;
	for (int i = 0; i < n; i++)
		if (cover(a[i], x, y, ra)) bm |= 1 << i;
	bitmap[top] = bm;
	r[top] = ra;
	top++;
}

int main()
{
	int testnumber, testcount;
	double min;
	
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("d.out", "w", stdout);
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d%d%d", &a[i].x, &a[i].y, &a[i].r);
		
		top = 0;
		
		for (int i = 0; i < n; i++)
		{
			getbitmap(a[i], a[i], a[i]);
			for (int j = i + 1; j < n; j++)
			{
				getbitmap(a[i], a[i], a[j]);
				for (int k = j + 1; k < n; k++)
				{
					getbitmap(a[i], a[j], a[k]);
				}
			}
		}
		
		min = 1e100;
		long long t = (((long long) 1) << n) - 1;
		for (int i = 0; i < top; i++)
			if (r[i] < min)
			for (int j = i; j < top; j++)
				if ((bitmap[i] | bitmap[j]) == t && r[j] < min)
				{
					if (r[i] > r[j]) min = r[i];
					else min = r[j];
				}
		printf("Case #%d: %.6lf\n", testcount + 1, min);
	}
	
	return 0;
}
