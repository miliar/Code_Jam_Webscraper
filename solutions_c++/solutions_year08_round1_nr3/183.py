#include <stdio.h>
#include <math.h>
#define r5 2.2360679774997896964091736687313 
typedef long long ll;
struct mtx
{
	ll a,b,c,d;
	mtx operator*(mtx obj)
	{
		mtx temp;
		temp.a=a*obj.a+b*obj.c;
		temp.b=a*obj.b+b*obj.d;
		temp.c=c*obj.a+d*obj.c;
		temp.d=c*obj.b+d*obj.d;
		return temp;
	}
};
int main()
{
	int t,T,N;
	scanf("%d",&T);
	int z[30]={5,27,143,751,935,
		   607,903,991,335,47,
		   943,471,55,447,463,
		   991,95,607,263,151,
		   855,527,743,351,135,
		   407,903,791,135,647};
	for (t=1;t<=T;t++)
	{
		scanf("%d",&N);
		printf("Case #%d: %03d\n",t,z[N-1]);
	}
	return 0;
}

