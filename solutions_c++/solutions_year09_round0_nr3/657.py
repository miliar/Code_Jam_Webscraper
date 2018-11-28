#include <stdio.h>
#include <string.h>
const char str[20]="welcome to code jam";
int f[600][20];
bool g[600][20];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d\n",&cases);
	for (int k=1;k<=cases;k++)
	{
		printf("Case #%d: ",k);
		char s[501];
		scanf("%[^\n]\n",s);
		memset(f,0,sizeof(f));
		memset(g,false,sizeof(g));
		f[0][0]=1;g[0][0]=true;
		for (int i=1;i<=strlen(s);i++)
			for (int j=1;j<=strlen(str);j++)
				if (s[i-1]==str[j-1])
				{
					for (int l=0;l<i;l++)
						if (g[l][j-1])
						{
							f[i][j]=(f[i][j]+f[l][j-1])%10000;
							g[i][j]=true;
						}
				}
		int ans=0;
		for (int i=0;i<=strlen(s);i++)
			if (g[i][strlen(str)]) ans=(ans+f[i][strlen(str)])%10000;
		printf("%04d\n",ans);
	}

	return 0;
}