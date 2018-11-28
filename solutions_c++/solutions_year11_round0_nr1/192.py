#include <iostream>
#include <stdio.h>
#define maxn 101

using namespace std;

int n,lca1,acl,tp,ans,n1,n2,p1,p2;
int a1[maxn],a2[maxn],goo[maxn];

void work(int k)
{
	int i, j, p;
	char re;
	ans=0,tp=0,lca1=0,acl=0,n1=1,n2=1,p1=1,p2=1;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		scanf(" %c %d",&re,&p);
		if(re=='O')
		{
			 goo[++tp]=2;
			 a2[++acl]=p;
		}
		else
		{
			goo[++tp]=1;
			a1[++lca1]=p;
		}
	}
	for(i=1;i<=tp;i++)
	{
		if(goo[i]==1)
		{
			while(p1!=a1[n1])
			{
				if(p1<a1[n1]) p1++;
				if(p1>a1[n1]) p1--;
				if(p2<a2[n2]) p2++;
				if(p2>a2[n2]) p2--;
				ans++;
			}
			if(p2<a2[n2]) p2++;
			if(p2>a2[n2]) p2--;
			n1++,ans++;}
		else
		{
			while(p2!=a2[n2])
			{
				if(p1<a1[n1]) p1++;
				if(p1>a1[n1]) p1--;
				if(p2<a2[n2]) p2++;
				if(p2>a2[n2]) p2--;
				ans++;
			}
			if(p1<a1[n1]) p1++;
			if(p1>a1[n1]) p1--;
			n2++,ans++;
		}
	}
	printf("Case #%d: %d\n",k,ans);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int k = 1 ; k <= T ; k++)
	{
		work(k);
	}
	scanf("%d",&n);
	return 0;
}
