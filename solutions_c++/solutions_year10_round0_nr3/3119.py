#include <iostream>
#include <list>
#include <queue>
#include "stdio.h"
using namespace std;
int main(){
  int a=0,tot=0,i1=0,t=0,temp1=0,temp=0,c=0,i=0,e=0,sum=0,sum1=0,d=0;
    FILE *sf,*rf;

  sf=fopen("i:\\csmall.in","r");
rf=fopen("i:\\ocsmall12.txt","w+");
  fscanf(sf,"%d",&t);



  for(i1=0;i1<t;i1++){
  fscanf(sf,"%d %d %d",&a,&tot,&c);
   queue<int> q;
  for(i=0;i<c;i++){
      fscanf(sf,"%d",&e);
      q.push(e);
  }
for(i=0;i<a;i++)
{   sum=0;
    for(d=0;d<c;d++){
       temp=q.front();
    sum=temp+sum;
    if(sum<=tot){
   temp1=q.front();
   q.pop();
   q.push(temp1);temp=0;
    continue;
    }
   else
   {  sum=sum-temp;temp=0;
       break;
   }
}
sum1=sum+sum1;
}


fprintf(rf,"Case #%d: %d\n",i1+1,sum1);
 sum1=0;
 a=0;tot=0;temp1=0;temp=0;c=0;i=0;e=0;sum=0;sum1=0;d=0;
 }
fclose(rf);
fclose(sf);

}
