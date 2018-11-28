#include <stdio.h>
#include <string.h>
char s[600];
char *cc = "welcome to code jam";
int ans[600][600];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	gets(s);
	for (int tt=0;tt<t;tt++)
	{
		gets(s);
		int l = strlen(s);
		memset(ans,0,sizeof(ans));
		for (int i=0;i<l;i++)
			for (int j=0;j<19;j++)
			{
				ans[i][j]=0;
				if (i>0)
					ans[i][j]+=ans[i-1][j];
				if (s[i]==cc[j])
				{
					if (i>0 && j>0)
						ans[i][j]+=ans[i-1][j-1];
					if (j==0)
						ans[i][j]++;
				}
				ans[i][j]%=10000;
			}

		printf("Case #%d: %0.4d\n",tt+1,ans[l-1][18]);
	}
	return 0;
}