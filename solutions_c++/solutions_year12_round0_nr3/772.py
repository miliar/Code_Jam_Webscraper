#include <iostream>
#include <set>
using namespace std;

int was[2000005];

void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int ntest=1;
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		int a,b;
		int ans=0;
		scanf("%d%d",&a,&b);
		int D=1;
		while (D<=b)
		{
			D*=10;
		}
		D/=10;
		int I=i*10000000;
		for (int j=a;j<b;j++)
		{
			int h=j;
			for (int g=0;g<7;g++)
			{
				int d=h%10;
				h/=10;
				h+=d*D;
				if (h>j && h<=b && was[h]!=I+j)
				{
					was[h]=I+j;
					ans++;
				}
			}
		}
		printf("Case #%d: %d",ntest++,ans);
		cout<<endl;
	}
}