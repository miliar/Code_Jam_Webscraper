#include <fstream.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long getnum(int len)
{
 long long sum=1;
 int i;
 for(i=0;i<len;i++)     
     sum = sum*3;
 return sum;
}  


int main()
{

 int allnum,casenum;
 int i,j,k,t,n,asum,sig;
 //int X,Y;
 int len,buf[100],max;
 char buffer[100];
 long long sum,value,value1;
 freopen("b.in","r",stdin);
 //fstream fin("A-large.in");
 
 cin>>allnum;
 for(casenum=1;casenum<=allnum;casenum++)
 {
   cin>>buffer;
   len = strlen(buffer);
   for(i=0;i<len;i++)
       buf[i] = buffer[i]-'0';
   max = getnum(len-1);
   sum = 0;
   for(i=0;i<max;i++)
   {
 //     i=5;
      j=i;
      value = 0;//buf[0];
      value1 = buf[0];
      sig=1;
      for(t=1;t<len;t++)
      {
        k = j%3;
        j = j/3;
        if(k == 1)
        {
     //     value = value*10;
          value1 = value1*10+sig*buf[t];     
  //        cout<<"=";
        }
        else 
        {
           value = value+value1;
           value1=0;
           if(k==0)     
              sig=1;
           else if(k==2)
              sig=-1;
           value1  = sig*buf[t];
   
        }
     
      }  //end for
      value = value+value1;
      if(value<0)
         value = 0-value;
  //       cout<<" "<<value<<" "<<sum<<endl;
      if(value==0)
         sum++;
      else
      {
        if(value%2==0)
          sum++;
         else if(value%3==0)
           sum++;
           else if(value%5==0)
              sum++;
            else if(value%7==0)
              sum++;  
          
      }   
  //       break;
   }
  
 
   cout<<"Case #"<<casenum<<": "<<sum<<endl;
  // cout<<sum<<endl;
  // printf("Case #%d: %lld\n",casenum,sum);
   
 }

}
