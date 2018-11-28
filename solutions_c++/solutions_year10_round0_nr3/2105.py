#include <stdio.h>

int main()
{
	int resultIndex[1000],indexLen,cycleStart;
	int t,r,k,n,g[1000],once[1000];
	int sum,caseNum;

	int i,j,p,q;
	int isCycle;

	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	scanf("%d",&t);

	for(caseNum=1;caseNum<=t;caseNum++)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%d",g+i);

		p=0;
		q=0;
		isCycle=0;
		indexLen=0;
		while((!isCycle)&&indexLen<r)
		{
			once[p]=0;	
			while(once[p]+g[q]<=k)
			{
				once[p]+=g[q];
				q++;
				q%=n;
				if(q==p)break;
			}
			
			resultIndex[indexLen++]=p;

			//check cycle
			for(j=0;j<indexLen;j++)
			{
				if(resultIndex[j]==q)
				{
					isCycle=1;
					cycleStart=j;
				}
			}
			p=q;

		}
	
		p=0;
		sum=0;
		while(r--)
		{
			if(p==indexLen)p=cycleStart;
			sum+=once[resultIndex[p]];
			p++;
		}

		



		printf("Case #%d: %d\n",caseNum,sum);
	}
	return 0;
}