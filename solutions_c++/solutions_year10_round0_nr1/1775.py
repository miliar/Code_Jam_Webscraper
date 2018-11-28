#include <iostream>

using namespace std;

int main()
{
    int t,n,k,q,j,c;
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>n>>k;
        c=0;
        for (j=0;j<n;j++)
        {
            c=k%2;
            if (c==0) break;
            k=k/2;
        }
        printf("Case #%d: ",q+1);
        if (c==1) cout<<"ON"<<endl;
        else cout<<"OFF"<<endl;
    }
    return 0;
}
