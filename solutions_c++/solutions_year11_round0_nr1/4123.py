#include<stdio.h>
#include<stdlib.h>
int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.txt","w",stdout);
    int t,i,j,k,y,n;
    int last,timeO,nowO,timeB,nowB;
    char x;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
     scanf("%d",&n);
     last=0,timeO=0,nowO=1,timeB=0,nowB=1;
     for(i=0;i<n;i++)
     {
      scanf(" %c%d",&x,&y);
      if(x=='O')
      {
       while(timeO<last||nowO!=y)
       {
        if(nowO<y) nowO++;
        else if(nowO>y) nowO--;
        timeO++;
       }
       last=++timeO;
      }
      else
      {
       while(timeB<last||nowB!=y)
       {
        if(nowB<y) nowB++;
        else if(nowB>y) nowB--;
        timeB++;
       }
       last=++timeB;
      }
     }
     printf("Case #%d: %d\n",k,last);
    }
}

