#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
using namespace std;
bool table[2000001];
int main()
{
  freopen("C-large.in","r",stdin);
  freopen("c.txt","w",stdout);
  int T,cases,A,B,i,j,temp,digits,r,counter,sum;
  int multi10[8]={1,1,10,100,1000,10000,100000,1000000};
  scanf("%d",&T);
  for (cases=1;cases<=T;cases++)
  {
    scanf("%d%d",&A,&B);
    sum=0;
    digits=ceil(log10(B));
    memset(table,0,sizeof(table));
    for(i=A;i<=B;i++)
    {
      temp=i;
      counter=0;
      table[i]=true;
      for(j=0;j<digits;j++)
      {
        r=temp%10;
        temp=r*multi10[digits]+temp/10;
        if(temp>=A && temp<=B)
        {
          if(!table[temp])
            counter++;
          table[temp]=true;
        }
      }
      sum+=(counter*(counter+1))>>1;
    }
    printf("Case #%d: %d\n",cases,sum);
  }
  return 0;
}
