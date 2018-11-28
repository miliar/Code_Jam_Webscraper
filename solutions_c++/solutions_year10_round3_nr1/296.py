#include <iostream>

using namespace std;

int main()
{
    int i,k,q,t,a[3000],b[3000],kol,n;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>n;
        kol=0;
        for (i=0;i<n;i++)
        {
            cin>>a[i]>>b[i];
        }
        for (i=0;i<n;i++)
          for (k=i;k<n;k++)
            if ((a[i]-a[k])*(b[i]-b[k])<0) kol++;
        printf("Case #%d: ",q+1);
        cout<<kol<<endl;
    }
    return 0;
}
