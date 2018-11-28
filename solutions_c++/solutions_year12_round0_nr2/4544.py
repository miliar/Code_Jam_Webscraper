#pragma comment(linker, "/stack:64000000")
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    int i,j;
    int ans,n,T,surp,p,googlers;
    int points;
    cin >> T;
    for(i=0;i<T;i++)
    {
        cin >> googlers >> surp >> p;
        ans=0;
        for(j=0;j<googlers;j++)
        {
            cin >> points;
            if(points/3+(points%3>0) >= p){ ans++; }
            else
            {
                if(points < p || surp == 0) continue;
                int a=(points-p)/2;
                if(abs(a-p) <= 2){ ans++; surp--; }
            }
        }

        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
