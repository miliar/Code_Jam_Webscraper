#include <cstdio>

typedef struct DATA
{
	char ch;
	int num;
}data;

int main()
{
	int testcase,cnt=1;
	FILE* fp;
	fp=fopen("output.out","w");
	scanf("%d",&testcase);
	getchar();

	while(testcase--)
	{
		int data_num;
		int i,time=0;
		int O[101]={-1};
		int B[101]={-1};
		int orderpos=0,bpos=1,opos=1; // 위치 정보

		scanf("%d",&data_num);

		data* order=(data*)new data[data_num+1];
	
		for(i=0;i<data_num;i++)
		{
			scanf(" %c %d",&(order[i].ch),&(order[i].num));
			if(order[i].ch=='O')
			{
				O[order[i].num]=1;
			}
			else
			{
				B[order[i].num]=1;
			}
		}
		while(orderpos<data_num)
		{
			char priority=order[orderpos].ch;
			int position=order[orderpos].num;
			int nextposition;
	
			if(priority=='B')
			{
				for(i=orderpos;i<data_num;i++)
				{
					if(order[i].ch=='O')
					{
						nextposition=order[i].num;
						if(O[nextposition]==1)
						{
							break;
						}
					}
				}
				if((B[bpos]==1&&bpos==position)||(B[bpos]==0&&bpos==position))
				{
					B[bpos]=0;
					orderpos++;
				}
				else
				{
					if(bpos<position)
					{
						bpos++;
					}
					else
					{
						bpos--;
					}
				}
				if(opos!=nextposition)
				{
					if(opos<nextposition)
					{
						opos++;
					}
					else
					{
						opos--;
					}
				}
			}
			else
			{
				for(i=orderpos;i<data_num;i++)
				{
					if(order[i].ch=='B')
					{
						nextposition=order[i].num;
						if(B[nextposition]==1)
						{
							break;
						}
					}
				}
				if((O[opos]==1&&opos==position)||(O[opos]==0&&opos==position))
				{
					O[opos]=0;
					orderpos++;
				}
				else
				{
					if(opos<position)
					{
						opos++;
					}
					else
					{
						opos--;
					}
				}
				if(bpos!=nextposition)
				{
					if(bpos<nextposition)
					{
						bpos++;
					}
					else
					{
						bpos--;
					}
				}
			}
			time++;
		}
		fprintf(fp,"Case #%d: %d\n",cnt++,time); 
		delete[] order;
	}
	fclose(fp);
	return 0;
}