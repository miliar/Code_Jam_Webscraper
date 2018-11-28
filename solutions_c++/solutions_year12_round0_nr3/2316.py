#include<iostream>
#include<fstream>
using namespace std;
int length;
int* arrayB=new int[10];
int* arrayN=new int[10];
int* V=new int[10];

int indexPow(int a)
{
    int temp=1;
    for(int i=0;i<a;i++) temp*=10;
    return temp;
}
int compare(int j)
{
    int temp=0;
    int index=length-1;
    for(int i=j;i<length;i++)
      temp+=arrayN[i]*indexPow(index--);
    for(int i=0;i<j;i++)
      temp+=arrayN[i]*indexPow(index--); 
    return temp;
}

int main()
{
   int i,j,n,m,T,A,B,sum;
   int temp,tempA,tempB;
   FILE *in=fopen("C:\\Users\\yl\\Desktop\\C-large.in","r");
   FILE *out=fopen("C:\\Users\\yl\\Desktop\\C-large.out","w");
   fscanf(in,"%d\n",&T);
   for(i=0;i<T;i++)
   {
     fscanf(in,"%d %d",&A,&B);
     tempA=A;
     tempB=B;
     sum=length=0;
     while(tempA)
     {
        length++;
        tempA=tempA/10;       
     }  
     for(j=length-1;j>=0;j--)
     {
         arrayB[j]=tempB%10;
         tempB=tempB/10;
     }        
   for(n=A;n<B;n++)
   {
     temp=n;
     for(j=length-1;j>=0;j--)
     {
         arrayN[j]=temp%10;
         temp=temp/10;
     }    
      
     for(j=1;j<length;j++)
     {
       if(arrayN[j]!=0)
       {
          V[j]=compare(j);
          int flag=0;
          for(m=1;m<j;m++)   
            if(V[j]==V[m]) {flag=1;break;}
          if(!flag&&V[j]>n&&V[j]<=B) sum++;
       }
     }   
    }
    fprintf(out,"Case #%d: %d\n",i+1,sum);              
 }
   system("pause");
   return 0;
}

