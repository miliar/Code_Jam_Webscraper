#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cn,cas,N,S,p,ti,i,n1,n2,ans, cnt;
    cin >> cas;
    for(cn = 1;cn <= cas;cn++)
    {
        ans = 0;cnt = 0;
        cin >> N >> S >> p; n1 = n2 = 0;
        for(i=0;i<N;i++)
        {
            cin >> ti;
            if(ti >= p + max(0, p - 1) + max(0, p - 1))
               ++ans;
            else if(ti >= p + max(0, p - 2) + max(0, p - 2))
               ++cnt;
        }
        printf("Case #%d: %d\n",cn,ans + min(cnt,S));
    }
}
