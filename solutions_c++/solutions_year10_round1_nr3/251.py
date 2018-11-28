#include <iostream>
using namespace std;

int d,i,j,m,n,x,y,t,c,a1,a2,b1,b2;
int f[1000001],l,r;
__int64 k;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	for (i=1; i<=1000000; i++)
	{
		l=i; r=2*i;

		while (l+1<r)
		{
			m=(l+r)/2;
			x=i; y=m;
			c=0;
			while (x!=y)
			{
				y-=x;
				if (x>y) swap(x,y);
				if (2*x<=y) break;
				c++;
			}			
			if (c%2==1) r=m; else l=m;
		}
		f[i]=r;
	}

	scanf("%d",&t);
	for (m=1; m<=t; m++)
	{
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		k=0;
        for (i=a1; i<=a2; i++)
        {
            if (f[i] < b1) k += b2 - b1 + 1;
            else if (f[i] <= b2) k += b2 - f[i] + 1;
        }
        for (i=b1; i<=b2; i++)
        {
            if (f[i] < a1) k += a2 - a1 + 1;
            else if (f[i] <= a2) k += a2 - f[i] + 1;
        }
		printf("Case #%d: ",m);
		printf("%I64d\n",k);
	}
	
//	system("pause");
	return 0;
}
