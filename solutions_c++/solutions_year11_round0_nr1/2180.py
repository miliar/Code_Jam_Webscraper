#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 110;
int seq_robot[MAXN], seq_p[MAXN];
int orange[MAXN], blue[MAXN];
int o[MAXN], b[MAXN];

int main()
{
    int t;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ++ca)
    {
        int n, n_o, n_b;
        scanf("%d", &n);
        n_o = n_b = 1;
        for (int i = 1; i <= n; ++i)
        {
            scanf(" %c%d", &seq_robot[i], &seq_p[i]);
            if ( seq_robot[i] == 'O' )
                orange[n_o++] = seq_p[i];
            else
                blue[n_b++] = seq_p[i];
        }
        orange[0] = blue[0] = 1;
        for (int i = 1; i < n_o; ++i)
            o[i] = fabs(orange[i]-orange[i-1])+1;
        for (int i = 1; i < n_b; ++i)
            b[i] = fabs(blue[i]-blue[i-1])+1;
        int i_o, i_b, tot;
        i_o = i_b = tot = 0;
        for (int i = 1; i <= n; ++i)
        {
            if ( seq_robot[i] == 'O' )
            {
                tot += o[++i_o];
                b[i_b+1] = max(b[i_b+1]-o[i_o], 1);
            }
            else
            {
                tot += b[++i_b];
                o[i_o+1] = max(o[i_o+1]-b[i_b], 1);
            }
        }
        printf("Case #%d: %d\n", ca, tot);
    }
    return 0;
}
