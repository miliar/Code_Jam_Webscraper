#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>

using namespace std;
const int maxn=1000;
int b[maxn],d[maxn],o[maxn];
char c[maxn];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int cas,n,i,op,bp,opp,bpp;
	int t;
	int ca;
	ca=0;
	scanf("%d",&cas);
	while (cas--)
	{
		ca++;
		scanf("%d",&n);
		b[0]=0;
		o[0]=0;
		for (i=0;i<n;i++)
		{
			scanf(" %c",&c[i]);
			scanf("%d",&d[i]);
			if (c[i]=='O')
			{
				o[++o[0]]=d[i];
			}
			else b[++b[0]]=d[i]; 
		}
		op=1;
		bp=1;
		opp=1;
		bpp=1;
		i=0;
		t=0;
		while (i<n)
		{
			t++;
			if (c[i]=='O')
			{
				if (op==o[opp])
				{
					opp++;
					i++;
				}
				else 
				{
					if (op<o[opp]) op++;
					else op--;
				}
				if (bpp<=b[0])
				{
					if (b[bpp]>bp) bp++;
					else if (b[bpp]<bp) bp--;
				}
			}
			else
			{
				if (bp==b[bpp])
				{
					bpp++;
					i++;
				}
				else 
				{
					if (bp<b[bpp]) bp++;
					else bp--;
				}
				if (opp<=o[0])
				{
					if (o[opp]>op) op++;
					else if (o[opp]<op) op--;
				}
			
			}
		}
		printf("Case #%d: %d\n",ca,t);
	}

fclose(stdin);
fclose(stdout);
return 0;
}