#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
using namespace std;
int T,Ti,da;
long long n;

int gcd(int a,int b)
{
	if(a==0)return b;
	return gcd(b%a,a);
}

int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,a,b,c,d,j,k,z;
    
    int ra,rb;
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		scanf("%lld%d%d",&n,&ra,&rb);
//		cout<<n<<' '<<ra<<' '<<rb<<endl;
		
//		cout<<ra<<' '<<gcd(ra,100)<<endl;
		
		if(ra==0)
		{
			if(rb==100)
			{
				printf("Broken\n");
				continue;
			}
			printf("Possible\n");
			continue;
		}		
		
		if(rb==100 && ra!=100 || rb==0 && ra!=0)
		{
			printf("Broken\n");
			continue;
		}
		
		ra=100/gcd(ra,100);	
		
		if(n<ra)
		{
			printf("Broken\n");
			continue;
		}
		
		
		
		printf("Possible\n");
	}	
    return 0;
}
