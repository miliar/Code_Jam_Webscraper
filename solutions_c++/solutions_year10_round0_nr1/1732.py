#include <iostream>
using namespace std;
int t,n,k;
int a[31];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	a[1] = 2;
	int i;
	scanf("%d",&t);
	for(i=2;i<=30;i++)
	{
		a[i] = 2*a[i-1];
	}
	int case_t = 1;

	while(t--)
	{
		printf("Case #%d: ",case_t++);
		scanf("%d%d",&n,&k);
		if(k%a[n]!=a[n]-1)
			printf("OFF\n");
		else
			printf("ON\n");
	}
	return 0;
}
