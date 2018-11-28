#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum <= T; testnum++)
    {
        printf("Case #%d: ", testnum);

        int N;
        scanf("%d", &N);

        int alc = 0, sum = 0, minv = 1000009;
        for(int i = 0; i < N; i++)
        {
            int v;
            scanf("%d", &v);

            alc ^= v;
            sum += v;
            minv = min(minv, v);
        }

        if(alc)
            printf("NO\n");
        else
            printf("%d\n", sum - minv);

 
    }
    return 0;
}
