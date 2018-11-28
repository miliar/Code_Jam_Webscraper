#include <cstdio>

using namespace std;

bool solve (int N, int K)
{
    for (int i=0; i<N; i++) if (((1<<i) & K) == 0) return false;
    return true;
}

int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    scanf ("%d", &T);
    for (int i=1; i<=T; i++)
    {
        int N,K;
        scanf ("%d %d", &N, &K);
        printf ("Case #%d: ", i);
        if (solve (N, K)) printf ("ON\n"); else printf ("OFF\n");
    }
    return 0;
}
