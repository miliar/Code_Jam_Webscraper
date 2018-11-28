#include <stdio.h>
#include <stdlib.h>

int max(int a,int b)
{
	return (a>b)?a:b;
}

	int c,d,n;
	char sc[100][4];
	char dc[100][3];
	char s[102];


char check(char a,char b)
{
	int i;
	for(i=0;i<c;i++)
	{
		if( (sc[i][0] == a && sc[i][1] == b) || (sc[i][0] == b && sc[i][1] == a) )
			return sc[i][2];
	}
	return 0;
}

int opp(char a,char b)
{
	int i;
	for(i=0;i<d;i++)
	{
		if( (dc[i][0] == a && dc[i][1] == b) || (dc[i][0] == b && dc[i][1] == a) )
			return 1;
	}
	return 0;
}

int main()
{
	int otime, btime;
	int opos, bpos;
	int pos;
	char cc;
	int cas,asd;
	int ins,i,j;

	char stack[103];
	int top;
	char next;
	
	freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d",&c);
		for(i=0;i<c;i++)
			scanf("%s",sc[i]);

		scanf("%d",&d);
		for(i=0;i<d;i++)
			scanf("%s",dc[i]);
		
		scanf("%d",&n);
		scanf("%s",s);
		top = 0;
		for(i=0;i<n;i++)
		{

			stack[top++] = s[i];

			while(top>=2 && (next = check(stack[top-2],stack[top-1]))!=0 )
			{
				stack[top-2] = next;
				top--;
			}

			for(j=0;j<top-1;j++)
			{
				if( opp(stack[top-1], stack[j]) )
					top = 0;
			}

		}
		stack[top] = 0;
		printf("Case #%d: [",asd+1);
		for(i=0;i<top;i++)
		{
			if(i!=0)
				printf(", ");
			printf("%c",stack[i]);
		}
		printf("]\n");
	}

	return 0;
}