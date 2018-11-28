// g++ -Wall -O2

#include <vector>
#include <algorithm>
#include <functional>
#include <cstdio>

using namespace std;

struct Level
{
    int index;
    int l;
    int p;
};

struct Earlier : binary_function<Level, Level, bool>
{
    bool operator() (const Level& a, const Level& b) const
    {
        if (a.l * b.p != b.l * a.p)
            return (a.l * b.p < b.l * a.p);
        else
            return (a.index < b.index);
    }
};

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        scanf("%d", &N);
        vector<Level> levels(N);
        for (int i = 0; i < N; ++i)
            levels[i].index = i;
        for (int i = 0; i < N; ++i)
            scanf("%d", &levels[i].l);
        for (int i = 0; i < N; ++i)
            scanf("%d", &levels[i].p);
        sort(levels.begin(), levels.end(), Earlier());
        printf("Case #%d:", testcase);
        for (int i = 0; i < N; ++i)
            printf(" %d", levels[i].index);
        putchar('\n');
    }
    return 0;
}
