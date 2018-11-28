#include<iostream>
using namespace std;
int main()
{
    int t,n,count=0;
    long long int c,min=1000000,sum=0,sumwr=0; 
    cin>>t;
    while(t--)
    {
              cin>>n;
              while(n--)
              {
                        cin>>c;
                        if(c<min)
                        min=c;
                        sum=sum+c;
                        sumwr=sumwr^c;
                        }
                        count++;
                        if(sumwr==0)
                        cout<<"Case #"<<count<<": "<<sum-min<<"\n";
                        else
                        cout<<"Case #"<<count<<": NO\n";
                        min=1000000;
                        sum=0;
                        sumwr=0;
              }
    return 0;
    }
