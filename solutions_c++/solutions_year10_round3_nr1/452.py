#include<iostream>
using namespace std;
int main()
{
    long long t,a,b,i,j,n,q,temp,count;
    q=1;
    cin>>t;
    while(t--)
    {
              struct
              {
                    long long x;
                    long long y;
              }arr[1005];
              cin>>n;
              for(i=0;i<n;i++)
                 cin>>arr[i].x>>arr[i].y;
              for(i=0;i<n;i++)
              {
                 for(j=i+1;j<n;j++)
                 {
                     if(arr[j].y<arr[i].y)
                     {
                        temp=arr[j].y;
                        arr[j].y=arr[i].y;
                        arr[i].y=temp;
                        temp=arr[j].x;
                        arr[j].x=arr[i].x;
                        arr[i].x=temp;
                     }
                 }
              }
              count=0;
              for(i=0;i<n;i++)
              {
                   b=arr[i].y;
                   a=arr[i].x;
                   for(j=0;j<i;j++)
                      if(arr[j].x > a)
                         count++;
                   for(j=i+1;j<n;j++)
                      if(arr[j].x < a)
                                     count++;
                                    
              }
              cout<<"Case #"<<q++<<": "<<(count/2)<<endl;
    }
    return 0;
}
