#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int T, c = 1;
int N, L, H;
int freq[128];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(scanf("%d", &T); T; --T)
    {
        int i, j;

        scanf("%d%d%d", &N, &L, &H);
        for(i = 0; i < N; ++i)
            scanf("%d", freq + i);

        for(i = L; i <= H; ++i)
        {
            for(j = 0; j < N; ++j)
                if(freq[j] % i != 0 && i % freq[j] != 0)
                    break;
            if(j == N)
                break;
        }

        if(i <= H)
            printf("Case #%d: %d\n", c++, i);
        else
            printf("Case #%d: NO\n", c++);

    }
}