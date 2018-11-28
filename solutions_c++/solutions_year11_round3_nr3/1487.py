#include"stdio.h"
int a[200];
int harmony(int,int,int);
int main()
{
    freopen("prob1.in" ,"r+",stdin);
    freopen("prob1.out" ,"w+",stdout);
     int N,L,H;
    int pd,pg;
    int num_of_cases = 0;
    scanf("%d\n",&num_of_cases);
    for(int i=1;i<=num_of_cases;i++)
    {
     scanf("%d ",&N);
     scanf("%d ",&L);
     scanf("%d\n",&H);
     for(int j=1;j<=N;j++)
     {
       scanf("%d ",&a[j]);
      }
      int har = harmony(N,L,H);
     if(!har)
	 printf("Case #%d: NO\n",i);
     else
     {
       printf("Case #%d: %d",i,har);
     }

    }

    fclose(stdin);
    fclose(stdout);
    return 1;
}
int harmony(int N,int L,int H)
{
	int count = 0;
      for(int i = L;i<=H;i++)
   {
	count = 0;
      for(int j= 1;j<=N;j++)
      {
	if(i%a[j] == 0 || a[j]%i == 0)
	 count++;

      }
      if(count == N)
      {
       return i;
      }
   }
   return 0;

  }