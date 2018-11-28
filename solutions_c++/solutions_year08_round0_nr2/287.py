#include <cstdio>
#include <algorithm>

#define BUFFER_SIZE 1024

using namespace std;

char buffer[BUFFER_SIZE];

int requiredA[1440], requiredB[1440];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int turn;
        scanf("%d", &turn);
        int n, m;
        scanf("%d%d", &n, &m);
        gets(buffer);
        memset(requiredA, 0, sizeof(requiredA));
        memset(requiredB, 0, sizeof(requiredB));
        for (int i = 0; i < n; i++) {
            gets(buffer);
            int start = ((buffer[0] - '0') * 10 + buffer[1] - '0') * 60 + (buffer[3] - '0') * 10 + buffer[4] - '0';
            int end = ((buffer[6] - '0') * 10 + buffer[7] - '0') * 60 + (buffer[9] - '0') * 10 + buffer[10] - '0';
            requiredA[start]++;
            if (end + turn < 1440) requiredB[end + turn]--;
        }

        for (int i = 0; i < m; i++) {
            gets(buffer);
            int start = ((buffer[0] - '0') * 10 + buffer[1] - '0') * 60 + (buffer[3] - '0') * 10 + buffer[4] - '0';
            int end = ((buffer[6] - '0') * 10 + buffer[7] - '0') * 60 + (buffer[9] - '0') * 10 + buffer[10] - '0';
            requiredB[start]++;
            if (end + turn < 1440) requiredA[end + turn]--;
        }

        int curA = 0, curB = 0, resA = 0, resB = 0;

        for (int i = 0; i < 1440; i++) {
            curA += requiredA[i];
            curB += requiredB[i];

            resA = max(curA, resA);
            resB = max(curB, resB);
        }

        printf("Case #%d: %d %d\n", test + 1, resA, resB);
    }
    return 0;
}
