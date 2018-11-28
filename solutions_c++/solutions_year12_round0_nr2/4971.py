#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int num[300];

typedef struct node {
    int score;
    int rem;
} NODE;

NODE nodes[300];

int main()
{
    int T, N, S, p;
    int cases = 1;
    scanf("%d", &T);
    while (T-- > 0) {
        scanf("%d %d %d", &N, &S, &p);
        for (int i = 0; i < N; i++) {
            scanf("%d", &num[i]);
            int avg = num[i] / 3;
            nodes[i].rem = num[i] % 3;
            if (nodes[i].rem == 0) {
                nodes[i].score = avg;
            } else {
                nodes[i].score = avg + 1;
            }
        }
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            if (nodes[i].score == p - 1 && nodes[i].rem != 1 && (nodes[i].score >= 2 || nodes[i].score == 1 && nodes[i].rem != 1)) {
                if (cnt + 1 > S) {
                    break;
                } else {
                    nodes[i].score++;
                    cnt++;
                }
            }
        }
        cnt = 0;
        for (int i = 0; i < N; i++) {
            if (nodes[i].score >= p) {
                cnt++;
            }
        }
        printf("Case #%d: %d\n", cases++, cnt);
    }
}
