using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

int pm[1000003] = {2}, pmc = 1;
bool sv[1000003] = {0};

int main()
{
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    for (int i=3; i<=1000000; i+=2)
    {
        if (!sv[i])
        {
            pm[pmc++] = i;
            if (i<=1000)
            {
                for (int j=i+i; j<=1000000; j+=i) sv[j] = 1;
            }
        }
    }
    int T;
    long long N;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        cin>>N;
        long long maxcnt = 1, mincnt = 0;
        for (int i=0; i<pmc && pm[i]<=N; ++i)
        {
            ++mincnt;
            long long j;
            for (j = pm[i]; j<=N; j*=pm[i]) ++maxcnt;
        }
        mincnt += (mincnt==0);
        printf("Case #%d: ", cas);
        cout << maxcnt-mincnt << endl;
    }
    return 0;
}

