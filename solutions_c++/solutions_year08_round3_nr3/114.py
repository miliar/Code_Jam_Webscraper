#include <fstream.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int A[500001];
int B[500001];
int seq[500001];
long long max=1000000007;
int main()
{

 int allnum,casenum;
 long long sum,asum;
 freopen("c.in","r",stdin);
 //fstream fin("A-large.in");
 int m,n,i,j,k;
 long long x,y,z;
 cin>>allnum;
 for(casenum=1;casenum<=allnum;casenum++)
 {
   cin>>n>>m>>x>>y>>z;
   for(i=0;i<m;i++)
      cin>>B[i];
   for(i=0;i<n;i++)
   {
      A[i] = B[i%m];
      B[i%m] = (x*B[i%m]+y*(i+1))%z;
   //   cout<<A[i]<<endl;
   }
   sum=1;
   seq[0] = 1;
   for(i=1;i<n;i++)
   {
     asum=1;
     for(j=0;j<i;j++)
     {
       if(A[i]>A[j])
         asum = (asum+seq[j])%max;              
     }
     seq[i] = asum;
  //   cout<<asum<<endl;
     sum = (sum+asum)%max;
   }
 
   cout<<"Case #"<<casenum<<": "<<sum<<endl;
  // cout<<sum<<endl;
  // printf("Case #%d: %lld\n",casenum,sum);
   
 }

}
