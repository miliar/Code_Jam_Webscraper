/* 
 * File:   main.cpp
 * Author: Rohit
 *
 * Created on 8 May, 2010, 8:14 PM
 */
#include <stdlib.h>
#include <stdio.h>
void shiftqueue(int*,int*,int);
void fill(int*, int*,int);
int count=0;
int main()
{
    int R,k,N,T,i;
FILE *f;
FILE *g;
f=fopen("C:\\Users\\Rohit\\Desktop\\test.in","r");
g=fopen("C:\\Users\\Rohit\\Desktop\\answer.in","w");
fscanf(f,"%d",&T);
for(i=1;i<=T;i++)
{
    int total=0;
    fscanf(f,"%d %d %d",&R,&k,&N);
    int *line=(int *)calloc(N,(sizeof(int)));
    int *line2=(int *)calloc(N,(sizeof(int)));
    for(int j=0;j<N;j++)
    {
        fscanf(f,"%d",(line+j));
    }
    for(int a=0;a<R;a++)
    {
        int set=0;
        while(true)
        {
          if(*line==0)
             {
                 break;
             }
         if((set+(*(line))<=k))
         {
             set=set+*(line);
             shiftqueue(line,line2,N);
         }
         else
         {
            break;
         }
        }
        total=total+set;
        fill(line,line2,N);
    }
    fprintf(g,"Case #%d: %d\n",i,total);
   }
    return (EXIT_SUCCESS);
}
void shiftqueue(int* line,int* line2,int N)
{
 int x,i;
 x=*line;
     if(N==1)
     {
         *line=0;
         *line2=x;
         return;
     }
     for(i=0;i<N-1;i++)
     {
             *(line+i)=*(line+i+1);
     }
     *(line+N-1)=0;
     *(line2+count)=x;
     count++;
}
void fill(int* line, int* line2,int N)
{
   
    int i,j;
    if(N==1)
    {
        *line=*line2;
        return;
    }
    for(i=N-1,j=count-1;j>=0;i--,j--)
    {
        *(line+i)=*(line2+j);
        *(line2+j)=0;
    }
    count=0;
}

