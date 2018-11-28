#include <cstdio>
#include <cstdlib>
#include <algorithm>
using std::sort;


int main()
{
    int T, tIdx;
    scanf("%d", &T);
    int N, nIdx;
    double sum;
    int array[1001];
    int sorted[1001];
    int i, j;
    for (tIdx = 0; tIdx < T; ++tIdx)
    {
        scanf("%d", &N);
        for (nIdx = 0; nIdx < N; ++nIdx)
        {
            scanf("%d", &array[nIdx]);
            sorted[nIdx] = array[nIdx];
        }
        sum = 0;
        sort(sorted, sorted + N);
        for (i = 0; i < N; ++i)
        {
            if (sorted[i] != array[i])
            {
                ++sum;
            }
        }
        printf("Case #%d: %lf\n", tIdx + 1, sum);
    }
    return 0;
}
