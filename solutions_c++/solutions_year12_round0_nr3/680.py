#include <iostream>
#include <cstdio>
using namespace std;
int t,a,b,g,i,x,y;
long long ans;
int po(int x,int y)
{
	int ret=1,i;
	for(i=1;i<=y;i++) ret*=x;
	return ret;
}
int LG(int x)
{
	if(x<10)return 1;
	return 1+LG(x/10);
}
int L(int x,int n)
{
	return x/10+(x%10)*po(10,n-1);
}
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	for(g=1;g<=t;g++)
	{
		ans=0;
		scanf("%d%d",&a,&b);
		for(x=a;x<=b;x++)
		{
			for(y=L(x,LG(x));x!=y;y=L(y,LG(x)))
				if((LG(x)==LG(y))&&(a<=y)&&(y<=b))
					ans++;
		}
		//printf("%d %d\n",LG(12),LG(21));
		printf("Case #%d: %I64d\n",g,ans/2);
	}
	return 0;
}
