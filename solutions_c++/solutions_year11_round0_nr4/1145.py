#include <iostream>
using namespace std;
int main()
{
    int i,j,k,t,n,p;
    cin>>t;
    for (i=1;i<=t;i++)
    {
        cin>>n;
        k=0;
        for (j=1;j<=n;j++)
        {
            cin>>p;
            if (p!=j) k++;
        }
        cout<<"Case #"<<i<<": "<<k<<".000000"<<endl;
    }
}
