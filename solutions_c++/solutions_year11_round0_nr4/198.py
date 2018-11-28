#include <iostream>

using namespace std;

int num[2000],n,ans;

void doing()
{
	scanf("%d",&n); ans=n;
	for (int i=1;i<=n;i++) 
	{
		scanf("%d",&num[i]);
		if (num[i]==i) ans--;
	}
	printf("%.6lf\n",(double)ans);
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		doing();
	}
}
