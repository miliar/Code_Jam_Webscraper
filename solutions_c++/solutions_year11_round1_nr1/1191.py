#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

int GCD(int num1,int num2)
{
    int t;
    if (num2>num1)
    {
        t=num2;
        num2=num1;
        num1=t;
    }
	if(num2 == 0)
		return 1;
    while ((t=(num1%num2))!=0)
    {
        num1=num2;
        num2=t;
    }
    return num2;
}

int main()
{
	//freopen("e:\\A-small.in", "r", stdin);	//freopen("e:\\A-small.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		long long N;
		int PD,PG;
		scanf("%lld %d %d",&N,&PD,&PG);
		int x1=0,x2=0,y1=0,y2=0;
		int gcd1=GCD(100,PD);
		x1=100/gcd1;
		x2=PD/gcd1;
		int flag=0;
		if(x1 <= N)
			flag=1;
		if((PG == 0)||(PD == 0))
		{
			if((PG == 0)&&(PD == 0))
				flag=1;
			else
				flag=0;
		}
		if((PG == 100)||(PD == 100))
		{
			if((PG == 100)&&(PD == 100))
				flag=1;
			else
				flag=0;
		}
		printf("Case #%d: ",i+1);
		if(flag == 1)
			printf("Possible\n");
		else
			printf("Broken\n");
		
	}
	return 0;
}