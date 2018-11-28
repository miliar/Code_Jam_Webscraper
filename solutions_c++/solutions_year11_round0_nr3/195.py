#include <iostream>

using namespace std;

int n;

void doing()
{
	scanf("%d",&n);
	int sum1=0,sum2=0,k,ret=0x7fffffff;
	for (int i=0;i<n;i++)
	{
		scanf("%d",&k);
		sum1+=k; sum2^=k;
		ret=min(ret,k);
	}
	if (sum2!=0) printf("NO\n"); 
	else
		printf("%d\n",sum1-ret);
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int casenum=1;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
