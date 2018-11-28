// Use g++

#include <cstdio>
#include <climits>
#include <vector>
#include <utility>

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        scanf("%d", &N);
        vector<int> candies(N);
        for (int i = 0; i < N; ++i)
            scanf("%d", &candies[i]);
        int xorValue = 0;
        ITERATE (it, candies)
            xorValue ^= *it;
        if (xorValue != 0)
            printf("Case #%d: NO\n", testcase);
        else
        {
            int sum = 0;
            ITERATE (it, candies)
                sum += *it;
            int minimum = INT_MAX;
            ITERATE (it, candies)
                minimum = min(minimum, *it);
            printf("Case #%d: %d\n", testcase, sum - minimum);
        }
    }
    return 0;
}
