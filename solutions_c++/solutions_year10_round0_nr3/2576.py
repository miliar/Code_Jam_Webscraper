#include<stdio.h>
#include<string.h>

#define MAX 10000

using namespace std;

int input[MAX];
int mark[MAX];

int main()
{
	int t,T;
	scanf("%d",&T);
	for(t= 1;t<= T;t++)
	{
		int r,k,n;
		//r times,maximum k people,n groups;
		scanf("%d%d%d",&r,&k,&n);
		int i;
		for(i= 0;i< n;i++)
		{
			scanf("%d",&input[i]);
		}
		int times,pointer= 0,income= 0;
		
		for(times= 0;times< r;times++)
		{
			int onBoard= 0;
			memset(mark,0,sizeof(mark[0])* n);
			while(onBoard< k)
			{
				if(mark[pointer]== 1)
					break;
				else
				{
					if(input[pointer]> k)
						input[pointer]= 0;

					onBoard+= input[pointer];
					mark[pointer]= 1;
					pointer= (pointer+ 1)% n;
				}
			}
			if(onBoard> k)
			{
				if(pointer== 0)
					pointer= n- 1;
				else
					pointer= (pointer- 1)% n;
				mark[pointer]= 0;
				onBoard-= input[pointer];
			}
			income+= onBoard;
//			printf("%d\n",income);
		}
		printf("Case #%d: %d\n",t,income);
	}
}
