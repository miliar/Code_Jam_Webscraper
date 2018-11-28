#include <stdio.h>
struct abc
{
	char a,b,c;//ºÏ³É
}hc[100];
struct ab
{
	char a,b;//ÏûÊ§
}xs[100];
char s[105];
char ans[105];
int hn,xn,an;
bool hebing()
{
	int i;
	if(an<=0)
		return 0;
	for(i=0;i<hn;i++)
	{
		if(hc[i].a==ans[an-1]&&hc[i].b==ans[an])
		{
			an--;
			ans[an]=hc[i].c;
			return 1;
		}
	}
	return 0;
}
bool xiaoshi(int a,int b)
{
	int i;
	for(i=0;i<xn;i++)
	{
		if(xs[i].a==ans[a]&&xs[i].b==ans[b])
		{
			an=-1;
			return 1;
		}
	}
	return 0;
}
int main ()
{
	int cas,ca,c,d,n,i;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		hn=xn=0;
		scanf("%d",&c);
		for(i=0;i<c;i++)
		{
			scanf("%s",&s);
			hc[hn].a=s[0];
			hc[hn].b=s[1];
			hc[hn++].c=s[2];
			hc[hn].a=s[1];
			hc[hn].b=s[0];
			hc[hn++].c=s[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++)
		{
			scanf("%s",&s);
			xs[xn].a=s[0];
			xs[xn++].b=s[1];
			xs[xn].a=s[1];
			xs[xn++].b=s[0];
		}
		scanf("%d%s",&n,&s);
		an=0;
		ans[an]=s[0];
		int j;
		for(i=1;i<n;i++)
		{
			ans[++an]=s[i];
			while(hebing());
			for(j=0;j<an;j++)
			{
				if(xiaoshi(j,an))
				{
					break;
				}
			}
		}
		printf("Case #%d: [",ca);
		if(an>=0)
			printf("%c",ans[0]);
		for(i=1;i<=an;i++)
			printf(", %c",ans[i]);
		printf("]\n");


	}
}