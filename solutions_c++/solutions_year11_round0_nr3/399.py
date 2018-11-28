#include <cstdio>
#include <algorithm>
using namespace std;

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    int i, n, A[1024], x = 0;
    scanf("%d", &n);
    for(i = 0; i < n; ++i)
    {
        scanf("%d", &A[i]);
        x = x ^ A[i];
    }
    if(x != 0)
    {
        printf("NO\n");
        return;
    }
    sort(A, A + n);
    int ans = 0;
    for(i = 1; i < n; ++i) ans += A[i];
    printf("%d\n", ans);
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
