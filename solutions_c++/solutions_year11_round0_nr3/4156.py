#include<iostream>
using namespace std;
int main()
{
    int t=0, n=0;
    int tt[1000];
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        int xr=0;
        for(int j=0;j<n;j++)
        {
            cin>>tt[j];
            xr^=tt[j];
        }
        cout<<"Case #"<<i+1<<": ";
        if(xr)  cout<<"NO\n";
        else
        {
            int sum=0, min=tt[0];
            for(int q=0;q<n;q++)
            {
                sum+=tt[q];
                if(tt[q]<min) min=tt[q];
            }
            cout<<sum-min<<'\n';
        }
    }
    return 0;
}
