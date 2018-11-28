#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#define MAXL 55
using namespace std;

long long int GCD(long long int x,long long int y)
{
	if(x == 0)
		return y;
	else if(y == 0)
		return x;
	if(x >=y)
		return GCD(x-y,y);
	else
		return GCD(x,y-x);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	long long int N;
	int T;
	long long int PD,PG;
	int x;
	scanf("%d",&T);
	long long int a,b;
	int c,d;
	long long int temp;
	int i,j;
	int t = 0;
	while(T--)
	{
		//scanf("%d %d",&a,&b);
		//printf("%d",GCD(a,b));
		
		scanf("%lld %lld %lld",&N,&PD,&PG);
		if(PG == 0)
		{
			if(PD == 0)
				printf("Case #%d: Possible\n",++t);
			else
				printf("Case #%d: Broken\n",++t);
		}
		else if(PG == 100)
		{
			if(PD == 100)
				printf("Case #%d: Possible\n",++t);
			else
				printf("Case #%d: Broken\n",++t);
		}
		else
		{
			temp = GCD(PD,100);
			a = PD / temp;
			b = 100 / temp;
			if(b <= N)	
				printf("Case #%d: Possible\n",++t);
			else
				printf("Case #%d: Broken\n",++t);
		}
	
		
	}
	return 0;
}
