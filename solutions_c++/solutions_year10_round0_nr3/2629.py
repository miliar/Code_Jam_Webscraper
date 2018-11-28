#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
   long long l,r,k,n;
    long long  i,j,m,p;
    long long  rsum=0,sum=0,temp=0,psum=0;
    cin>>l;
    for(i=1;i<=l;i++)
    {
                    rsum=0;psum=0;
                    cin>>r>>k>>n;
                    long long  a[n];
                    for(p=0;p<n;p++)
                              { cin>>a[p];}
                              for(p=0;p<n;p++)
                                    {
                                    psum=psum+a[p];}
                                    
                                 if(psum<=k)
                                  {rsum=psum*r;
                                    cout<<"Case #"<<i<<": "<<rsum<<endl;
                                    continue;}
                   else
                    for(m=0;m<r;m++)
                    {    sum=0;
                         while(sum<=k)
                            {   
                                 if(sum+a[0]<=k)
                                 {sum=sum+a[0];
                                 temp=a[0];
                                 for(j=0;j<n-1;j++)
                                 {a[j]=a[j+1];}
                                 a[n-1]=temp;}
                                 else 
                                 break;
                            }
                            
                    rsum+=sum;
                    
                    }
    cout<<"Case #"<<i<<": "<<rsum<<endl;
   }
   //system("pause");
   return 0;
}
