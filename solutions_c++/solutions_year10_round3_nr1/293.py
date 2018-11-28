#include <iostream>
using namespace std;
int main()
{
    int t,n,ti=0,i,j,p;
    int a[1010],b[1010];
    cin>>t;
    while(t>0)
    {
        t--;
        ti++;
        p=0;
        cin>>n;
        for(i=0;i<n;i++)
            cin>>a[i]>>b[i];
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
            {
                if((a[i]>a[j] && b[i]<b[j]) || (a[i]<a[j] && b[i]>b[j]))
                p++;
            }
        cout<<"Case #"<<ti<<": "<<p<<endl;
    }
}
