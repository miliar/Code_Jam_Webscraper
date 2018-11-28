#include <iostream>
using namespace std;
const int MAX = 5005;

int n, k;
int num[MAX];

int main (void)
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int Case = 1, T;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &k);
		int i, j, cnt = 0;
		memset(num, -1, sizeof(num));
		i = 0; j = 0;
		while (cnt < k)
		{
			while (num[i] != -1)
			{
				i ++;
				if (i == k) i = 0;
			}
			if (j == cnt)
			{
				num[i] = j+1;
				cnt ++;
				j = 0;
				continue;
			}
			j ++; i ++;
			if (i == k) i = 0;
		}

		printf("Case #%d:", Case++);
		scanf("%d", &i);
		while (i --)
		{
			scanf("%d", &j);
			printf(" %d", num[j-1]);
		}
		putchar('\n');
	}
	return 0;
}