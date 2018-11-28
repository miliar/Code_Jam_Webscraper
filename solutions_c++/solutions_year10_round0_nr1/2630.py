#include<iostream>
using namespace std;
int main()
{
    long long int power(int,int);
    int t;
    cin>>t;
    for(int i=0;i<t;++i)
    {
     int n=0;
     long long k=0;
     cin>>n>>k;
     if(((k+1)%(power(2,n)))==0) cout<<"Case #"<<i+1<<": "<<"ON"<<endl; 
     else   cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;    
    }
}
long long int power(int a,int n)
{
    long long int s=1;
    for(int i=0;i<n;++i)
    {
            s*=a;
    }
    return s;
}
