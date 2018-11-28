#include <stdio.h>
#include <algorithm>
#include <memory.h>
//#define NDEBUG
#include <assert.h>
using namespace std;
typedef long long int llint;
#define N 802
llint X[N],Y[N];
int main()
{
	int t,n,ca=1;
	for(scanf("%d",&t);t--;)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%lld",X+i);
		for(int i=0;i<n;i++)scanf("%lld",Y+i);
		sort(X,X+n);
		sort(Y,Y+n);
		llint ans=0;
		for(int i=0;i<n;i++)
			ans+=(llint)X[i]*(llint)Y[n-1-i];
		printf("Case #%d: %lld\n",ca++,ans);
	}
	return 0;
}
