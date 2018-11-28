#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int nt;
int C, D, n;

int x[1000000];

bool good(double t)
{
	double prev = x[0] - t;
	for(int i = 1; i < n; i++)
	{
		prev += D;
		if (prev > x[i] + t + 1e-10) return false;
		prev = max(prev, x[i] - t);
	}
	return true;
}

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);
		
		scanf("%d %d", &C, &D);
		
		n = 0;
		
		for(int i = 0; i < C; i++)
		{
			int pos, cnt;
			scanf("%d %d", &pos, &cnt);
			for(int j = 0; j < cnt; j++) x[n++] = pos;
		}
		
		double L = 0, R = 1e30;
		while(R - L > 1e-10)
		{
			double x = (L + R) / 2;
			if (good(x)) R = x; else L = x;
		}
		
		printf("%.8lf\n", R);
	}
	
	return 0;
}