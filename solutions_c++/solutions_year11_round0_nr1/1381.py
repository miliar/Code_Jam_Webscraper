#include<stdio.h>
#include<stdlib.h>
#include<math.h>

FILE *f,*f2;
struct node
{
       char c;
       int num;
};

int main()
{
    f=fopen("A-large.in","r");
    f2=fopen("A-large.out","w");
    int T,N;
    fscanf(f,"%d",&T);
   //scanf("%d",&T);
    node a[100]; 
    for(int i=0;i<T;i++)
    {
            fscanf(f,"%d",&N);
            //printf("%d\n",N);
            
            for(int j=0;j<N;j++)
            {
                int x;
                char y[10];
                
               // do
                fscanf(f,"%s",y);
                //while(y=='B'||y=='O');                          
                fscanf(f,"%d",&x);
               // printf("%c %d\n",y[0],x);
                a[j].c=y[0];
                a[j].num=x;
                //printf("%c and %d\n",a[j].c,a[j].num);
            }
            for(int j=0;j<N;j++)
            {
                    //printf("%c and %d\n",a[j].c,a[j].num);       
            }
            char now=a[0].c;
            int p1=1,p2=1;
            int time=0;
            int temp=0;
            for(int j=0;j<N;)
            {                   
                    if(a[j].c==now) 
                    {
                                  time+=abs(a[j].num-p1)+1;
                                  temp+=abs(a[j].num-p1)+1;
                                  p1=a[j].num;
                                  j++;
                    }
                    else
                    {
                                  if(abs(a[j].num-p2)<temp)
                                  {
                                                      p2=p1;
                                                      p1=a[j].num;
                                                      now=a[j].c;
                                                      temp=0;
                                  }
                                  else
                                  {
                                                      if(a[j].num>p2)
                                                      {
                                                                     int t=p2;
                                                                     p2=p1;
                                                                     p1=t+temp;
                                                      }
                                                      else
                                                      {
                                                                     int t=p2;
                                                                     p2=p1;
                                                                     p1=t-temp;
                                                      }
                                                      now=a[j].c;
                                                      temp=0;
                                  }
                    }
                    //printf("%d %d %d\n",time,p1,p2,j);
            }
            fprintf(f2,"Case #%d: %d\n",i+1,time);
                                  
                    
                     
                                      
                     
    }     
}          
