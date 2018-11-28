#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

int t,n,l,h,d[1010];
int i,j,flag;

int gcd(int a,int b)
{
	if (a==0)return b;
	else return gcd(b%a,a);
}

int lcm(int a,int b)
{
	return a/gcd(a,b)*b;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for (i=0;i<n;i++)scanf("%d",&d[i]);
		if (l==1) i=1;
		else 
		for (i=l;i<=h;i++)
		{
			flag=1;
			for (j=0;j<n;j++)
				if (d[j]>1 && gcd(i,d[j])==1)flag=0;
			if (flag==1)break;
		}
		printf("Case #%d: ",id);
		if (i<=h)printf("%d\n",i);
		else printf("NO\n");
	}
	return 0;
}
