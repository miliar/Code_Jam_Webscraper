#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;
int A[25];
int B[25];
char C[25];
int len;
int tmp;

int num;
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 int t;
 int max;
 scanf("%d\n",&t);
 for(int i=1;i<=t;i++)
 {
  gets(C);
  len=strlen(C);
  num=0;max=50;
  for(int j=0;j<=20;j++)
  {
  A[j]=0;
  }
  for(int j=len-1;j>=0;j--)
  {
  A[len-j]=C[j]-'0';
  }
  for(int p=1;p<=len;p++)
  {
  for(int j=p+1;j<=len;j++)
  {
   if(A[j]<A[p])
   {
    /*tmp=A[p];
    A[p]=A[j];
    A[j]=tmp;
    sort(&A[1],&A[j]);
     printf("Case #%d: ",i);
     for(int k=len;k>=j;k--)
     {
     printf("%d",A[k]);
     }
     for(int k=1;k<j;k++)
     {
     printf("%d",A[k]);
     }
     printf("\n");*/
     if(j<max){max=j;num=p;}
    j=len+1;/*p=len+1;*/
   }
  } 
  
  }
  if(num!=0)
  {
  tmp=A[num];
    A[num]=A[max];
    A[max]=tmp;
    sort(&A[1],&A[max]);
     printf("Case #%d: ",i);
     for(int k=len;k>=max;k--)
     {
     printf("%d",A[k]);
     }
     for(int k=1;k<max;k++)
     {
     printf("%d",A[k]);
     }
     printf("\n");
  }
   else if(num==0)
   {
   sort(&A[1],&A[len+1]);
   printf("Case #%d: ",i);
    for(int ll=1;ll<=len;ll++)
    {
     if(A[ll]!=0)
     {
      printf("%d",A[ll]);
      for(int kk=1;kk<ll;kk++)
      {
      printf("0");
      }
       printf("0");
       for(int kk=ll+1;kk<=len;kk++)
       {
       printf("%d",A[kk]);
       }
       printf("\n");
      ll=len+1;
     }
    
    }
   }
 }
 return 0;
}
