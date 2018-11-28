#include <stdio.h>
#include <memory.h>
#include <algorithm>

using namespace std;

int n;
long long p, k, l;
long long matrix[1000];
long long keys[1000][1000];
long long num;
long long cnt;
long long rez;

void Init()
{
	p = 0;
	k = 0;
	l = 0;
	cnt = 0;
	rez = 0;
	memset(matrix, 0, sizeof(matrix));
	memset(keys, 0, sizeof(keys));
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		Init();
		scanf("%lld%lld%lld", &p, &k, &l);
		for (int j = 0; j < l; j++)
			scanf("%lld", &matrix[j]);
		sort(matrix, matrix + l);
		num = 0;
		for (int j = 0; j < l; j++)
		{
			keys[num][cnt] = matrix[l - j - 1];
			num++;
			if (num >= k)
			{
				num %= k;
				cnt++;
			}
		}
		for (int j = 0; j < k; j++)
			for (int u = 0; u <= cnt; u++)
				rez += keys[j][u] * (u + 1);
		printf("Case #%d: %lld\n", i + 1, rez);
	}
	return 0;
}