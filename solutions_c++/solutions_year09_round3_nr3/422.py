#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int im,io;
int ip[200];
int selecta[200];
int selected[200];
int simulate[200];
int ansmin;
int permute(int n)
{
	int m,o,p=0,po;
	if(n==io)
	{
		/*for(m=0;m<io;m++)
		{
			printf("%d ",ip[m]);
		}
		printf("\n");*/
		for(m=1;m<=im;m++)
		{
			simulate[m]=1;
		}
		for(o=0;o<io;o++)
		{
			po=p;
			for(m=selecta[o]+1;m<=im;m++)
			{
				if(simulate[m]==0)
					break;
				p++;
			}
			for(m=selecta[o]-1;m>=1;m--)
			{
				if(simulate[m]==0)
					break;
				p++;
			}
			//printf(":%d\n",p-po);
			simulate[selecta[o]]=0;
		}
		if(p<ansmin)
			ansmin=p;
		//printf("%d\n",p);
		return 0;
	}
	for(m=0;m<io;m++)
	{
		if(selected[m]==1)
			continue;
		selecta[n]=ip[m];
		selected[m]=1;
		permute(n+1);
		selected[m]=0;
	}
}
int main()
{
	int in,n,m;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		ansmin=999999999;
		scanf("%d %d",&im,&io);
		for(m=0;m<io;m++)
			scanf("%d",&ip[m]);
		permute(0);
		printf("Case #%d: %d\n",n+1,ansmin);
	}
}
