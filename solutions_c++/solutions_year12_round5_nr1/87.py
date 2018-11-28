#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int l[10000];
int p[10000];

int main()
{
	int _cn,_cc,i,j,k,n;
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%d",&n);
		for (i=0;i<n;++i) scanf("%d",l+i);
		for (i=0;i<n;++i) scanf("%d",p+i);
		printf("Case #%d: ",_cc);
		for (i=0;i<n;++i)
		{
			k=0;
			for (j=0;j<n;++j) if (p[j]>=0 && p[j]*l[k]>p[k]*l[j]) k=j;
			printf("%d ",k);
			p[k]=-1;
		}
		printf("\n");
	}
	return 0;
}
