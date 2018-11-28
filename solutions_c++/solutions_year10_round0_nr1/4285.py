# include<cstdio>

int main()
{
	int t;
	scanf("%d",&t);	
	int T=1;
	while(T<=t)
	{
		bool SnapperStatus[30]={false};
		int N, K;
		scanf("%d %d",&N,&K);
		
		int lastOn=0;
		for(int i=0;i<K;i++)
		{
			for(int j=0;j<N && j<=lastOn;j++)
			{
				SnapperStatus[j]=!SnapperStatus[j];
			}
				
			int k=0;
			for(;SnapperStatus[k]!=false;k++);
			lastOn=k;
		}
		printf("Case #%d: ",T);
		bool flag=false;
		for(int i=0;i<N;i++)
		{
			if(SnapperStatus[i]==false)
			{
				printf("OFF");
				flag=true;
				break;
			}
		}
		if(!flag)
			printf("ON");
		printf("\n");
		T++;
	}
}