#include <cstdio>
#include <iostream>
#define LMAX 20
#define DMAX 5010
#define NMAX 510
#define IS1(x,k) ((x&(1<<k))!=0)
#define IS0(x,k) (!IS1(x,k))
#define SET1(x,k) (x|(1<<k))
#define SET0(x,k) (x(1<<k))


char s[1000];

int dic[DMAX][LMAX];
int p[NMAX][LMAX];
int ans[NMAX];
int n,d,l;


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	scanf("%d%d%d",&l,&d,&n);
	memset(dic,0,sizeof(dic));
	memset(p,0,sizeof(p));
	memset(ans,0,sizeof(ans));
	getchar();
	for (i=1;i<=d;i++)
	{
		gets(s);
		for (j=0;j<l;j++)
		{
			dic[i][j]=SET1(dic[i][j],(s[j]-'a'));
		}
	}
	for (i=1;i<=n;i++)
	{
		gets(s);
		int ls=strlen(s);
		bool f=false;
		int q=0;
		j=0;
		while (j<ls)
		{
			if (s[j]>='a'&&s[j]<='z')
			{
				if (f==false)
				{
					p[i][q]=SET1(p[i][q],s[j]-'a');
					q++;
					j++;
				}
				else
				{
					p[i][q]=SET1(p[i][q],s[j]-'a');
					j++;
				}
			}
			else if (s[j]=='(')
			{
				f=true;
				j++;
			}
			else
			{
				f=false;
				q++;
				j++;
			}
		}
	}

	for (i=1;i<=d;i++)
	{
		for (j=1;j<=n;j++)
		{
			bool f=true;
			for (k=0;k<l;k++)
			{
				if ((~dic[i][k]|(p[j][k]))!=(~0))
				{
					f=false;
					break;
				}
			}
			if (f==true) ans[j]++;
		}
	}

	for (i=1;i<=n;i++)
	{
		printf("Case #%d: %d\n",i,ans[i]);
	}

	return 0;
}
