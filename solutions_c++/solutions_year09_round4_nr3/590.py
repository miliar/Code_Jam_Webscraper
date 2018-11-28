#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int data[200][200];
int graph[200][200];
int ans,im;
int todo[200];
void permute(int c)
{
	if(c==im)
	{
		int c,n,m,d;
		c=0;
		for(n=0;n<im;n++)
		{
			c+=todo[n];
		}
		if(c<=ans)
			return;
		d=0;
		for(n=0;n<im;n++)
		{
			for(m=0;m<im;m++)
			{
				if(todo[n]==1&&todo[m]==1&&graph[n][m]==0)
					continue;
				d++;
			}
		}
		if(d==im*im)
			ans=c;
		return;
	}
	todo[c]=0;
	permute(c+1);
	todo[c]=1;
	permute(c+1);
}
int main()
{
	int in,io,n,m,o,p,eq;
	scanf("%d",&in);
	for(n=0;n<in;n++)
	{
		scanf("%d %d",&im,&io);
		for(m=0;m<im;m++)
			for(o=0;o<im;o++)
				graph[m][o]=0;
		for(m=0;m<im;m++)
			for(o=0;o<io;o++)
				scanf("%d",&data[m][o]);
		for(m=0;m<im;m++)
			for(o=0;o<im;o++)
			{
				if(data[m][0]==data[o][0])
				{
					graph[m][o]=1;
					graph[o][m]=1;
					continue;
				}
				if(data[m][0]>data[o][0])
				{
					for(p=0;p<io;p++)
					{
						if(data[m][p]<=data[o][p])
							break;
					}
					if(p!=io)
					{
					graph[m][o]=1;
					graph[o][m]=1;
					continue;
					}
					
				}
				if(data[o][0]>data[m][0])
				{
					for(p=0;p<io;p++)
					{
						if(data[o][p]<=data[m][p])
							break;
					}
					if(p!=io)
					{
					graph[m][o]=1;
					graph[o][m]=1;
					continue;
					}
				}
			}
		/*for(m=0;m<im;m++)
		{
			for(o=0;o<im;o++)
			{
				printf("%d",graph[m][o]);
				
			}
			printf("\n");
		}*/
		ans=-999;
		permute(0);
		//if(ans<=1)
		//	ans=1;
		printf("Case #%d: %d\n",n+1,ans);
	}
	return 0;
};
