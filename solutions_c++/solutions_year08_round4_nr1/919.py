#include <stdio.h>

int min(int a, int b)
{
	return a>b?b:a;
}

int main()
{
	bool ch[10000];
	int dyn[10000][2],ver[10000];
	int n1,n2,n3,n4,N,M,G,C,V;
	freopen("A-small.in","r",stdin);
	freopen("out.in","w",stdout);
	
	scanf("%d",&N);
	for(int z=0;z<N;z++)
	{
		for(int i=0;i<10000;i++)
	{
		ch[i]=false;
		dyn[i][0]=dyn[i][1]=100000000;
	}
		scanf("%d%d",&M,&V);
		for(int i=0;i<(M-1)/2;i++)
		{
			scanf("%d%d",&G,&C);
			ver[i]=G;
			if(C==1) ch[i]=true;
		}
		
		for(int i=(M-1)/2;i<M;i++)
		{
			scanf("%d",&G);
			ver[i]=G;
			dyn[i][ver[i]]=0;
			
		}
		
		for(int i=(M-1)/2-1;i>=0;i--)
		{
			n1=n2=n3=n4=100000000;
			if(ver[i]==1)
			{
				if((dyn[2*i+1][1]!=100000000)&&(dyn[2*i+2][1]!=100000000))
				{
					n1=dyn[2*i+1][1]+dyn[2*i+2][1];
				}
				if((dyn[2*i+1][0]!=100000000)||(dyn[2*i+2][0]!=100000000))
				{
					n2=min(dyn[2*i+1][0],dyn[2*i+2][0]);
				}
			}
			else if(ver[i]==0)
			{
				if((dyn[2*i+1][1]!=100000000)||(dyn[2*i+2][1]!=100000000))
				{
					n1=min(dyn[2*i+1][1],dyn[2*i+2][1]);
				}
				if((dyn[2*i+1][0]!=100000000)&&(dyn[2*i+2][0]!=100000000))
				{
					n2=dyn[2*i+1][0]+dyn[2*i+2][0];
				}
			}
			
			if(ch[i])
			{
				if(ver[i]==1)ver[i]=0;
				else ver[i]=1;
				if(ver[i]==1)
				{
					if((dyn[2*i+1][1]!=100000000)&&(dyn[2*i+2][1]!=100000000))
					{
						n3=dyn[2*i+1][1]+dyn[2*i+2][1]+1;
					}
					if((dyn[2*i+1][0]!=100000000)||(dyn[2*i+2][0]!=100000000))
					{
						n4=min(dyn[2*i+1][0],dyn[2*i+2][0])+1;
					}
				}
				else if(ver[i]==0)
				{
					if((dyn[2*i+1][1]!=100000000)||(dyn[2*i+2][1]!=100000000))
					{
						n3=min(dyn[2*i+1][1],dyn[2*i+2][1])+1;
					}
					if((dyn[2*i+1][0]!=100000000)&&(dyn[2*i+2][0]!=100000000))
					{
						n4=dyn[2*i+1][0]+dyn[2*i+2][0]+1;
					}
				}
			}
			dyn[i][1]=min(n1,n3);
			dyn[i][0]=min(n2,n4);
		}
		if(dyn[0][V]!=100000000){
			printf("Case #%d: %d\n",z+1,dyn[0][V]);
		}
		else printf("Case #%d: IMPOSSIBLE\n",z+1);
	}
	return 0;
}

