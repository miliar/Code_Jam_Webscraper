#include<iostream>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
int gcd(int a,int b)
{
	if(a%b==0)
		return b;
	return gcd(b,a%b);
}
int main()
{
	freopen("n.txt","w",stdout);
	int t,i,j;
	long long n;
	int pd,pg;
	int ga,k;
	cin>>t;
	int id;
	for(id=1;id<=t;id++)
	{
		scanf("%lld%d%d",&n,&pd,&pg);
		if(pd>0)
	    {
				ga=gcd(100,pd);
		        k=100/ga;
		}
		else
			k=0;
		printf("Case #%d: ",id);
		if(k<=n&&pg<=max(pd,99)&&pg>=min(1,pd))
			puts("Possible");
		else
			puts("Broken");
	}
	return 0;
}