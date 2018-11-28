#include<iostream>

using namespace std;
#define N  10000
typedef unsigned long long ll;

int main()
{
    int n,t;
    ll c[N];
    int q=1,exor;
    unsigned long long sum=0,min;
    cin>>t;
    while(t-->=1)
    {
                 cin>>n;
                 long i;
                 exor=0;sum=0;
                 min=10000000;
                 for(i=0;i<n;i++)
                 {
                  cin>>c[i];
                  
                  sum+=c[i];
                  if(min>c[i])
                              min=c[i];
                  exor=exor^c[i];
                 }
                 if(exor==0)
                 cout<<"Case #"<<q<<": "<<sum-min;
                 else
                 cout<<"Case #"<<q<<": NO";
                 cout<<endl;
                 q++;
    }
    cin>>n;
    return 0;
}
