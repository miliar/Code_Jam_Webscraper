#include <cstdio>
#include <algorithm>
#include <cmath>

#define SIZ int(2e3)
#define eps (1e-8)

using namespace std;

struct inter
{
	double len;
	int w;	

	inter() {}

	inter(int a, int b)
	{
		len = double(a), w = b;
	}
};

bool operator < (inter a, inter b)
{
	return a.w < b.w;
}

inter l[SIZ];

int main()
{
	int T;
	scanf("%d ", &T);

	for (int test = 0; test < T; test++)
	{
		int X, S, R, N, sum = 0;
		double res = 0, t;
		scanf("%d %d %d %lf %d ", &X, &S, &R, &t, &N);

		for (int i = 0; i < N; i++)
		{
			int beg, end, w;
			scanf("%d %d %d ", &beg, &end, &w);
			l[i] = inter(end - beg, w);
			sum += end - beg;
		}

		sort(l, l + N);

		if (int(t) * R >= X - sum)
		{
			res += double(X - sum) / R;
			t -= res;
		}
		else
		{
			X -= t * R;
			res += t;
			t = 0;
			res += double(X - sum) / S;
		}

		for (int i = 0; i < N; i++)
		{
			if ( (t * (l[i].w + R) - l[i].len) > eps || (fabs(t * (l[i].w + R) - l[i].len) < eps) )
			{
				res += double(l[i].len) / (l[i].w + R);
				t -= double(l[i].len) / (l[i].w + R);
			}
			else
			{
				res += t;
				l[i].len -= (l[i].w + R) * t;
				t = 0;
				res += double(l[i].len) / (l[i].w + S);				
			}
		}

		printf("Case #%d: %.6f\n", test + 1, res);
	}


	return 0;
}
