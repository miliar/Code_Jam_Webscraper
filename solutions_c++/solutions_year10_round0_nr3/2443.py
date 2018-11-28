
#include <cstdio>

#include <queue>
#include <algorithm>
using namespace std;

const int MaxN = 1010;
int g[MaxN]; // 1 ¡Ü gi ¡Ü 10^7

int main()
{
    freopen("in.txt", "r", stdin);freopen("out.txt", "w", stdout);
    int T;
    int R; // run R times in a day. 1 ¡Ü R ¡Ü 10^8.
    int k; // hold k people at once. 1 ¡Ü k ¡Ü 10^9.
    int N; // N groups. 1 ¡Ü N ¡Ü 1000.
    int cnt = 0;

    int i, j;
    queue<int> Q1, Q2; // get on queue, wait queue
    int top, sum;
    int ans;

    scanf("%d", &T);
    while (T--) {
        scanf("%d %d %d", &R, &k, &N);
        for (i = 0; i < N; ++i) {
            scanf("%d", &g[i]);
            Q2.push(g[i]); // wait
        }
        ans = 0;
        for (i = 0; i < R; ++i) {
            sum = 0;
            while (sum < k && !Q2.empty()) {
                top = Q2.front();
                if (sum + top > k) break;
                sum += top;
                Q2.pop();
                Q1.push(top); // get on
            }
            ans += sum;
            while (!Q1.empty()) {
                Q2.push(Q1.front()); // wait
                Q1.pop();
            }
        }
        while (!Q1.empty()) Q1.pop();
        while (!Q2.empty()) Q2.pop();
        printf("Case #%d: %d\n", ++cnt, ans);
    }

    return 0;
}
