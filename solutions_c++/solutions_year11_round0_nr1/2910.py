#include <stdio.h>

#define MAXN 101

typedef struct TASK 
{
	int order;
	int p;
	int flag;
}TASK;
TASK blue[MAXN],orange[MAXN];
int step_time(int);

int main()
{
	int t,n;
	int time = 0;
	int pos;
	int o,b,j,i;
	char r;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
		
	scanf("%d",&t);
	for(i = 1 ; i  <= t; i++)
	{
		scanf("%d",&n);
		for(j = 0; j < MAXN; j++)
			orange[j].order = blue[j].order = 0;
		for(j = 1,o = b = 0; j <= n; j++)
		{
			scanf(" %c %d",&r,&pos);

			if(r == 'O')
			{
				orange[o].order = j;
				orange[o].flag= 0;
				orange[o++].p = pos;
			}
			else
			{
				blue[b].order = j;
				blue[b].flag = 0;
				blue[b++].p = pos;

			}
		}
		time = step_time(n);
		printf("Case #%d: ",i);
		printf("%d\n",time);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

int step_time(int n)
{
	int i;
	char cur_r;
	int o = 0,b = 0;
	int time = 0;
	int cnt = 0;
	int curo = 1,curb = 1;
	

	for(i = 1; i <= n; i++)
	{
		cur_r = orange[o].order == i ? 'O' : 'B';
		
		while(1)
		{
			if(cur_r == 'O')
			{
				if(orange[o].flag)
					break;
				if(curo < orange[o].p)
					curo++;
				else if(curo > orange[o].p)
					curo--;
				else
					orange[o].flag++;
					
				if(curb < blue[b].p)
					curb++;
				else if(curb > blue[b].p)
					curb--;	
			}
			else
			{
				
				if(blue[b].flag)
					break;
				if(curb < blue[b].p)
					curb++;
				else if(curb > blue[b].p)
					curb--;
				else
					blue[b].flag++;
					
				if(curo < orange[o].p)
					curo++;
				else if(curo > orange[o].p)
					curo--;	
			}
			time++;
		}
		cur_r == 'O' ? o++ : b++;	
		cnt++;	
	}
	return time;
}
