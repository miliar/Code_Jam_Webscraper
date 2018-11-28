#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctime>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;





int main() 
{ 
//    freopen("..\\A.in","r",stdin); 
   freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout); 
//    freopen("..\\A-small-attempt1.in","r",stdin);freopen("..\\A-small-attempt1.out","w",stdout); 
//    freopen("..\\A-large.in","r",stdin);freopen("..\\A-large.out","w",stdout); 
//    freopen("..\\A-small.in","r",stdin);freopen("..\\A-small.out","w",stdout);
    int t,R,K,N,g[1001];
    int head,tail;
    int sum[100001],count,num[100001];
    while (scanf ("%d",&t)!=EOF)
    {
          for (int i=1;i<=t;i++)
          {
              scanf ("%d %d %d",&R,&K,&N);
              for (int j=0;j<N;j++)       
                  scanf ("%d",&g[j]);
              head=0;tail=N-1;
              count=0;
              sum[0]=0;
              int res;
              for (int j=0;j<R;j++)
              {
                  num[j]=0;
                  for (int l=0,k=head;l<N;k=(k+1)%N,l++)
                  {
                      if (num[j]+g[k]<=K)
                      {
                         num[j]+=g[k];                   
                      }    
                      else
                      {
                          head=k;
                          tail=(k+N-1)%N;
                          break;    
                      }
                  }    
                  
                  sum[j+1]=num[j]+sum[j];
                  //cout<<sum[j+1]<<" "<<num[j]<<" "<<head<<" "<<tail<<endl;
                  count=j+1;
                  res=sum[j+1];
                  if (head==0)
                  {
                      res=R/count*res+sum[R%count];
                      break;           
                  }
              }
              
              
              
              printf ("Case #%d: %d\n",i,res);
          }
    }
    return 0; 
} 



