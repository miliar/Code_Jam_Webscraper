#include <cstdio>

using namespace std;

const int MAXN = 30;

int *N;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d/n", &t);
    N = new int[MAXN];
    N[0] = 1;
    for (int i = 1; i < MAXN; i++)
         N[i] = 2 * N[i-1] + 1;
    
    for (int i = 0; i < t; i++) {
        int n, k;
        scanf("%d %d/n", &n, &k);
        printf("Case #%d: ", i + 1);
        if ((k + 1) % (N[n - 1] + 1) == 0)
           printf("ON\n");
        else printf("OFF\n");
    }
    return 0;
}
