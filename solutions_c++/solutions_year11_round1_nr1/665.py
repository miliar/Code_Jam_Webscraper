#include "stdlib.h"
#include "stdio.h"
using namespace std;

long long int N;
int PD, PG;

void read_case()
{
	scanf("%lld %d %d\n",&N,&PD,&PG);
}

bool solve()
{
	int d,D(0);
	
	do
	{
		D++;
		d = PD*D/100;
	} while (PD*D != 100*d);
	
	//printf("%d of %d\n",d,D);
	
	if (D>N)
		return false;
		
	if (PG==100 && d<D)
		return false;
	
	if (PG==0 && d>0)
		return false;
		
	return true;
}

int main()
{
	int T;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++)
	{
		read_case();
		printf("Case #%d: ",i+1);
		solve() ? printf("Possible\n") : printf("Broken\n");
	}
	return 0;
}
