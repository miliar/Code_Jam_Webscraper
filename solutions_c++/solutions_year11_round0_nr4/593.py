#include <stdio.h>
#include <string.h>
#include <algorithm>

const int MAXN = 1024;

int nums[MAXN];

int rank[MAXN];

int used[MAXN];

class int_comp_t
{
public:

    int_comp_t(int *elems): _elems(elems) {}

    inline bool operator()(int i, int j) const
    {
        return  _elems[i] < _elems[j];
    }
    
private:

    int *_elems;
};

int main(int argc, char *argv[])
{
    int tc;
    scanf("%d", &tc);
    for (int ncase = 1; ncase <= tc; ++ncase)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &nums[i]);
            rank[i] = i;
            used[i] = 0;
        }
        int_comp_t comp(nums);
        std::sort(rank, rank + n, comp);
        int cost = 0;
        for (int i = 0; i < n; ++i)
        {
            if (used[i])
            {
                continue;
            }
            used[i] = 1;
            int j = rank[i];
            int round = 1;
            while (j != i)
            {
                ++round;
                used[j] = 1;
                j = rank[j];
            }
            if (round > 1)
            {
                cost += round;
            }
        }
        printf("Case #%d: %d\n", ncase, cost);
    }
    return 0;
}
