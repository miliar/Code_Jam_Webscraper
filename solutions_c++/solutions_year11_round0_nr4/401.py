#include <cstdio>
using namespace std;

void solve_case(int case_id)
{
    int i, unstat = 0, n, p;
    scanf("%d", &n);
    for(i = 0; i < n; ++i)
    {
        scanf("%d", &p);
        if(p != i + 1) ++unstat;
    }
    printf("Case #%d: %d.000000\n", case_id, unstat);
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
