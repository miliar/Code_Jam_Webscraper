#include <stdio.h>

char combine[50][4];
char opposite[50][3];
char stack[500];

int main()
{
  int T,c = 0,i,C,D,n,j,p,q,top,flag,a;
  char ch;

  scanf("%d",&T);
  while(T--)
  {
	  c++;
	  scanf("%d",&C);
	  for(i = 0;i<C;i++)
	  {
		  getchar();
		  scanf("%s",combine[i]);
	  }
	  scanf("%d",&D);
	  for(i = 0;i<D;i++)
	  {
          getchar();
		  scanf("%s",opposite[i]);
	  }
	  scanf("%d",&n);
	  getchar();
      top = 1;
	  scanf("%c",&stack[0]);
	  for(i = 1;i<n;i++)
	  {
           scanf("%c",&ch);
		   if(top==0)
		   {
			   stack[top++] = ch;
			   continue;
		   }
		   for(j = 0;j<C;j++)
		   {
			   if((stack[top-1]==combine[j][0]&&ch==combine[j][1])||(stack[top-1]==combine[j][1]&&ch==combine[j][0]))
			   {
				   top--;
				   stack[top++] = combine[j][2];
				   break;
			   }
		   }
		   if(j==C)
		   {
			   flag = 0;
			   a = top;
			   for(p = 0;p<a;p++)
			   {
				   for(q = 0;q<D;q++)
				   {
					   if((stack[p]==opposite[q][0]&&ch==opposite[q][1])||(stack[p]==opposite[q][1]&&ch==opposite[q][0]))
					   {
						   top = 0;
						   flag = 1;
						   break;
					   }
				   }
				   if(flag==1)
					   break;
			   }
			   if(p==a)
				   stack[top++] = ch;
		   }
	  }
	  printf("Case #%d:",c);
	  if(top==0)
	  {
		  printf(" []\n");
	  }
	  else
	  {
	  for(i = 0;i<top;i++)
	  {
		  if(i==0)
			  printf(" [");
		  else
			  printf(", ");
		  putchar(stack[i]);
	  }
	  printf("]\n");
	  }
  }
  return 0;
}