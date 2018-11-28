#include <stdio.h>
#include <string.h>

char str[600];
char temp[600];
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
	freopen("C-small-attempt2.in","r",stdin);
	freopen("data.txt","w",stdout);
	int cas,i,t;
	char c;
	scanf("%d",&cas);
	getchar();
	for (i=1;i<=cas;i++)
	{
		memset(str,0,sizeof(str));
		t = 0;
		while((c = getchar()) != '\n')
		{
			if(strchr("welcom tdja",c) != NULL)
				str[t++] = c;
		}
		L = strlen(str);
		ans = 0;
		solve(0,0);
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}	