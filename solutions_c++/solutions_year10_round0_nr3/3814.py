#include<iostream>
using namespace std;

int a[10001];

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	int name = 1;
	scanf("%d", &T);
	while(T--)
	{
		int n, k, r;
		scanf("%d %d %d", &r, &k, &n);
		int i;
		for(i=0; i<n; i++)
			scanf("%d", &a[i]);

		int money = 0;
		int cas = 0;
		int count = 0;
		for(i=0; i<n; i++)
			count += a[i];
		if(count <= k)
		{
			printf("Case #%d: %d\n", name++, count * r);
			continue;
		}
		count = 0;

		int cnt = n;
		int start = 0;
		int end;
		while(cas < r)
		{
			int j;
			for(i=start, j=0; i<cnt; i++,j++)
			{
				count += a[i];
				if(count > k)
				{
					count -= a[i];
					money += count;
					cas ++;
					for(int h=start; h<start+j; h++)
						a[cnt++] = a[h];
					start = start + j;

					break;
				}
			}

			if(i == cnt)
			{
				cas ++;
				money += (r - cas) * count;
			}
			count = 0;
		}

		printf("Case #%d: %d\n", name++, money);
	}
}

						



