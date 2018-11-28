#include<stdio.h>
#include<bitset>
#define MAX 2000000
using namespace std;
main()
{
	bitset<MAX+1> s;
	int t,c,a,b,d,i,j,k,n;
	scanf("%d",&t);
	for(c=1;c<=t;c++)
	{
		scanf("%d %d",&a,&b);
		for(d=1;d<=a;d*=10);
		d/=10;
		s.reset();
		for(i=a,k=0;i<=b;i++)
		{
			n=i;
			j=0;
			while(n>MAX || s[n]==0)
			{
				if(n<=MAX) s[n]=1;
				if(a<=n && n<=b) j++;
				n=(n%10)*d + n/10;
			}
			k+=j*(j-1)/2;
		}
		printf("Case #%d: %d\n",c,k);
	}
}
