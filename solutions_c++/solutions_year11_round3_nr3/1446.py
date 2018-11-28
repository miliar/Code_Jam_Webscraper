#include<iostream>
using namespace std;

int main()
{
    int t,a[100];
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,l,h;
        cin>>n>>l>>h;
        for(int j=0;j<n;j++)
        {
            cin>>a[j];
        }
        cout<<"Case #"<<i+1<<": ";
        bool done = false;
        for(int j=l;j<=h;j++)
        {
            if(!done)
            for(int k=0;k<n;k++)
            {
                if(j%a[k]==0||a[k]%j==0)
                {
                    if(k+1==n)
                    {
                        cout<<j<<'\n';
                        done = true;
                        break;
                    }
                }
                else break;
            }
        }
        ;if(!done) cout<<"NO\n";
    }
}
