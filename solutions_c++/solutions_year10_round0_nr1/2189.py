#include <stdio.h>

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);

	int n,k,t;
	int caseNum;

	scanf("%d",&t);

	for(caseNum=1;caseNum<=t;caseNum++)
	{
		scanf("%d %d",&n,&k);

		if(((k+1)%(1<<n))==0)
		{
			printf("Case #%d: ON\n",caseNum);
		}else
		{
			printf("Case #%d: OFF\n",caseNum);
		}
	}

	return 0;
}