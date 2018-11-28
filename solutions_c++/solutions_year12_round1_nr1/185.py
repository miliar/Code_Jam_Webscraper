#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    int T, A, B;
    scanf("%d", &T);

    for(int t = 1; T--; t++)
    {
        scanf("%d%d", &A, &B);
        double ans = B+2, mp = 1, p;

        for(int i = 0; i < A; i++)
        {
            double cost = (1-mp)*(B+1) + (A-i) + (B-i) + 1;
            ans = min(ans, cost);
            scanf("%lf", &p);
            mp *= p;
        }

        ans = min(ans, mp*(B-A+1)+(1-mp)*(2*B-A+2));
        printf("Case #%d: %.6f\n", t, ans);
    }
    return 0;
}
