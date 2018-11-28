#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main()
{
    //freopen("C-small-test.in","r",stdin);
    freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-large.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    //freopen("C-large.out","w",stdout);
    int T, N;

    scanf("%d",&T);

    for(int TT=0; TT<T; ++TT)
    {
        scanf("%d",&N);
        vector<int> candies(N);

        for(int i=0; i<N; ++i)
        {
            scanf("%d",&candies[i]);
        }

        int sz = (1 << N) - 1, maxi = -1;
        for(int i=1; i<sz; ++i)
        {
            int sa = 0, sb = 0, pa = 0, pb = 0, c = i;
            for(int j=0; j<N; ++j, c>>=1)
            {
                if((c&1)>0)
                {
                    sa ^= candies[j];
                    pa += candies[j];
                }
                else
                {
                    sb ^= candies[j];
                    pb += candies[j];
                }
            }
            if(sa == sb)
            {
                maxi = max(maxi, max(pa, pb));
            }
        }

        if(maxi == -1)
        {
            printf("Case #%d: NO\n", TT + 1);
        }
        else
        {
            printf("Case #%d: %d\n", TT + 1, maxi);
        }
    }

    return 0;
}
