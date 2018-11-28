#include <fstream.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int compare(int  *arg1,   int   *arg2 )  
{
         return *arg2-*arg1;
}   


int main()
{

 int allnum,casenum;
 long long i,j,k,n,asum;
 //int X,Y;
 int P,K,L;
 int feq[1002];
 long long sum;
 freopen("a.in","r",stdin);
 //fstream fin("A-large.in");
 
 cin>>allnum;
 for(casenum=1;casenum<=allnum;casenum++)
 {
   cin>>P>>K>>L;
   for(i=0;i<L;i++)
     cin>>feq[i];
   qsort((void *)feq,L,sizeof(int),(int(*)(const void*, const   void*))compare);
    k=1;
    n=0;
    sum=0;
    asum = 0;
    for(i=0;i<L;i++)
    {
        n++;
        asum+=feq[i];
        if(n==K)
        {
                    //   cout<<asum<<" "<<k<<endl;

          sum += k*asum; 
          asum = 0;
          n =0;
          k++;       
        }
                    
    }
    sum+=k*asum;
 
   cout<<"Case #"<<casenum<<": "<<sum<<endl;
  // cout<<sum<<endl;
  // printf("Case #%d: %lld\n",casenum,sum);
   
 }

}
