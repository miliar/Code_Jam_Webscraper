#include<cstdio>
#include<memory>

int n,i,j,k,f[505][20];
char a[505],b[20]="welcome to code jam";

int g(int i,int j)
{
	int s;
	if(j<0)return 1;
	if(i<0)return 0;
	if(f[i][j]>=0)return f[i][j];
	s=g(i-1,j);
	if(a[i]==b[j])s+=g(i-1,j-1);
	if(s>9999)s-=10000;
	f[i][j]=s;
	return s;
}

int main()
{
	freopen("d:\\c.in","r",stdin);
	freopen("d:\\c.out","w",stdout);
	scanf("%d\n",&n);
	for(i=1;i<=n;i++)
	{
		memset(f,-1,sizeof(f));
		gets(a);
		for(j=0;a[j];j++);
		printf("Case #%d: %04d\n",i,g(j-1,18));
	}
	return 0;
}