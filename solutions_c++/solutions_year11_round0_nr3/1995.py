
#include <cstdio>

int d[1010];

int main()
{
	int t,cs=0;
	scanf("%d",&t);
	while(cs++<t){
		int n;
		scanf("%d",&n);
		int sum=0,small=1<<30,res=0;
		for(int i=0;i<n;++i){
			int a;
			scanf("%d",&a);
			res ^= a;
			sum += a;
			if(small>a)small = a;
		}

		printf("Case #%d: ",cs);
		
		if(res)puts("NO");
		else printf("%d\n",sum-small);
	
	
	}

	return 0;
}
