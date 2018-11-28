#include<iostream>
using namespace std;
int main()
{
    int t,n,i,k,r=0;
    cin>>t;
    bool ok;
    while(t>0)
    {
        r++;
        cin>>n>>k;
        ok=1;
        for(i=0;i<n;i++)
        {
            if((k&(1<<i))==0)
            {
                ok=0;
                break;
            }
        }
        cout<<"Case #"<<r<<": ";
        if(ok) cout<<"ON\n";
        else cout<<"OFF\n";
        t--;
    }
}
