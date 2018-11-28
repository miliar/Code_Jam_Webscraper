#include <iostream>

int main()
{
	//freopen("../input.in","r",stdin);
	//freopen("../output.out","w",stdout);

	unsigned int T,R,K,N,*g,k,mutex,sum,sum_tmp,total;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		total=0;
		scanf("%d",&R);
		scanf("%d",&K);
		scanf("%d",&N);
		g=new unsigned int[N];
		for(int j=0;j<N;j++)
			scanf("%d",&g[j]);
		k=0;
		for(int j=0;j<R;j++)
		{
			mutex=0;
			sum=0;
			sum_tmp=0;
			while(1)
			{
				sum=sum_tmp;
				sum_tmp+=g[k%N];
				mutex++;
				if(sum_tmp>K||mutex>N)break;
				else k++;
			}
			total+=sum;
		}
		printf("Case #%d: %d\n",i,total);
		delete [] g;
	}

	return 0;
}