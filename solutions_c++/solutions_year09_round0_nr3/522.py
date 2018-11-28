#include <stdio.h>
#include <string.h>

const char str[20]="welcome to code jam";
const int maxn = 1100;
const int maxm = 30;

int n,m,t,cases,i,j;
int f[maxn][maxm];
char a[maxn];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&cases);
	for (t=1;t<=cases;t++)
	{
		gets(a);
		while (a[0]==0) gets(a);
		n=strlen(a);
		m=strlen(str);
		for (i=0;i<=m;i++) f[0][i]=0;
		f[0][0]=1;
		for (i=1;i<=n;i++)
		{
			f[i][0]=f[i-1][0];
			for (j=1;j<=m;j++)
			{
				f[i][j]=f[i-1][j];
				if (a[i-1]==str[j-1]) f[i][j]=(f[i][j]+f[i-1][j-1])%10000;
			}
		}
		printf("Case #%d: ",t);
		if (f[n][m]>=1000) printf("%d\n",f[n][m]); else
		if (f[n][m]>=100) printf("0%d\n",f[n][m]); else
		if (f[n][m]>=10) printf("00%d\n",f[n][m]); else
		printf("000%d\n",f[n][m]);
	}
	return 0;
}