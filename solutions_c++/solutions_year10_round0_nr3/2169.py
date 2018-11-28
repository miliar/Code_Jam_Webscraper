#include<iostream>
using namespace std;
int main()
{
    int t,i,j,l,count=0,count1;
    long long int r,k,n,lsum=0,temp;
    int arr[1000];
    cin>>t;
    for(i=0;i<t;i++)
    {
                    lsum=0;
                    cin>>r>>k>>n;
                    temp = k;
                    count = 0;
                    
                    for(j=0;j<n;j++)
                    {
                                    cin>>arr[j];
                    }
                    for(j=0;j<r;j++)
                    {
                              count1=-1;
                              temp=k;   
                              while(temp>=0 && count1!=count)
                              {
                                           temp=temp-arr[count];
                                           count1 = count;
                                           lsum += arr[count];
                                           count = (count+1)%n;
                              }   
                                
                              if(temp<0) {
                              lsum = lsum - arr[count1];
                              count = count1; 
                              }
                    }
                    cout<<"Case #"<<(i+1)<<": "<<lsum<<"\n";
    }
    return 0;
}
