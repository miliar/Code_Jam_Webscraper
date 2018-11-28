#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

    int T, N, K, t;
    int periodN;     // ��N��Snapper��(0, 0)���(1, 1)�����ڣ��պ���2^N��

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
