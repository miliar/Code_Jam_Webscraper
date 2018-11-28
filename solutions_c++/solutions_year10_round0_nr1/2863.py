#include <iostream>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    //freopen("1.txt","r",stdin);freopen("2.txt","w",stdout);
	int testcase,n,k;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d",&n,&k);
		int x=1;
		for(int i=1;i<n;i++)
		{
		    x=x<<1;
		    x+=1;
		}
		int y=k&x;
		if(y==x)
		    printf("ON\n");
        else
            printf("OFF\n");
		fflush(stdout);
	}
	return 0;
}
