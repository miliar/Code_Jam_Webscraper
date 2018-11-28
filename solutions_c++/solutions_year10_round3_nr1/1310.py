#include <iostream>
#define NUM 1005
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    //freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	int testcase,n;
	int A[NUM],B[NUM];
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
		    scanf("%d%d",&A[i],&B[i]);
		}
		int m=0;
		for(int i=1;i<n;i++)
		{
		    for(int j=i-1;j>=0;j--)
		    {
		        if((A[i]<A[j]&&B[i]>B[j])||(A[i]>A[j]&&B[i]<B[j]))
                    m++;
		    }
		}

        printf("%d\n",m);
		fflush(stdout);
	}
	return 0;
}
