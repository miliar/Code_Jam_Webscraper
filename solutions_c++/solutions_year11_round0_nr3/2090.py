#include<iostream>
using namespace std;
int main()
{
    int t,n,a,b,i,j,min;
    unsigned long long sum;
    cin>>t;
    for(i=0;i<t;i++)
    {
                    cin>>n;
                    cin>>a;
                    b=a;
                    min=a;
                    sum=a;
                    for(j=1;j<n;j++)
                    {
                                    cin>>a;
                                    b=a^b;
                                    sum=sum+a;
                                    if(a<min)
                                    min=a;
                    }
                    if(b!=0)cout<<"Case #"<<(i+1)<<": NO"<<endl;
                    else
                         cout<<"Case #"<<(i+1)<<": "<<(sum-min)<<endl;
    }
    return 0;
}
