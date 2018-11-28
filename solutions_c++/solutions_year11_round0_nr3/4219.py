#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define SI ({int x;scanf("%d",&x);x;})

int a[1111], n;

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("C-output.out","w",stdout);

	int kk=SI;
	for(int k=1;k<=kk;k++)
	{
		n=SI;
		int sum=0,x=0;
		for(int i=0;i<n;i++)
		{
			a[i]=SI;
			sum+=a[i]; x^=a[i];
		}

		printf("Case #%d: ",k);

		if(x!=0) printf("NO\n");
		else printf("%d\n",sum-*min_element(a,a+n));
	}
	return 0;
}

