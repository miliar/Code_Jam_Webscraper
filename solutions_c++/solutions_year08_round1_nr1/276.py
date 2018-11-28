#include <stdio.h>
#include <algorithm>


using namespace std;


#define MAX 1000

int main()
{
	long long int v1[MAX],v2[MAX];
	int ncases;
	int cnt;
	int n;
	long long int res;
	int i;
	scanf("%d",&ncases);
	for(cnt=1;cnt<=ncases;++cnt)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%lld",&v1[i]);
		for(i=0;i<n;++i)
			scanf("%lld",&v2[i]);
		sort(v1,v1+n);
		sort(v2,v2+n);

		res=0;
		
		for(i=0;i<n;++i)
			res+=v1[i]*v2[n-i-1];

		printf("Case #%d: %lld\n",cnt,res);
	}
	return 0;
}

