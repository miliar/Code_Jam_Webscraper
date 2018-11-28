#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; i++)
    {
        int N, S, p;
        scanf("%d%d%d", &N, &S, &p);
        int t[100];
        for(int j=0; j<N; j++)
            scanf("%d", &t[j]);
        sort(t, t+N);
        int r = 0;
        for(int j=N-1; j>=0; j--)
        {
            if(t[j] >= 3*p-2)
                r++;
            else if(t[j] >= 3*p-4 && S != 0 && t[j] != 0)
            {
                r++;
                S--;
            }
        }
        printf("Case #%d: %d\n", i, r);
    }
    return 0;
}