#include <stdio.h>

int a[31];

int main()
{
    int T, n, k, i, re = 1;
	freopen("A-large.in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    a[0] = 1;
    for(i = 1; i <= 30; ++i)
        a[i] = a[i - 1] * 2;
    while(T--) {
        scanf("%d%d", &n, &k);
        if(k % a[n] == a[n] - 1)
            printf("Case #%d: ON\n", re++);
        else
            printf("Case #%d: OFF\n", re++);
    }
    return 0;
}
