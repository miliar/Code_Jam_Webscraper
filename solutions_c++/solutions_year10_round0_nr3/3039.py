#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    long int T,i=0,r,k,n,j,sum=0,m,totsum=0,l,arrsum;
    int gsize[1000];
    cin>>T;
    while(i<T)
    {
              cin>>r>>k>>n;
              arrsum=0;
              for(j=0;j<n;j++)
              {
               cin>>gsize[j];
               arrsum+=gsize[j];
              }
              m=0;
              totsum=0;
              
              if(arrsum<k)
              totsum=r*arrsum;
              else
              {
              for(j=0;j<r;j++)
              {
               sum=0; 
                            
               while(sum<=k)
               {
                  sum+=gsize[m];
                  m++;
                  
                  if(m==n)
                  m=0;              
               
               }
               if(m==0)
               m=n-1;
               else
               m--;
               sum=sum-gsize[m];
               totsum+=sum;
              }
              }
              cout<<"Case #"<<i+1<<": "<<totsum<<"\n";
              i++;        
    }
    return 1;
}
