#include<stdio.h>
#include<string.h>
const int N = 10000;
char str[3];
struct node
{
	int pret;//上一时间
	int prep;//上一位置
}robot[2];
int main()
{
	
	int T;
	scanf("%d",&T);
	{
		int cases;
		for(cases=1;cases<=T;cases++)
		{
           int n,x;
		   scanf("%d",&n);
           for(x=0;x<2;x++)
		   {
			   robot[x].prep = 1;
			   robot[x].pret = 0;
		   }

		   int ans = 0;
		   int choice;
		   while(n--)
		   {
			   scanf("%s%d",str,&x);
			   if(str[0]=='O')
			    choice = 0;
			   else
			    choice=1;

			   int temp = x-robot[choice].prep;
               temp=temp>0?temp:-temp;
			   int cost = ans - robot[choice].pret;
			   temp=temp>cost?(temp-cost):0;
			   temp++;
			   ans+=temp;
			   robot[choice].prep = x;
			   robot[choice].pret = ans;
		   }

		   printf("Case #%d: %d\n",cases,ans);
		}
	}
	return 0;
}

/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

*/