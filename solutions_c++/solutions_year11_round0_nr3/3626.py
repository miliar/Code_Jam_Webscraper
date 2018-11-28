#include<iostream>
using namespace std;
int main()
{
    long long s,i,j,t,n,c[1001],min;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>n;
        s=0;
        for(j=0;j<n;j++)
                cin>>c[j];
        for(j=0;j<n;j++)
                s=s^c[j];
        if(s!=0)
                cout<<"Case #"<<(i+1)<<": NO\n";
        else
        {
                min=c[0];
                for(j=0;j<n;j++)
                {
                    s=s+c[j];
                    if(c[j]<min)
                                        min=c[j];
                }
                cout<<"Case #"<<(i+1)<<": "<<(s-min)<<"\n";
        }
    }        
    return 0;
}    
