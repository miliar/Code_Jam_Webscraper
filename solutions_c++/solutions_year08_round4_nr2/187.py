#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

typedef struct pto
{
	int x,y;
} pto;

int ar (pto & a, pto & b, pto & c)
{
	return b.x*c.y+a.x*b.y+c.x*a.y
		-(b.x*a.y+a.x*c.y+c.x*b.y);
}

int main()
{
	int t,cnt;
	int n,m;
	int i,j,k,l;
	int A;
	pto a,b,c;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;++cnt)
	{
		scanf("%d %d %d",&n,&m,&A);
		a.x=0;a.y=0;
		printf("Case #%d: ",cnt);
		for(i=0;i<=n;++i)
			for(j=0;j<=m;++j)
			{
				b.x=i;
				b.y=j;
				for(k=0;k<=n;++k)
					for(l=0;l<=m;++l)
					{
						c.x=k;
						c.y=l;
						if(abs(ar(a,b,c))==A)
						{
							printf("%d %d %d %d %d %d\n",a.x,a.y,b.x,b.y,c.x,c.y);
							goto fim;
						}
					}
			}
		printf("IMPOSSIBLE\n");
fim:
		a.x=0;
	}
	return 0;
}





