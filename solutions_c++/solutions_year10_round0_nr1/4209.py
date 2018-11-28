#include <iostream>
#include <cstdio>
using namespace std;

int n, k, t, a[31];
bool q;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    for (int turn = 1; turn <= t; turn++)
    {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++)
        {
            a[i] = k & 1;
            k >>= 1;
        }
        q = true;
        for (int i = 0; i < n; i++)
            if (a[i] == 0)
            {
                     q = false;
                     break;
            }
        printf("Case #%d: ", turn);
        if (q) printf("ON\n");
        else printf("OFF\n");
    }
    return 0;
}
            
