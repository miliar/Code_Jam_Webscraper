#include <iostream>
#include <string.h>
using namespace std;

char s[45];

int com(int x,int y)
{
	int t,p,i;
	t=1;
	p=0;
	for(i=y;i>=x;i--)
	{
		p=(p+t*(s[i]-'0'))%210;
		t=(t*10)%210;
	}
	return p;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int n,j,i,k,m,l;
	__int64 t;
	__int64 a[45][210];
	
	scanf("%d",&n);
	for(k=1;k<=n;k++)
	{
		printf("Case #%d: ",k);
		scanf("%s",s);
		l=strlen(s);
		memset(a,0,sizeof(a));
		a[0][0]=1;
		for(i=0;i<l;i++)
			for(j=0;j<210;j++)
			{
				if(a[i][j])
				{
					for(m=i;m<l;m++)
					{
						int p=com(i,m);
						a[m+1][(j+p)%210]+=a[i][j];
						if(i)
							a[m+1][(j-p+210)%210]+=a[i][j];
					}
				}
			}
		t=0;
		for(i=0;i<210;i++)
			if(i%2==0||i%3==0||i%7==0||i%5==0)
				if(a[l][i])
					t+=a[l][i];
		printf("%I64d\n",t);
	}

	return 0;
}