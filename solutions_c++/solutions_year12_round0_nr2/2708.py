#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
int t;
fstream ip ("B-small-attempt1.in");
fstream op ("output.txt");

ip>>t;
int size=t;
while(t--)
{    
  int res_count,count=0;
   int N;
   ip>>N;
   int max;
  ip>>res_count;
   ip>>max;
   while(N--)
  { 
    int x;
    ip>>x;
    if(x%3==0)
   {
      int y=x/3;
      
      if(y>=max){count++;}
      else 
      {
       if((y+1)<10&&(y+1)>=max&&(y-1)>=0){count++;res_count--;}
      }
  

   } 
   else if(x%3==1)
   {
     int y=(x-1)/3;
     if((y+1)>=max)
     {
      count++;
         
     }  
  
   }
   else
   {
     int y=(x-2)/3;
       if((y+1)>=max){count++;}
       else
       {
         if((y+2)<10&&(y+2)>=max){count++;res_count--;}
       }
   }
  } 


  if(res_count<0)count=count+res_count;
  op<<"Case #"<<size-t<<": "<<count<<"\n";
 }
 ip.close();
 op.close();
}
