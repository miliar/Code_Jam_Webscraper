#include <iostream>
#include <algorithm>
using namespace std;

struct gao
{
	int a,b;
	bool f;
}c[1001];

int a[1001];
int b[1001];
int na,nb;

bool com(gao a,gao b)
{
	if(a.a!=b.a)
		return a.a<b.a;
	return a.b<b.b;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1o.in","w",stdout);
	int nn,ii,i,j,k,t,tt,n1,n2,n;
	char s1[10],s2[10];
	scanf("%d",&nn);
	for(ii=1;ii<=nn;ii++)
	{
		printf("Case #%d: ",ii);
		scanf("%d",&tt);
		scanf("%d%d",&na,&nb);
		n=na+nb;
		for(i=0;i<na;i++)
		{
			scanf("%s%s",s1,s2);
			c[i].a=((s1[0]-'0')*10+s1[1]-'0')*60+(s1[3]-'0')*10+s1[4]-'0';
			c[i].b=((s2[0]-'0')*10+s2[1]-'0')*60+(s2[3]-'0')*10+s2[4]-'0';
			c[i].f=false;
		}
		for(i;i<n;i++)
		{
			scanf("%s%s",s1,s2);
			c[i].a=((s1[0]-'0')*10+s1[1]-'0')*60+(s1[3]-'0')*10+s1[4]-'0';
			c[i].b=((s2[0]-'0')*10+s2[1]-'0')*60+(s2[3]-'0')*10+s2[4]-'0';
			c[i].f=true;
		}
		sort(c,c+n,com);
		na=nb=n1=n2=0;
		for(i=0;i<n;i++)
		{
			if(!c[i].f)
			{
				for(j=0;j<na;j++)
					if(a[j]<=c[i].a)
					{
						k=j;
						break;
					}
				if(j==na)
				{
					b[nb++]=c[i].b+tt;
					n1++;
				}
				else
				{
					b[nb++]=c[i].b+tt;
					for(j;j<na-1;j++)
					{
						a[j]=a[j+1];
					}
					na--;
				}
			}
			else
			{
				for(j=0;j<nb;j++)
					if(b[j]<=c[i].a)
					{
						k=j;
						break;
					}
				if(j==nb)
				{
					a[na++]=c[i].b+tt;
					n2++;
				}
				else
				{
					a[na++]=c[i].b+tt;
					for(j;j<nb-1;j++)
					{
						b[j]=b[j+1];
					}
					nb--;
				}
			}
		}
		printf("%d %d\n",n1,n2);
	}

	return 0;
}