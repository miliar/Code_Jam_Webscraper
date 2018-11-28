#include <iostream>
using namespace std;

char c[] = "welcome to code jam";
int n;
char str[502];
int cnt;
int nc;

void dfs(int p, int cp)
{
	if (str[p] == 0)
	{
		if (cp == 19)
		{
			cnt++;
			if (cnt == 10000)
			{
				cnt = 0;
			}
		}
		return;
	}
	if (str[p] == c[cp])
	{
		dfs(p+1, cp+1);
	}
		dfs(p+1, cp);
}

int main()
{
	freopen("E:\\1.in", "r", stdin);
	freopen("C.out", "w", stdout);
	nc= 1;
	scanf("%d", &n);
	getchar();
	while (n--)
	{
		cnt = 0;
		gets(str);
		dfs(0, 0);
		char ans[5] = {0};
		for (int i=10, j=3; j>=0; j--)
		{
			ans[j] = cnt % i + '0';
			cnt /= i;
		}
		printf("Case #%d: %s\n", nc++, ans);
	}
}