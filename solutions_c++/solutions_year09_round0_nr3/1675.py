#include <stdio.h>
#include <string.h>

#define MAX_L 35
char str[MAX_L];
int ans,L;
char s[] = "welcome to code jam"; 

void solve(int x,int k)
{
	int i;
	for (i=k;i<L;i++)
	{
		if (s[x] == str[i])
		{
			if(x==18)
			{
				ans  = (ans+1) % 10000;
			}
			else
			{
				solve(x+1,i+1);
			}
		}
	}
}


int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int cas,i;
	scanf("%d",&cas);
	getchar();
	for (i=1;i<=cas;i++)
	{
		gets(str);
		L = strlen(str);
		ans = 0;
		solve(0,0);
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}