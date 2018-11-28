//#pragma comment(linker,"/STACK:256000000")
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <math.h>
#include <set>
#include <map>
using namespace std;

int gcd (int a, int b) {
	while (b) {
		a %= b;
		swap (a, b);
	}
	return a;
}

int main()
{
	//freopen("1.txt","rt",stdin);
	//freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-large.in","rt",stdin);
	//freopen("OutSmallA.txt","wt",stdout);
	freopen("OutLargeA.txt","wt",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int pd,pg;
		long long n;
		cin>>n>>pd>>pg;
		int u,u1,a1,b1,u2,a2,b2,k11,k12,k21,k22;
		
		if(pd!=100 && pd!=0)
		{
			int u=gcd(pd,100);
			if(long long(100/u)>n)
			{
				printf("Case #%d: Broken\n",i);
				continue;
			}
		}			
		if(pg==0)
		{
			if(pd==0)
				printf("Case #%d: Possible\n",i);
			else
				printf("Case #%d: Broken\n",i);
			continue;
		}
		if(pg==100)
		{
			if(pd==100)
				printf("Case #%d: Possible\n",i);
			else
				printf("Case #%d: Broken\n",i);
			continue;
		}
		if(pd==100 || pd==0)
		{
			printf("Case #%d: Possible\n",i);
			continue;
		}
printf("Case #%d: Possible\n",i);
		/*if(pd<pg)
		{
			if(b1*k11*a2>=a1*b2*k11)
				printf("Case #%d: Possible\n",i);
			else
				if(b1*k12*a2>=a1*b2*k12)
				printf("Case #%d: Possible\n",i);
			else
				printf("Case #%d: Broken\n",i);
		}
		else
		{
			
			if(b2*k11*a1>=a2*b1*k11)
				printf("Case #%d: Possible\n",i);
			else
				if(b2*k12*a1>=a2*b1*k12)
				printf("Case #%d: Possible\n",i);
			else
				printf("Case #%d: Broken\n",i);
		}*/
	}





			



fclose(stdout);
}