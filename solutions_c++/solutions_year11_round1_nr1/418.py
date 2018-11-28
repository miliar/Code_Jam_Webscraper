#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;
long long gcd(long long a,long long b)
{
	        if(b==0)
			                return a;
		        else return gcd(b,a%b);
}


int main()
{
	int t;	
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		long long n,pd,pg;
		cin>>n>>pd>>pg;
		if(pd>0 && pg==0 || pd !=100 && pg==100)
			printf("Case #%d: Broken\n",k);
		else
		{
			if (100/gcd(100,pd)<=n)
				printf("Case #%d: Possible\n",k);
			else
				printf("Case #%d: Broken\n",k);
		}
					
	}	
	return 0;
}
