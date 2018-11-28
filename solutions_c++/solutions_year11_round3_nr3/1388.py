#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
   int l,test,m,n,a[10005],i,f,j,s,tcase=1;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    cin>>test;
    while(test--)
    {
        cin>>l>>n>>m;
        for(i=0;i<l;i++)
        cin>>a[i];
        f=0;
        for(i=n;i<=m;i++)
        {
            for(j=0;j<l;j++)
            {
                if((a[j]%i==0) ||(i%a[j]==0))
                {
                   // cout<<"i="<<i<<"j="<<j<<endl;
                 s=i;
                 continue;
                }
                else
                break;
                //cout<<j<<endl;
                //if(j+1==l)
                  // f=1;
            }

            if(j==l)
            {
                f=1;
                break;
            }


        }
        cout<<"Case #"<<tcase++<<": ";
        if(f==1)
        {
            cout<<s<<endl;
        }
        else
         cout<<"NO"<<endl;
    }
return 0;
}
