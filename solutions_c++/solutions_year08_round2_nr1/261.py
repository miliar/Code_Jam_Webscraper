#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long x[100010];
long long y[100010];

int main( void )
{
    int N;
    scanf( "%d", &N );

    for (int tc = 0; tc < N; tc++)
    {
        int n, A, B, C, D, x0, y0, M;
        scanf( "%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M );

        x[0] = x0;
        y[0] = y0;
        for (int i = 1; i < n; i++)
        {
            x[i] = (int)((long long)(A * x[i-1] + B) % (long long)M);
            y[i] = (int)((long long)(C * y[i-1] + D) % (long long)M);
        }

        int cnt = 0;
        for (int i = 0; i < n-2; i++) for (int j = i+1; j < n-1; j++) for (int k = j+1; k < n; k++)
        {
            if (((x[i] + x[j] + x[k]) % 3 == 0) && ((y[i] + y[j] + y[k]) % 3 == 0))
            {
                cnt++;
            }
        }

        printf( "Case #%d: %d\n", tc+1, cnt );
    }
}
