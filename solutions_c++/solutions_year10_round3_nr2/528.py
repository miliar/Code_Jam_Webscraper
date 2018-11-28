#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-Small.out.txt", "w", stdout);

    int T, L, P, C;
    int m, n, l;

    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d%d", &L, &P, &C);

        m = 0, l = L;
        while (l*C < P) {
            l *= C;
            m ++;
        }   // 求得中间节点数

        n = 0, l = 1;
        while (l <= m) {
            l *= 2;
            n ++;
        }

        printf("Case #%d: %d\n", t, n);
    }

    fclose(stdin);
	fclose(stdout);

    return 0;
}
