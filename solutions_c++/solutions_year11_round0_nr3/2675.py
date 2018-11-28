#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{    
    freopen("out.txt", "w", stdout); 
    int T, N;
    scanf("%d", &T);
    
    for(int t = 1; T--; ++t)
    {
        scanf("%d", &N);
        int v, theMin = 10000000, xsum = 0, sum = 0;
        
        for(int i = 0; i < N; i++)
        {
            scanf("%d", &v);
            xsum ^= v;
            sum += v;
            theMin = min(theMin, v);
        }
        
        if(xsum != 0)
            printf("Case #%d: NO\n", t);
        else
            printf("Case #%d: %d\n", t, sum-theMin);
    }
    return 0;
}
