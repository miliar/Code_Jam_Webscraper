#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int N = 1000+10;
int value[N];
int main()
{

//	freopen("D-large.in","r",stdin);
//	freopen("D-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	
	int cases;
	for(cases=1;cases<=T;cases++)
	{
		int n;
		scanf("%d",&n);
		int i;
		int total = 0;
		int ans= 0;
		for(i=1;i<=n;i++)
		{
			
			scanf("%d",&value[i]);
			if( i != value[i])
				ans ++;
		}
		printf("Case #%d: %.6lf\n",cases,double(ans));
      
	}
	return 0;
}