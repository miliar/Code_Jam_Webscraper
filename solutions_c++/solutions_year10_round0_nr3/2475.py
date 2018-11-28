#include  <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include<iostream.h>
int main()
{
//	freopen("A.in","r",stdin);
freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//freopen("A-small.in","r",stdin);freopen("A-small.ans","w",stdout);
	int testcase,R,k,N,groupsize[10],l2,index,sum,amount,index2;
    index=0,sum=0,amount=0,index2=0;

	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);

		scanf("%d%d%d",&R,&k,&N);

		for (l2=0;l2<N;l2++)
	      scanf("%d",&groupsize[l2]);


 for (l2=0;l2<R;l2++)
        {    sum=groupsize[index];
             index2=(index+N-1)%N;
            while((sum+groupsize[(index+1)%N])<=k && (index2!=index)){index++;index%=N;sum+=groupsize[index];}
            amount+=sum;index++;index%=N;
        }
        printf("%d\n",amount);
        amount=0;index=0;
	}



	return 0;
}
