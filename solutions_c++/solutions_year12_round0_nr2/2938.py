#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int rem0,rem1,rem2;
	int a[100],b[100],c,p,t,N,S,T;
	scanf(" %d",&T);
	for(int t = 1; t <= T; ++t)
	{
		rem0 = rem1 = rem2 = c = 0;
		scanf("%d%d%d",&N,&S,&p);
		for(int i=0; i<N; i++)
		{
			scanf("%d",&a[i]);
			switch(a[i]%3)
			{
				case 0 : rem0++; b[i] = a[i]/3; break;
				case 1 : rem1++; b[i] = a[i]/3+1; break;
				case 2 : rem2++; b[i] = a[i]/3+1; break;
			}
			if(b[i]>=p)
				c++;
		}
		for(int i=0,ctr=0; ctr<S && i<N; i++)
		{
			if(b[i] == p-1 && a[i]>=2 && a[i]%3 != 1)
			{
				c++;
				ctr++;
			}
		}
		printf("Case #%d: %d\n",t,c);
	}
	return 0;
}
