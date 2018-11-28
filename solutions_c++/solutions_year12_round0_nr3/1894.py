#include <stdio.h>
#include <algorithm>
using namespace std;

int TC,tc;
int a,b,n,m,l[100];
int d,f,t;

int main()
{
	int i;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	for(scanf("%d",&TC),tc=1;tc<=TC;++tc)
	{
		scanf("%d%d",&a,&b);
		for(d=0,f=1,i=a/10;i;i/=10,++d,f*=10);
		t=0;
		for(n=a;n<=b;++n)
		{
			for(m=n,i=0;i<d;++i)
			{
				m=m/10+(m%10)*f;
				l[i]=m;
			}
			sort(l,l+d);
			for(i=0;i<d;++i)
			{
				if((i==0||l[i]!=l[i-1]) && n<l[i]&&a<=l[i]&&l[i]<=b)
				{
					++t;// printf("%d %d\n",n,m);
				}
			}
		}
		printf("Case #%d: %d\n",tc,t);
	}
	return 0;
}