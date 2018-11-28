#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int gcd(int a,int b)
{
	while(b!=0)
	{
		int tmp=b;
		b=a%b;
		a=tmp;
	}
	return a;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,Pd,Pg;
	long long N;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		cin>>N>>Pd>>Pg;
		printf("Case #%d: ",t);
		if(Pd!=100&&Pg==100)
		{
			printf("Broken\n");
			continue;
		}
		if(Pd!=0&&Pg==0)
		{
			printf("Broken\n");
			continue;
		}
		if(100/gcd(Pd,100)<=N)
			printf("Possible\n");
		else
			printf("Broken\n");
		
	}
	return 0;
}
