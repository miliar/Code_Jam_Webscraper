// vim:set ts=8 sw=4 et smarttab:
// Round 3 2012

#include <cstdio>
#include <algorithm>

int n;
int time[1000], prob[1000], idx[1000];

struct comp
{
    bool operator() (const int &lhs, const int &rhs) const
    {
        if (prob[lhs] != prob[rhs])
        {
            return prob[lhs] > prob[rhs];
        }
        else
        {
            return lhs < rhs;
        }
    }
};

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &time[i]);
        }
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &prob[i]);
        }
        for (int i = 0; i < n; ++i)
        {
            idx[i] = i;
        }
        std::sort(idx, idx + n, comp());
        printf("Case #%d:", tc);
        for (int i = 0; i < n; ++i)
        {
            printf(" %d", idx[i]);
        }
        printf("\n");
    }
}
