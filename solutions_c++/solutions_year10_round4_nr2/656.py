#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int P;
int a[1024];
int c[11][512];
int d[11][1024][11];

int calc(int level, int start, int sub)
{
	if (d[level][start][sub] != -1) return d[level][start][sub];
	
	int left = P - level;
	int n = 1 << left;
	
	// check if done
	
	bool good = true;
	for(int i = 0; i < n; i++) if (a[start + i] > sub) { good = false; break;}
	
	if (good)
	{
		d[level][start][sub] = 0;
		return 0;
	}
	
	// check if necessary
	
	for(int i = 0; i < n; i++) if (a[start + i] - sub == left) { good = true; break;}
	
	int res_1 = calc(level + 1, start, sub + 1) + calc(level + 1, start + n / 2, sub + 1) + c[level][start / n];

	if (good)
	{
		d[level][start][sub] = res_1;
		return res_1;
	}
	
	int res_0 = calc(level + 1, start, sub) + calc(level + 1, start + n / 2, sub);
	
	if (res_1 < res_0) res_0 = res_1;
	
	d[level][start][sub] = res_0;
	return res_0;
}

int main()
{
	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);
		
		scanf("%d", &P);
		int n = 1 << P;
		
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			a[i] = P - a[i];
		}
		
		for(int k = P - 1; k >= 0; k--)
		{
			int nr = 1 << k;
			for(int j = 0; j < nr; j++) scanf("%d", &c[k][j]);
		}
		
		memset(d, -1, sizeof d);
		
		int res = calc(0, 0, 0);
		
		printf("%d\n", res);
	}
	return 0;
}