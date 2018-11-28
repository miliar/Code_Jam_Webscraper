#include <stdio.h>
#include <algorithm>
using namespace std;

int f[1024];

int main()
{
	int n,p,k,l;
	int i,j,c;
	__int64 sum;

	scanf("%d",&n);
	for(c=1;c<=n;c++)
	{
		scanf("%d%d%d",&p,&k,&l);
		for(i=0;i<l;i++)
		{
			scanf("%d",f+i);
		}

		sort(f,f+l);
		sum=0;

		for(i=1;i<=p;i++)
		{
			for(j=1;j<=k;j++)
			{
				sum+=f[--l]*i;
				if(l==0) goto end;
			}
		}

end:
		if(l==0)
			printf("Case #%d: %I64d\n",c,sum);
		else
			printf("Case #%d: Impossible\n",c);
	}

	return 0;
}