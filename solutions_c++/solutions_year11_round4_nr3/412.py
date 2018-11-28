#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const __int64 maxn=1000005;
__int64 primes[maxn*10];
int cnt;
void makePrimes()
{
    __int64 i, j;
    int num=maxn;
    primes[0] = 2;
    primes[1] = 3;
    
    for(i = 5, cnt = 2; cnt < maxn; i += 2)
    {
        int flag = true;
        for(j = 1; primes[j]*primes[j] <= i; ++j)
        {
            if(i%primes[j] == 0)
            {
                flag = false; break;
            }
        }
        if(flag) primes[cnt++] = i;
		if (i>maxn) return ;
    }
}

int main()
{
    makePrimes();
	int cas;
	int ca=0;
	__int64 x,Max,Min,y,j,a,M;
	int i;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
	Max=1;
		scanf("%I64d",&x);
		if (x==1) M=0;
		else
		{
			M=1;
		for (i=0;i<cnt;i++)
		{
			y=1;
			j=0;
			a=primes[i];
			while (y*a<=x)
			{
				y=y*a;
				j++;
			}
			if (j>=1)
			M+=j-1;
		}
		}
		ca++;
		printf("Case #%d: %I64d\n",ca,M);
	}
return 0;
}