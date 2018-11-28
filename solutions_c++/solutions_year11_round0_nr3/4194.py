#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    freopen("a.txt","r",stdin);
    freopen("D:/gcj/c-large.out","w",stdout);
	int cas,t=0,n,i,j;
	int a[1005],sum;
	scanf("%d",&cas);
	while(cas--)
	{
		sum=0;
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			sum^=a[i];
		}
		if(sum!=0)
		{
			printf("Case #%d: %s\n",++t,"NO");
			continue;
		}
		else
		{
			sort(a,a+n);
			sum=0;
			for(i=1;i<n;++i){
				sum+=a[i];
			}
			printf("Case #%d: %d\n",++t,sum);
		}
	}
	return 0;
}
