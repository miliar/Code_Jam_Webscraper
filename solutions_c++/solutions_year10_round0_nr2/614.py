#include <iostream>
#include <algorithm>
using namespace std;

int lcd(int a, int b) // b != 0
{
    if (a*b == 0) return max(a, b);

    int r = a % b;
    while (r) {
        a = b;
        b = r;

        r = a % b;
    }

    return b;
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small.out1.txt", "w", stdout);

    int C, N, t[1000];
    int y, maxfactor;
    int c, i;

    scanf("%d", &C);
    for (c = 1; c <= C; ++ c) {
        scanf("%d", &N);
        for (i = 0; i < N; i ++){
            scanf("%d", &t[i]);
        }
        sort(t, t + N);

        if (N == 2) {
            if (t[0] == t[1]) y = 0;
            else {
                maxfactor = t[1] - t[0];
                y = t[0] % maxfactor;
                if (y != 0) y = maxfactor - y;
            }
        } else {
            maxfactor = lcd(t[1]-t[0], t[2]-t[1]);
            y = t[0] % maxfactor;
            if (y != 0) y = maxfactor - y;
        }

        printf("Case #%d: %d\n", c, y);
    }

    fclose(stdin);
	fclose(stdout);

    return 0;
}
