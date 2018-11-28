#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int t,tt;
long long n,k,kk,i;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

	scanf("%d",&tt);
	for (t=1; t<=tt; t++)
	{
		scanf("%I64d %I64d",&n,&k);
		kk=1;
		for (i=1; i<=n; i++)
			kk*=2;
		k++;
		printf("Case #%d: ",t);
		if (k%kk) printf("OFF\n");
		else	  printf("ON\n");
	}

    return 0;
}
