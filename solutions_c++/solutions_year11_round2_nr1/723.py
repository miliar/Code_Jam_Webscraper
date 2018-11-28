#include <cstdio>

using namespace std;

const int maxn = 100 + 10;

int n;
char G[maxn][maxn];

double OWP[maxn];
double OOWP[maxn];

double wp(int i)
{
    int won = 0, played = 0;
    for (int j = 0; j < n; j++) {
        if (G[i][j] != '.') played++;
        if (G[i][j] == '1') won++;
    }
    return (double) won / played;
}

double owp(int i)
{
    if (OWP[i] < 0) {
        //printf("owp(%d)\n", i);
        double wp_sum = 0.0;
        int wp_count = 0;
        for (int j = 0; j < n; j++)
            if (G[i][j] != '.') {
                char val = G[j][i];
                G[j][i] = '.';
                wp_sum += wp(j);
                //printf("adding wp(%d) = %f\n", j, wp(j));
                G[j][i] = val;
                wp_count++;
            }
        OWP[i] = wp_sum / wp_count;
    }
    return OWP[i];
}

double oowp(int i) {
    if (OOWP[i] < 0) {
        double owp_sum = 0.0;
        int owp_count = 0;
        for (int j = 0; j < n; j++)
            if (G[i][j] != '.') {
                owp_sum += owp(j);
                owp_count++;
            }
        OOWP[i] = owp_sum / owp_count;
    }
    return OOWP[i];
}

void printG()
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            printf("%c", G[i][j]);
        printf("\n");
    }
}

void solve()
{
    scanf("%d\n", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            scanf("%c", &G[i][j]);
        scanf("\n");
    }
    for (int i = 0; i < n; i++)
        OWP[i] = OOWP[i] = -1;
    /*
    if (n == 4)
        for (int i = 0; i < n; i++)
            printf("%.10lf\n", owp(i));
    */
    for (int i = 0; i < n; i++)
        printf("%.16f\n",
                0.25 * wp(i) +
                0.50 * owp(i) +
                0.25 * oowp(i));
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d:\n", t);
        solve();
    }
}
