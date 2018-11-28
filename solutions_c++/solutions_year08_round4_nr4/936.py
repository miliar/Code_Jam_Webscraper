#include <fstream.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char trans[1024*64][16];
int createtrans(int n)
{
 int i,j,k,t,n1,n2,tt;
 char tmp[17];
 for(i=0;i<n;i++)
    tmp[i] = i;
 int max=1,min;
 for(i=0;;i++)
 {
    memcpy(trans[i],tmp,16);
    for(j=n-2;j>=0;j--)
    {
       if(tmp[j]<tmp[j+1])
           break;     
    }
    if(j<0)
       break;
    min = 100;
    for(t=j+1;t<n;t++)
    {
      if((tmp[t]>tmp[j])&&(tmp[t]<min))
      {
         min = tmp[t];
         tt = t;                      
      }                  
    }
    tmp[tt] = tmp[j];
    tmp[j] = min;
 
    for(t=n-1;t>j;t--)
      for(k=j+1;k<t;k++)
      {
         if(tmp[k]>tmp[k+1])
         {
    tt = tmp[k];
    tmp[k] = tmp[k+1];
    tmp[k+1] = tt;
                            
         }                
                      
      }
 }
 max = i+1;   
 return max;
}  


int main()
{

 int allnum,casenum;
 int i,j,k,t,n,max,min;
 //int X,Y;
 int len,start,count;
 char buffer[6000],buf1[60000],tmp,tmp1;

 freopen("d.in","r",stdin);
 //fstream fin("A-large.in");
 
 cin>>allnum;
 for(casenum=1;casenum<=allnum;casenum++)
 {
   cin>>k>>buffer;
   max = createtrans(k);
   len = strlen(buffer);
   min = 50000;
   for(t=0;t<max;t++)
   {
     start = 0;
     j=0;
     count = 0;
   tmp=0;
     for(i=0;i<len;i++)
     {
       tmp1 = buffer[trans[t][i-start]+start];
       j++;
       if(j==k)
       { 
               j=0;
               start+=k;
       }
       if(tmp !=  tmp1)
       {
          tmp = tmp1;
          count++;   
       }
       
     }
     if(count<min)
       min = count;
   }
 
   cout<<"Case #"<<casenum<<": "<<min<<endl;
  // cout<<sum<<endl;
  // printf("Case #%d: %lld\n",casenum,sum);
   
 }

}
