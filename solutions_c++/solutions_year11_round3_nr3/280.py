#include <iostream>
#include <cstdio>

using namespace std;

long long a[10000];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,q,n,l,h,k,pos,f,res;
    int i,j;
    cin>>t;
    for (q=0;q<t;q++)
    {
        pos=0;
        cin>>n>>l>>h;
        for (i=0;i<n;i++)
          cin>>a[i];
        for (i=l;i<=h;i++)
        {
            f=1;
            for (j=0;j<n;j++)
              if (i%a[j]!=0 && a[j]%i!=0)
                f=0;
            if (f)
            {
                res=i;
                pos=1;
                break;
            }
        }
        printf("Case #%d: ",q+1);
        if (pos)
          cout<<res<<endl;
        else
          cout<<"NO"<<endl;

    }
    return 0;
}
