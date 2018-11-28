#include <cstdio>
#include <cstring>

const int maxn = 40;

int a[maxn];
char s[maxn + 1];
int n;

int main()
{
	int testnumber, testcount;
	
	freopen("A-large (1).in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &testnumber);
	for (testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", s);
			int j = n - 1;
			while (j > 0 && s[j] == '0') j--;
			a[i] = j;
		}
		
		int total = 0;
		for (int i = 0; i < n; i++)
		{
			int j = 0;
			while (a[j] > i) j++;
			for (int k = 0; k < j; k++)
				if (a[k] < n) total++;
			a[j] = 0x7fffffff;
		}
		printf("Case #%d: %d\n", testcount + 1, total);
	}
	
	return 0;
}
