#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

    int T, N, K, t;
    int periodN;     // 第N个Snapper由(0, 0)变成(1, 1)的周期，刚好是2^N。

    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        scanf("%d%d", &N, &K);

        periodN = (1 << N);

        if ((K+1) % periodN == 0) {
            printf("Case #%d: ON\n", t);
        } else {
            printf("Case #%d: OFF\n", t);
        }
    }

	fclose(stdin);
	fclose(stdout);

	return 0;
}
