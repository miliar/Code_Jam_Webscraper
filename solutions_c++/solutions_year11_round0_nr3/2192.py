#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int a[1001];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,j,q,n,res,sum,x;
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>n;
        res=0;
        sum=0;
        for (i=0;i<n;i++)
        {
            cin>>a[i];
            sum=sum^a[i];
            res+=a[i];
        }
        sort(a,a+n);
        printf("Case #%d: ",q+1);
        if (sum==0)
          cout<<res-a[0]<<endl;
        else
          cout<<"NO"<<endl;
    }
    return 0;
}
