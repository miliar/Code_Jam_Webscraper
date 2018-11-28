#include <iostream>
#include <algorithm>
using namespace std;

int n, p, k, l;
int ll[1008];

int main()
{
	cin>>n;
	int ca=1;
	while(n--)
	{
		cin>>p>>k>>l;
		for(int i=0; i<l; i++)
			cin>>ll[i];
		sort(ll, ll+l);
		int nn=1;
		long long int sum=0;
		int i=0;
		while(i<l)
		{
			if(i!=0 && i%k==0)
				nn++;
			sum+=ll[l-i-1]*nn;
			i++;
		}
		printf("Case #%d: %I64d\n", ca++, sum);

	}
	return 0;
}