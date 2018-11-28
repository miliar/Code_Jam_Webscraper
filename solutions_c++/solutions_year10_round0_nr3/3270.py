#include<stdio.h>
#include<stdlib.h>
void change_people(int);
int people[10]={0},N;
int main()
{
   int T,i,j,l,m,R,k,set=0,money=0;
   scanf("%d",&T);
   FILE *file=fopen("output.txt","w");
   for(i=0;i<T;i++)
   {
      scanf("%d %d %d",&R,&k,&N);
      for(j=0;j<N;j++)
         scanf("%d",&people[j]);
      for(l=0;l<R;l++)
      {
         for(j=0;j<N;j++)
         {
            if(set<=k)
            {
               set+=people[j]; 
               if(j==N-1 && N!=1 && set>k)
                  set-=people[j];
            }
            else
            {
               if(set!=k)
                  set-=people[j-1];
               break;
            }
         }
         money+=set;
         change_people(j-1);
         set=0;
      }
      fprintf(file,"Case #%d: %d\n",i+1,money);
      money=0;
   }
   fclose(file);
   return 0;
}
void change_people(int j)
{
   int a,b,c,temp[10];
   for(c=0;c<j;c++)
      temp[c]=people[c];
   for(a=j,b=0;a<N;a++,b++)
      people[b]=people[a];
   for(a=b,c=0;a<N;a++,c++)
      people[a]=temp[c];
   for(c=0;c<10;c++)
      temp[c]=0;
}

