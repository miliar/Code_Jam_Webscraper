#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int cmp(int a,int b)
{
    return a>b;
}
int main()
{
    int t,n,s,p,a[100],i,j,x,y;
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    cin>>t;
    for (x=1;x<=t;x++)
    {
        cin>>n>>s>>p;
        for (i=0;i<n;i++) cin>>a[i];
        sort(a,a+n,cmp);
        y=0;
        if (!s)
        {
            if (!p) y=n;
            else for (i=0;i<n;i++)
            {
                if (!a[i]) break;
                if (a[i]>p*3-3) y++;
                else break;
            }
        }
        else
            for (i=0;i<n;i++)
            {
                if (!a[i]) break;
                if (a[i]>p*3-3) y++;
                else if (a[i]>p*3-5) {y++;s--;}
                if (!s) break;
            }
        cout<<"Case #"<<x<<": "<<y<<endl;
    }
    return 0;
}
