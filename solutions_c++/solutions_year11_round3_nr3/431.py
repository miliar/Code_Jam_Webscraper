#include <stdio.h>

#define MAX 110

int main()
{
	int t,ccnt;

	int l,h;
	int n;
	int f[MAX];
	int i,j;

	scanf("%d",&t);

	for(ccnt=1;ccnt<=t;++ccnt)
	{
		scanf("%d %d %d",&n,&l,&h);

		for(i=0;i<n;++i)
			scanf("%d",&f[i]);

		for(i=l;i<=h;++i)
		{
			for(j=0;j<n;++j)
			{
				if(f[j]>i && f[j]%i)
					break;
				if(f[j]<i && i%f[j])
					break;
			}
			if(j==n)
				break;
		}

		printf("Case #%d: ",ccnt);

		if(i>h)
			printf("NO\n");
		else
			printf("%d\n",i);
	}
	return 0;
}

