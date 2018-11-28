#include<iostream>
#include<string>
using namespace std;
int main()
{
    int o,c,j,t,n,mi,i,su;
    cin>>t;
    for(i=0;i<t;i++)
    {
        su=o=0;
        cin>>n;
        for(j=0;j<n;j++)
        {
            cin>>c;
            o=o^c;
            if(j==0)mi=c;
            if(mi>c)mi=c;
            su+=c;
        }
        cout<<"Case #"<<i+1<<": ";
        if(o!=0)cout<<"NO\n";
        else cout<<su-mi<<endl;
    }
}