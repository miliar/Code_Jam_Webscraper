#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);

    int t,s,n,p;
    int sco,ans;
    scanf("%d",&t);
    for(int cases = 1;cases <= t;cases++)
    {
        ans = 0;
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&sco);
            sco -= p;
            if(sco<0)continue;
            sco /= 2;
            if(sco>=p) ans++;
            if(sco == p-1) {ans++;}
            if(sco == p-2) if(s) {ans++;s--;}
        }
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
