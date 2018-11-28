#include<stdio.h>
#include<memory.h>
#include<string.h>
char need[20] = {"welcome to code jam"};
char s[1000];
int ans[30];
int main()
{
	int cas, i, j, v, len;
	freopen("cs.in","r",stdin);
	freopen("c2.txt","w",stdout);
	scanf("%d",&cas);
	gets(s);
	for(v = 1; v <= cas; v++)
	{
		memset(ans, 0, sizeof(ans));
		gets(s);
		len = strlen(s);
		for(i = 0; i < len; i++)
		{
			for(j = 18; j >= 0; j--)
				if (need[j] == s[i])
				{
					if (j == 0)
						ans[j]++;
					else
					{
						ans[j] += ans[j - 1];
						ans[j] %= 10000;
					}
				}
		}
		printf("Case #%d: %04d\n",v, ans[18]);
	}
}