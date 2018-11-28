#include<stdio.h>
#include<conio.h>
#include<cmath>

int count;

int telldigits(int x)
{
    if(x<10) return 0;
    else if(x<100) return 2;
    else if(x<1000)return 3;
    else if(x<10000) return 4;
} 

inline void rcs(int n,int m,int len,int len1)
{
     int temp=n,temp1;
     if(len==len1)
     {
     while(n>0)
     {
                  n=n/10;
                  temp1=pow(10.00,len-1)*(temp%10)+floor(temp/10);
                  if(temp1==m) 
                  {
                               count++;
                               break;
                  }
                  temp=temp1;
                  
     }
     }
}

int main()
{
int t,a,b,i,j,test;

freopen("C-small-attempt0.in","r",stdin);
freopen("recycleanssmall.txt","w",stdout);

scanf("%d",&t);
for(test=1;test<=t;test++)
{
          count=0;
          scanf("%d %d",&a,&b);
          for(i=a;i<=b-1;i++)
          {
                             for(j=i+1;j<=b;j++)
                             {
                                                rcs(i,j,telldigits(i),telldigits(j));
                             }
          }
          printf("Case #%d: %d\n",test,count);                                   
}
return 0;
}
