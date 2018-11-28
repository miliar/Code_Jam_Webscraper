#include "stdio.h"

typedef struct order 
{
	char c[10];
	int loc;
};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t,n;
	order or[105];
	int curr_o,curr_b,tmp,tmp2;
	int res = 0;
	int id = 1;

	scanf("%d",&t);
	while(t--)
	{
		curr_o = curr_b = 1;
		res = 0;
		scanf("%d",&n);
		for(i = 0;i < n; i++)
		{
			scanf("%s%d",or[i].c,&or[i].loc);
		}

		for(i = 0;i < n ;i++)
		{
			if(or[i].c[0] == 'O')
			{
				tmp = or[i].loc - curr_o;
				if(tmp < 0)
					tmp = -tmp;
				tmp ++;
				res = res + tmp;
				curr_o = or[i].loc;
				//printf("O:%d",tmp - 1);

				//处理另外一个
				for(j = i + 1 ; j < n ; j++)
				{
					if(or[j].c[0] == 'B')
						break;
				}
				if(j < n)
				{
					if(or[j].loc > curr_b)
					{
						curr_b += tmp ;
						if(curr_b > or[j].loc)
							curr_b = or[j].loc;
						//printf("B:%d\n",currb - )
					}
					else if(or[j].loc < curr_b)
					{
						curr_b -= tmp;
						if(curr_b < or[j].loc)
							curr_b = or[j].loc;
					}
					else 
					{}
				}
			}
			else if(or[i].c[0] == 'B')
			{
				tmp = or[i].loc - curr_b;
				if(tmp < 0)
					tmp =-tmp;
				tmp ++;
				res = res + tmp;
				curr_b = or[i].loc;

				//处理另外一个
				for(j = i + 1 ; j < n ; j++)
				{
					if(or[j].c[0] == 'O')
						break;
				}
				if(j < n)
				{
					if(or[j].loc > curr_o)
					{
						curr_o += tmp ;
						if(curr_o > or[j].loc)
							curr_o = or[j].loc;
					}
					else if(or[j].loc < curr_o)
					{
						curr_o -= tmp;
						if(curr_o < or[j].loc)
							curr_o = or[j].loc;
					}
					else 
					{}
				}
			}
		}

		printf("Case #%d: %d\n",id++,res);
	}

}