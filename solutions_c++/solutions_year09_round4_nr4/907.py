#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int x[3];
int y[3];
int r[3];

double solve(int o, int a, int b)
{
    double d = hypot(x[a]-x[b], y[a]-y[b]);
    return max(1.*r[o], 0.5*(r[a] + r[b] + d));
}

int main()
{
    int T;
    scanf("%d", &T);
    for( int C = 1; C <= T; ++C )
    {
        int n;
        scanf("%d", &n);

        double rv = 1e50;
        for( int i = 0; i !=n; ++i )
            scanf("%d %d %d", &x[i], &y[i], &r[i]);

        switch( n )
        {
        case 1:
            rv = r[0];
            break;
        case 2:
            rv = max(r[0], r[1]);
            break;
        case 3:
            rv = solve(0, 1, 2);
            rv = min(rv, solve(1, 0, 2));
            rv = min(rv, solve(2, 0, 1));
            break;
        }

        printf("Case #%d: %.6f\n", C, rv);
    }

    return 0;
}
