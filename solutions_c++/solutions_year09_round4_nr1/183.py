#include<stdio.h>
#define maxn 41
char s[maxn][maxn+1];
int lenth[maxn];

int n;

int solve()
{
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		lenth[i]=-1;
		scanf("%s",s[i]);
		for(int j=0;j<n;++j)
			if(s[i][j]=='1')
				lenth[i]=j;
	}
	int re=0;
	for(int i=0;i<n;++i)
		if(lenth[i]>i)
		{
			int p;
			for(p=i+1;lenth[p]>i;++p);
			for(int j=p;j>i;--j)
			{
				++re;
				int t=lenth[j];
				lenth[j]=lenth[j-1];
				lenth[j-1]=t;
			}
		}
	return re;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
		printf("Case #%d: %d\n",i+1,solve());
	return 0;
}

