//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>

using namespace std;

int main()
{
    freopen("inputC.txt","r",stdin);
    freopen("outputC.txt","w",stdout);
    int cas,kas;
    cin>>kas;
    for(cas=0;cas<kas;cas++)
    {
        int n,a,b;
        int ar[10000];
        cin>>n>>a>>b;
        for(int i=0;i<n;i++)
        {
            cin>>ar[i];
        }
        int fl=1;
        printf("Case #%d: ",cas+1);
        for(int i=a;i<=b;i++)
        {
            int fls=1;
            for(int j=0;j<n;j++)
            {
                if(ar[j]%i!=0&&i%ar[j])
                fls=0;
            }

            if(fls){cout<<i<<endl;
            fl=0;
            break;
            }
        }
        if(fl)
        cout<<"NO"<<endl;

    }
}
