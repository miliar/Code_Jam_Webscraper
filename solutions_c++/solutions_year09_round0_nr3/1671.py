#include <cstdio>
#include <cstring>

int T,L=19;
char s[512];
char d[24]="welcome to code jam";
int sum[512][20];

void init()
{
	gets(s);
}




void work()
{
	int i,j,k,len,tot;
	
	memset(sum,0,sizeof(sum));
	len=strlen(s);
	sum[0][0]=1;
	for (i=0;i<len;i++)
	{
		for (j=0;j<L;j++)
		{
			if (s[i]==d[j])
			{
				for (k=0;k<=i;k++)
				{
					sum[i+1][j+1]=(sum[i+1][j+1]+sum[k][j])%10000;
				}
			}
			
		}
	}
	
	tot=0;
	for (i=0;i<=len;i++)
	{
		tot=(tot+sum[i][L])%10000;
	}
	printf("%04d\n",tot);
}

int main()
{
	int i;
	
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d ",&T);
	for (i=1;i<=T;i++)
	{
		init();
		printf("Case #%d: ",i);
		work();
	}
	return 0;
}
