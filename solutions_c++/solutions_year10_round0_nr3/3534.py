# include<cstdio>

int main()
{
	int t;
	scanf("%d",&t);
	int T=1;
	while(T<=t)
	{
		int R,k,N;
		scanf("%d %d %d",&R,&k,&N);
		int* groups=new int [N];
		for(int i=0;i<N;i++)
			scanf("%d",&groups[i]);

		int start=0,end=0,euros=0;		
		for(int i=0;i<R;i++)
		{
			int count=0;
			bool flag=false;
			while(1)
			{
				count+=groups[end];
				if(count>k || (flag==true && start==end))
				{
					count-=groups[end];					
					break;
				}
				flag=true;
				end=(end+1)%N;
			}
			start=end;			
			euros+=count;
		}
		printf("Case #%d: %d\n",T,euros);
		T++;
	}
}