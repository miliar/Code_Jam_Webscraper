#include <cstdlib>
#include <iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
using namespace std;

int main(int argc, char *argv[])
{
    int t,n,cas,i,j;
    int r[200],p[200];
    freopen("A-large.in","r",stdin);
    freopen("out_1_large.txt","w",stdout);
    scanf("%d",&cas);
    t=0;
    while(cas--)
    {
      t++;
      scanf("%d",&n);
      int sum=0;
      int tot=0;
      int d,d1,d2,td;
      int temp;
      char s[2];
      char ch,tch;
      getchar();
      scanf("%c",&ch);
      tch=ch;
      scanf("%d",&d);
      sum+=d;
      td=d;
      d1=d2=1;
      bool flag=false;
      int ta=0;
      int tb=0;
      for (i=1;i<n;i++)
      {
        getchar();
        scanf("%c",&ch);
        scanf("%d",&d);
     //   cout<<tot<<" #"<<endl;
        if (ch!=tch) 
          {
            flag=true;
            if (ch=='O') {temp=ta+fabs(d-d1)+1; d2=td; tb=sum;}
            else {temp=tb+fabs(d-d2)+1; d1=td; ta=sum;}
            if (sum<temp) sum=temp;
            else sum++;
          //  sum=max(sum,temp);
            tch=ch;
            td=d;
          }
        else 
         {
             flag=false;
             sum+=(fabs(d-td)+1);
      //       cout<<sum<<endl;
         }
        tch=ch;
        td=d;
      }
     printf("Case #%d: %d\n",t,sum);
    }
  //  system("PAUSE");
    return EXIT_SUCCESS;
}
