long long GCD(long long a, long long b)
{
	long long v;

	if (a < b) { v = a; a = b; b = v; }
	
	while (b > 0)
	{
		v = b;
		b = a % b;
		a = v;
	}

	return a;
}

//And GCD for all...
long long GCD4all(long long* arr, int len)
{
	int i;
	int result = arr[0];
	for (i = 1; i < len; i++)
	{
		result = GCD(result, arr[i]);
	}
	return result;
}

#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	int c;
	scanf("%d", &c);

	int n;
	long long t[1000]; 
	int i;
	int j;
	long long d;

	for (i = 1; i<=c; i++)
	{
		//Scanning
		scanf("%d", &n);
		for (j = 0; j < n; j++)
			scanf("%lld", t+j);
		
		//Sorting
		random_shuffle(t, t+n);
		sort(t, t+n);

		//Calculating difference between 2 nearest numbers for all t[i]
		for (j = n-1; j > 0; j--)
			t[j] = t[j] - t[j-1];

		//Calculating GCD for differences (t[0] is a member of orginal t[i])
		d = GCD4all(t+1, n-1);

		//Calculating answer
		if (*t % d == 0) d = 0; else d = d - *t % d;
		
		//Printing answer
		printf("Case #%d: %d\n", i, d);
	}
}