#include <iostream>

using namespace std;

int n,p1,p2;

bool check()
{
	scanf("%d%d%d",&n,&p1,&p2);
	if (p2==0 && p1!=0) return false;
	if (p2==100 && p1!=100) return false;
	if (n<100)
	{
		for (int i=1;i<=n;i++)
			if ((i*p1)% 100 ==0) return true;
		return false;
	}
	return true;
}


int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d: ",cc);
		if (check()) printf("Possible\n");
			else printf("Broken\n");
	}
}
