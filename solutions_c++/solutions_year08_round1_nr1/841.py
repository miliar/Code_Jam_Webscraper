#include "iostream"
#include <stdlib.h>

using namespace std;

int main()
{
	int T;
	scanf("%d\n",&T);
	int v1[800];
	int v2[800];
	for (int c = 0; c < T; c++)
	{
		long int ret = 0;
		int n;
	
		scanf("%d\n",&n);
		for (int j =0; j < n; j++)
			scanf("%d ",&(v1[j]));
		scanf("\n");
		for (int j =0; j < n; j++)
			scanf("%d ",&(v2[j]));
		scanf("\n");
		sort(v1,v1+n);
		sort(v2,v2+n);
		for (int j =0; j < n; j++)
			ret += v1[j]*v2[n-1-j];
		printf("Case #%d: %ld\n",c+1,ret);
	}
	return 0;
}
