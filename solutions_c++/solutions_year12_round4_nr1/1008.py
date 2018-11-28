#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 22222;

int n, d[N], l[N], largest[N], queue[N];
bool visit[N];

int main() {
    int test_count;
    scanf("%d", &test_count);
    for (int test = 1; test <= test_count; ++ test) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++ i) {
            scanf("%d%d", d + i, l + i);
        }
        scanf("%d", d + n);
        for (int i = 0; i < n; ++ i) {
            largest[i] = 0;
        }
        largest[0] = d[0];
        memset(visit, 0, sizeof(visit));
        int head = 0;
        int tail = 0;
        queue[tail ++] = 0;
        while (head != tail) {
            int i = queue[head];
            head = (head + 1) % N;
            visit[i] = false;
            for (int j = 0; j < n; ++ j) {
                if (abs(d[i] - d[j]) <= largest[i] && min(abs(d[i] - d[j]), l[j]) > largest[j]) {
                    largest[j] = min(abs(d[i] - d[j]), l[j]);
                    if (!visit[j]) {
                        visit[j] = true;
                        queue[tail] = j;
                        tail = (tail + 1) % N;
                    }
                }
            }
        }
        bool found = false;
        for (int i = 0; i < n; ++ i) {
            if (d[i] + largest[i] >= d[n]) {
                found = true;
            }
        }
        printf("Case #%d: %s\n", test, found? "YES": "NO");
    }
    return 0;
}
