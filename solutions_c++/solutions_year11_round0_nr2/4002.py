#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
void check_oppose(char oppose[28][3],int D,char stack[100],int *stack_top);
int check_combine(char combine[36][4],int C,char stack[100],int *stack_top);
int main()
{
	int T,C,D,N;
	int i,j,str_len;
	char combine[36][4],oppose[28][3],str[101];
	char stack[100];
	int stack_top;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		stack_top=-1;
		scanf("%d",&C);
		for(j=0;j<C;j++)
			scanf("%s",combine[j]);
		scanf("%d",&D);
		for(j=0;j<D;j++)
			scanf("%s",oppose[j]);
		scanf("%d",&N);
		scanf("%s",str);
		stack[++stack_top]=str[0];
		for(j=1;j<strlen(str);j++)
		{
			stack[++stack_top]=str[j];
			while(check_combine(combine,C,stack,&stack_top));
			check_oppose(oppose,D,stack,&stack_top);
		}
		if(stack_top==-1)
			printf("Case #%d: []\n",i+1);	
		else
		{
			printf("Case #%d: [%c",i+1,stack[0]);
			for(j=1;j<=stack_top;j++)
				printf(", %c",stack[j]);
			printf("]\n");
		}	
	}
	return 0;
}
int check_combine(char combine[36][4],int C,char stack[100],int *stack_top)
{
	int i,j;
	if((*stack_top)==0 || (*stack_top)==-1)
		return 0;
	for(i=0;i<C;i++)
	{
		if((combine[i][0]==stack[*stack_top] && combine[i][1]==stack[*stack_top-1]) || (combine[i][1]==stack[*stack_top] && combine[i][0]==stack[*stack_top-1]))
		{
			(*stack_top)--;
			stack[*stack_top]=combine[i][2];
			return 1;
		}
	}
	return 0;
}
void check_oppose(char oppose[28][3],int D,char stack[100],int *stack_top)
{
	int i, j, a;
	for(j=0;j<D;j++)
		if(oppose[j][a=0]==stack[*stack_top] || oppose[j][a=1]==stack[*stack_top])
		{
			for(i=0;i<(*stack_top);i++)
				if(oppose[j][1-a]==stack[i])
				{	
					*stack_top=-1;
					return;
				}					
		}	
}
