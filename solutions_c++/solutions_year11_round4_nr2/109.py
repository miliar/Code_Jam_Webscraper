#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int nt, n, m, D;

char s[500][501];

__int64 a[500][500];
__int64 ai[500][500];
__int64 aj[500][500];

__int64 sum[500][500];
__int64 sumi[500][500];
__int64 sumj[500][500];

__int64 Sum(int i1, int j1, int i2, int j2)
{
	i1--; i2--; j1--; j2--;
	
	__int64 res = sum[i2][j2];
	
	if (i1 >= 0) res -= sum[i1][j2];
	if (j1 >= 0) res -= sum[i2][j1];
	if (i1 >= 0 && j1 >= 0) res += sum[i1][j1];
	
	return res;
}

__int64 Sumi(int i1, int j1, int i2, int j2)
{
	i1--; i2--; j1--; j2--;
	
	__int64 res = sumi[i2][j2];
	
	if (i1 >= 0) res -= sumi[i1][j2];
	if (j1 >= 0) res -= sumi[i2][j1];
	if (i1 >= 0 && j1 >= 0) res += sumi[i1][j1];
	
	return res;
}

__int64 Sumj(int i1, int j1, int i2, int j2)
{
	i1--; i2--; j1--; j2--;
	
	__int64 res = sumj[i2][j2];
	
	if (i1 >= 0) res -= sumj[i1][j2];
	if (j1 >= 0) res -= sumj[i2][j1];
	if (i1 >= 0 && j1 >= 0) res += sumj[i1][j1];
	
	return res;
}


int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d %d", &n, &m, &D);
		
		for(int i = 0; i < n; i++) scanf("%s", s[i]);
		
		for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			a[i][j] = D + (s[i][j] - '0');
			ai[i][j] = i * a[i][j];
			aj[i][j] = j * a[i][j];
		}
		
		for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
		{
			sum[i][j] = a[i][j];
			if (i) sum[i][j] += sum[i - 1][j];
			if (j) sum[i][j] += sum[i][j - 1];
			if (i && j) sum[i][j] -= sum[i - 1][j - 1];
			
			sumi[i][j] = ai[i][j];
			if (i) sumi[i][j] += sumi[i - 1][j];
			if (j) sumi[i][j] += sumi[i][j - 1];
			if (i && j) sumi[i][j] -= sumi[i - 1][j - 1];

			sumj[i][j] = aj[i][j];
			if (i) sumj[i][j] += sumj[i - 1][j];
			if (j) sumj[i][j] += sumj[i][j - 1];
			if (i && j) sumj[i][j] -= sumj[i - 1][j - 1];
		}
		
	/*	puts("");
		for(int i = 0; i < n; i++, puts(""))
		for(int j = 0; j < n; j++) printf("%5I64d", a[i][j]);
		
		puts("");
		for(int i = 0; i < n; i++, puts(""))
		for(int j = 0; j < n; j++) printf("%5I64d", sum[i][j]);*/
		
		int k = min(n, m);
		bool ok = false;
		
		while(k >= 3)
		{
			for(int i = 0; i + k <= n && !ok; i++)
			for(int j = 0; j + k <= m && !ok; j++)
			{
				__int64 total = Sum(i, j, i + k, j + k);
				
				__int64 totali = Sumi(i, j, i + k, j + k);
				__int64 totalj = Sumj(i, j, i + k, j + k);
				
				total  -=  a[i][j] +  a[i + k - 1][j] +  a[i][j + k - 1] +  a[i + k - 1][j + k - 1];
				totali -= ai[i][j] + ai[i + k - 1][j] + ai[i][j + k - 1] + ai[i + k - 1][j + k - 1];
				totalj -= aj[i][j] + aj[i + k - 1][j] + aj[i][j + k - 1] + aj[i + k - 1][j + k - 1];				
				
				// totali / total == (i + i + k - 1) / 2
				// totalj / total == (j + j + k - 1) / 2
				
	
				// totali * 2 == (i + i + k - 1) * total
				// totalj * 2 == (j + j + k - 1) * total
				
				//printf("(%d %d)-(%d %d): %I64d %I64d %I64d\n", i, j, i + k - 1, j + k - 1, total, totali, totalj);
				
				if (totali * 2 == (i + i + k - 1) * total && totalj * 2 == (j + j + k - 1) * total)
				{
					ok = true;
					break;
				}
			}
			if (ok) break;
		
			k--;
		}
		
		if (k < 3) puts("IMPOSSIBLE"); else printf("%d\n", k);
	}
	
	return 0;
}