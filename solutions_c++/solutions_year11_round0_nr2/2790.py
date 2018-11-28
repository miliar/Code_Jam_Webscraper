#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstring>

using namespace std;

const int maxn=1000;
char a[maxn][3];
char b[maxn][2];
char c[maxn];

bool Judge(char a,char b,char c,char d)
{
	if ((a==c&&b==d)||(a==d&&b==c))
	{
		return true;
	}
	return false;
}

void clear(int &tot,int n)
{
	int i,j;
	for (i=0;i<n;i++)
	{
		for (j=0;j<tot-1;j++)
		if (Judge(c[j],c[tot-1],b[i][0],b[i][1]))
		tot=0;
		break;
	}
}

bool combine(int &tot,int n)
{
	int i;
	for (i=0;i<n;i++)
	{
		if (Judge(c[tot-1],c[tot-2],a[i][0],a[i][1]))
		{
			tot--;
			c[tot-1]=a[i][2];
			return true;
		}
	}
	return false;
}

int main()
{
freopen("a.in","r",stdin);
freopen("a.out","w",stdout);

	int cas;
	int ca=0;
	int n,m,i,d;
	scanf("%d",&cas);
	while (cas--)
	{
		ca++;
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf(" %c%c%c",&a[i][0],&a[i][1],&a[i][2]);
		scanf("%d",&m);
		for (i=0;i<m;i++)
			scanf(" %c%c",&b[i][0],&b[i][1]);
		scanf("%d",&d);
		int tot=0;
		for (i=0;i<d;i++)
		{
			if (i==0)
			scanf(" %c",&c[tot++]);
			else scanf("%c",&c[tot++]);
			if (tot!=1)
			{
				if (!combine(tot,n))			
				clear(tot,m);
			}
		}
		printf("Case #%d: [",ca);
		for (i=0;i<tot;i++)
		{
			if (i==0)
				printf("%c",c[i]);
			else printf(", %c",c[i]);
		}
		printf("]\n");
	}
fclose(stdin);
fclose(stdout);

return 0;

}