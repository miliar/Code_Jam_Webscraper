#include <iostream>
#include <algorithm>
using namespace std;

int t, n, a[1000], b[1000];
int main()
{
	scanf("%d", &t);
	int ca=1;
	while(t--)
	{
		scanf("%d", &n);
		for(int i=0; i<n; i++)
			scanf("%d", &a[i]);
		for(int j=0; j<n; j++)
			scanf("%d", &b[j]);
		sort(a, a+n);
		sort(b, b+n);
		long long int sum=0;
		for(int i=0; i<n; i++)
				sum+=a[i]*b[n-i-1];
		printf("Case #%d: %d\n", ca++, sum);
	}
	return 0;
}