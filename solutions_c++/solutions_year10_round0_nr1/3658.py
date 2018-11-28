#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,n[10000],i;
    long k[10000],p;
    ofstream f("A-small.out");
    cin>>t;
    for(i=0;i<t;i++)
    cin>>n[i]>>k[i];
    for(i=0;i<t;i++)
    {
                    if((((1<<n[i])-1)&k[i])==((1<<n[i])-1))
                    f<<"Case #"<<(i+1)<<":"<<" "<<"ON"<<"\n";
                    else
                    f<<"Case #"<<(i+1)<<":"<<" "<<"OFF"<<"\n";
                    }
                    }
