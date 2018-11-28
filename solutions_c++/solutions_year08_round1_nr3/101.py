#include <cmath>
#include <cstdio>

const double base = 3+sqrt(5.0);
int t,n;
int ans[] = {5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447,463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

int main()
{
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int i = 1;i <= t;++i)
	{
		scanf("%d",&n);
		//ans = 1;
		/*for(int j = 0;j < n;++j)
		{
			ans *= base;
			ans -= int(ans/1000)*1000;
		}*/
		printf("Case #%d: %03d\n",i,ans[n-1]);
	}
	return 0;
}