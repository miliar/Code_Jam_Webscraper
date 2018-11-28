#include"stdio.h"
char a[50][50];
int replacetiles(int,int,int);
int main()
{
    freopen("prob1.in" ,"r+",stdin);
    freopen("prob1.out" ,"w+",stdout);
     int N,M;
    int pd,pg;
    int num_of_cases = 0;
    scanf("%d\n",&num_of_cases);
    for(int i=1;i<=num_of_cases;i++)
    {
     scanf("%d ",&N);
     scanf("%d ",&M);
     for(int j=1;j<=N;j++)
     {
      for(int k=1;k<=M;k++)
	scanf("%c",&a[j][k]);
	scanf("\n");
      }
     if(!replacetiles(N,M,i))
	 printf("Case #%d:\nImpossible\n",i);
    }

    fclose(stdin);
    fclose(stdout);
    return 1;
}
int replacetiles(int N,int M,int caseno)
{
 for(int i=1;i<=N;i++)
  for(int j=1;j<=M;j++)
  {
   if(a[i][j] == '#')
   {
    if(a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
    {
      a[i][j+1] = '\\';
      a[i][j] = '\/';
      a[i+1][j] = '\\';
      a[i+1][j+1] = '\/';

    }
    else
    {
     return 0;
    }
   }
  }
  printf("Case #%d:\n",caseno);
  for(i = 1;i<=N;i++)

  {
  for(j=1;j<=M;j++)
  {
     printf("%c",a[i][j]);
  }
  printf("\n");
  }
  return 1;
}