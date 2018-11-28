#include <iostream>

using namespace std;

int main()
{
    long long c,n,k,aux,pot;
    cin>>c;
    
    for(int i=1; i<=c; i++)
    {
            
            cin>>n>>k;
            //if(k==0) {cout<<"No"<<endl; continue;}
            aux=(1<<n)-1;
            //cout<<"mask "<<aux<<endl;
            pot=1;
            while(pot*2<k) pot<<=1;
            //cout<<"pot  "<<pot<<endl;
            k%=(1<<n);
            //cout<<"   k  "<<k<<endl;
            if(aux==k) cout<<"Case #"<<i<<": ON"<<endl;
            else cout<<"Case #"<<i<<": OFF"<<endl;          
    }
    
    return 0;    
}
