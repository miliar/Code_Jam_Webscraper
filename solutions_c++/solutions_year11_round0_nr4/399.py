#include<iostream>
#include<cstdlib>

using namespace std;

int main()
{
  //  freopen("D-large.in","r",stdin);
  //  freopen("D-large.out","w",stdout);
    int t;
    cin>>t;
    for (int ti=0; ti<t; ti++)
    {
        int n,m,x;
        cin>>n;
        m=n;
        for (int i=0; i<n; i++)
        {
            cin>>x;
            if (x==i+1)
                m--;
        }
        cout<<"Case #"<<ti+1<<": "<<m<<".000000"<<endl;
    }
    return 0;
}
            
