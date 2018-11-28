#include<iostream>

using namespace std;

int n, k;

int main()
{
    int T, Ti;
    freopen("A-large.in", "r", stdin);
    freopen("task1.out.txt", "w", stdout);
    scanf("%d", &T);
    for(Ti = 1; Ti <= T; ++Ti)
    {
        scanf("%d %d", &n, &k);
        printf("Case #%d: %s\n", Ti, k % (1 << n) == (1 << n) - 1 ? "ON" : "OFF");
    }
    return 0;
}
