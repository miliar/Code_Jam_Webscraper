#include<stdio.h>
#include<string.h>

int pn[20],p[20][500],len,d[20][500];
char str[20]={"welcome to code jam"},string[501];

int process()
{
	int i,j,k;
	len=strlen(string);
	for(i=0;i<19;i++)
	{
		pn[i]=0;
		for(j=0;j<len;j++)
		{
			if(str[i]==string[j])
			{
				p[i][pn[i]++]=j;
			}
		}
		for(j=0;j<pn[i];j++)
		{
			if(i==0){ d[i][j]=1; continue; }
			d[i][j]=0;
			for(k=0;k<pn[i-1];k++)
			{
				if(p[i-1][k]<p[i][j])
				{
					d[i][j]=(d[i][j]+d[i-1][k])%10000;
				}
			}
		}
	}
	int ans=0;
	for(i=0;i<pn[18];i++)
	{
		ans=(ans+d[18][i])%10000;
	}
	return ans;
}

int main()
{
	int i,n,ans;
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&n);
	for(i=1;i<=n;i++)
	{
		gets(string);
		ans=process();
		printf("Case #%d: %04d\n",i,ans);
	}
	return 0;
}