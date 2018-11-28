#include<iostream>
#include<cstdio>
#define MAX 11
using namespace std;

int R, K , N , G[MAX] , SUM;

int move(int x)
{
   if(x < 0)return N-1;
   else if(x == N)return 0;    
   else return x; 
}

int main()
{
   freopen("C-small-attempt1.in","r",stdin);
   freopen("out.txt","w",stdout);
   
   int cs , make , f , sum;
   scanf("%d",&cs);
   for(int c=1;c<=cs;c++)
   {
      scanf("%d%d%d",&R,&K,&N);
      SUM = 0;
      for(int i=0;i<N;i++)
      {
         scanf("%d",&G[i]);
         SUM += G[i];
      }
      
      make = 0 , f = 0;
      if(K >= SUM)make = R * SUM;
      else
      while(R--)
      {
          sum = 0;
          while(sum <= K)
          {
             sum += G[f];  
             f = move(f+1);             
          }
          //printf("%d\n",sum-G[move(f-1)]);
          make += (sum-G[move(f-1)]);  
          f = move(f-1);         
      }   
      printf("Case #%d: %d\n",c,make);           
   }
   return 0;
}
