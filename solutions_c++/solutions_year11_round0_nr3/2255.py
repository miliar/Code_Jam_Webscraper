#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int n;

int main()
{
	freopen("in.txt","w",stdout);
	freopen("test.txt","r",stdin);
	int ca,i,x,z,tp,sum,mmin;
	while (scanf("%d",&ca)!=EOF)
	{
	for (z=1;z<=ca;z++)
	{
		scanf("%d",&n);
		printf("Case #%d: ",z);
		tp=0;
		sum=0;
		mmin=99999999;
		for (i=0;i<n;i++)
		{
			scanf("%d",&x);
			tp^=x;
			sum+=x;
			if (x<mmin)
				mmin=x;
		}
		if (tp!=0)
			printf("NO\n");
		else
			printf("%d\n",sum-mmin);
	}
	}
	return 0;
}