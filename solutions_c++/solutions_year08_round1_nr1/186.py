#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<algorithm>
using namespace std;

int n;
__int64 a[1000];
__int64 b[1000];
int main()
{
	int i,test;
	__int64 j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(int T=1;T<=test;T++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%I64d",&a[i]);
		for(i=0;i<n;i++)
			scanf("%I64d",&b[i]);

		sort(a,a+n);
		sort(b,b+n);
		j=0;
		for(i=0;i<n;i++)
			j+=a[i]*b[n-i-1];
		printf("Case #%d: %I64d\n",T,j);
	}
	return 0;
}