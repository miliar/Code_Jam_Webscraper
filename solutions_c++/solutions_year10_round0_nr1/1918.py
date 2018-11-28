#include<iostream>
using namespace std;
int main()
{
    int t,n,k,q;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>n>>k;
        /*if(n==1)
        {
            if(k%2==1)
            {
                
            }    
            else
            {
                cout<<"Case #"<<t<<": OFF"
            }    
            continue;
        }
        */    
        q=(1<<n);
        if(k%q==q-1)
        {
            cout<<"Case #"<<i<<": ON"<<endl;
        }   
        else
        {
            cout<<"Case #"<<i<<": OFF"<<endl;
        }  
    }  
    return 0;  
}    
