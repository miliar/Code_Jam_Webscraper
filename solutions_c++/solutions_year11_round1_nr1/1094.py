#include<cstdio>
#include<algorithm>
#include<string.h>
#include<math.h>

using namespace std;
long long int gcd(long long int a,long long int b)
{
	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}
int main()
{
	int test,t=1;
	scanf("%d",&test);
	while(test--)
	{
		long long int i,check=0,j,x,y,z,a,b,g,flag=0;
		scanf("%lld %lld %lld",&y,&x,&g);
		if(g==0 && x>0)
			check=1;
		long long int c=gcd(x,100);
		z=x/c;
		long long int d=100/c;
		printf("Case #%d: ",t++);
		if(d<=y)
			flag=1;
		else
			flag=0;
		if(flag==1)
		{
			c=gcd(g,100);
			b=g/c;
			a=100/c;			
			if(b==a && z==d)
				flag=1;
			else if(b<a && z==d)
				flag=1;
			else if(b<a && z<d)
				flag=1;
			else
				flag=0;
		}
		if(flag==0 || check==1)	
			printf("Broken\n");
		else
			printf("Possible\n");		
	}
	return 0;
}
