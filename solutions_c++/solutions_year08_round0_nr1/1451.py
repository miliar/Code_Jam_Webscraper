#include<stdio.h>
#include<string.h>
#define SIZE 1100


struct search
{
	char eng[1000];
	int st;
	int end;
}engine[SIZE ];

struct query
{
	char q[1000];
}content[SIZE ];

void update(int n_s,int n_q,int index)
{
	int i,j;
	for(i=0;i<n_s;i++)
	{
		for(j=index+1;j<n_q;j++)
		{
			if(strcmp(engine[i].eng,content[j].q) == 0)
			{
				engine[i].st = index+1;
				engine[i].end = j-1;
				break;
			}
		}
		if(j>=n_q)
		{
			engine[i].st = index+1;
			engine[i].end = j-1;	
		}
	}

}

int choose(int n_s)
{
	int i,max,j;
	max = engine[0].end;
	j = 0;
	for(i=1;i<n_s;i++)
	{
		if(engine[i].end > max)
		{
			max = engine[i].end;
			j = i;
		}
	}
	return max;
}

int main(void)
{
	int t,n_s,n_q,i,count,j,end;
	
	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	scanf("%d",&t);
	
	
	for(i=1;i<=t;i++)
	{
		count = -1;
		scanf("%d%*c",&n_s);
		for(j=0;j<n_s;j++)
		{
			gets(engine[j].eng);	
		}
		scanf("%d%*c",&n_q);
		
		for(j=0;j<n_q;j++)
		{
			gets(content[j].q);	
		}

		end = -1;
		while(1)
		{
			update(n_s,n_q,end);
			end = choose(n_s);
			count++;
			if(end == n_q-1)	break;
		}
		printf("Case #%d: %d\n",i,count);
		
	}
	
	return 0;
}

