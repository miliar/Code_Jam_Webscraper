#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
 using namespace std;
#define FOR(a,with,b) for(a=with;a<b;a++)

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int x,y,v,sum,valu,i,j,k,m,n,ar[3000];
    k=1;
    cin>>n;

    while(n--)
    {
        cin>>m;

        FOR(i,0,m)
                  { cin>>valu;
                    ar[i]=valu;
                  }
        x=ar[0];
        FOR(i,1,m)
                {
                        y=ar[i];
                        v=x^y;
                        x=v;
                }
        if(x)
              {       cout<<"Case #"<<k<<": NO"<<endl;
                      goto out;
              }

        sort(&ar[0],&ar[m]);
        sum=0;
        FOR(j,1,m)
            sum+=ar[j];
        cout<<"Case #"<<k<<": "<<sum<<endl;

        out:;
        k++;
    }
    return 0;
}
