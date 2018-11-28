#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    int i,j,T,N,S,p,sum;
    FILE *in=fopen("C:\\Users\\yl\\Desktop\\B-large.in","r");
    FILE *out=fopen("C:\\Users\\yl\\Desktop\\B-large.out","w");
    fscanf(in,"%d\n",&T);
    for(i=0;i<T;i++)
    {
       fscanf(in,"%d %d %d",&N,&S,&p);
       int* t=new int[N];
       int* tempA=new int[N];
       int* tempB=new int[N];
       int* V=new int[N];
       sum=0;
       for(j=0;j<N;j++)
       {
         fscanf(in,"%d",&t[j]);
         tempA[j]=t[j]/3;
         tempB[j]=t[j]%3;
       }
           
       for(j=0;j<N;j++)
       {
          if(tempB[j]==2)
          {
            if(tempA[j]+2==p&&S>0)  {sum++; S--;}        
          } 
          else if(tempB[j]==0)
          {
             if(tempA[j]>0&&tempA[j]+1==p&&S>0) {sum++;S--;}  
          }           
       }
            
       for(j=0;j<N;j++)
       {
         if(tempB[j]==1)   
         {
             if(tempA[j]+1>=p)  
             {
               sum++;
               if(S>0)S--;
             }
         }
         
         else if(tempB[j]==0) 
         {
            if(tempA[j]>=p)
            {
               sum++;
               if(S>0) S--;
            } 
         }
         else if(tempB[j]==2)
         {
            if(tempA[j]+1>=p) 
            {
              sum++;
              if(S>0) S--;
            }
         }
       } 
       
       fprintf(out,"Case #%d: %d\n",i+1,sum);            
    }
    system("pause");
    return 0;
}
