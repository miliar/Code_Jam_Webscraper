#include<iostream>
#include<stdio.h>

using namespace std;

bool cas()
{
	int i;
	int ar[] = {0, 0};
	int n, pd, pg;
	cin >> n >> pd >> pg;
	int tmp = pd;

	if (pd == 0 && pg != 100) return true;
	
	while (!(tmp & 1) && tmp) 
	{
		ar[0]++;
		tmp>>=1;
	}
	while (tmp % 5 == 0 && tmp)
	{
		ar[1]++;
		tmp /= 5;
	}

	int q = 1;

	for (i = ar[0]; i < 2; i++) q *= 2;
	for (i = ar[1]; i < 2; i++) q *= 5;
	
	if (q > n) return false;

	
	if (pg == 100 && pd != 100) return false;
	

	if (pg == 0 && pd != 0) return false;	


	return true;
}

int main()
{
	int t, i;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		if (cas())
			printf("Possible\n");
		else
			printf("Broken\n");
	}
	return 0;
}
