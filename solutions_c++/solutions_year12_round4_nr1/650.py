#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <cstring>
using namespace std;

const int MAXN = 10100;
long long d[MAXN], l[MAXN], best[MAXN];
bool reach[MAXN];

int main()
{
    int T, N;
    cin>>T;

    for(int t = 1; T--; t++)
    {
        cin>>N;
        memset(best, 0, sizeof(best));

        for(int i = 0; i < N; i++)
            cin>>d[i]>>l[i];
        cin>>d[N];

        memset(reach, false, sizeof(reach));
        best[0] = min(d[0], l[0]);
        reach[0] = true;

        for(int i = 0; i < N; i++)
            if(reach[i])
            {
                //printf("DEBUG %d - %lld\n", i, best[i]);
                for(int j = i+1; j <= N; j++)
                    if(d[j]-d[i] <= best[i])
                    {
                        long long dl = d[j]-d[i];
                        best[j] = max(best[j], min(dl, l[j]));
                        reach[j] = true;
                    }
            }

        printf("Case #%d: %s\n", t, reach[N] ? "YES" : "NO");
    }
    return 0;
}
