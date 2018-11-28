#include<stdio.h>
#include<string.h>
const int N = 100+10;
int a[N];
int main()
{

	freopen("C-small-attempt0 (1).in","r",stdin);
	freopen("C-out.out","w",stdout);
	int T;
	scanf("%d",&T);
	
	int cases;
	for(cases=1;cases<=T;cases++)
	{
		int n,l,h;
		scanf("%d%d%d",&n,&l,&h);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		printf("Case #%d: ",cases);
		int ans;
		for(ans = l;ans<=h;ans++)
		{
			for(i=0;i<n;i++)
			{
				if(a[i]==0||ans%a[i]==0||a[i]%ans==0)
					continue;
				else
					break;
			}

			if(i==n)break;
		}
		if(ans<=h)
		printf("%d\n",ans);
		else
			printf("NO\n");
		//printf("Case #%d: %.6lf\n",cases,double(ans));
      
	}
	return 0;
}