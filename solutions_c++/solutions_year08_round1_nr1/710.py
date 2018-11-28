#include <stdio.h>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int a[100002] ,b[100002];
int ncase;
int n;
long long sum;

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-small.sol","w",stdout);
	int i ,j ,x;
	scanf("%d",&ncase);
	for(x=1;x<=ncase;x++) { // x is input number
		scanf("%d",&n);
		for(i=0;i<n;i++) 
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%d",&b[i]);
		sort(a , a+n);
		sort(b , b+n);
		sum = 0;
		for(i=0;i<n;i++)
			sum += a[i] * b[n-1-i];
		printf("Case #%d: %lld\n",x,sum);
	}
	return 0;
}
