#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

int a[1005];

int main()
{
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		int n;
		scanf("%d",&n);
		int s=0;
		for (int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			s^=a[i];
		}
		
		if (s!=0) printf("Case #%d: NO\n",test);
		else
		{
			sort(a,a+n);
			s=0;
			for (int i=1;i<n;++i)
				s+=a[i];
			printf("Case #%d: %d\n",test,s);
		}
	}
	return 0;
}
