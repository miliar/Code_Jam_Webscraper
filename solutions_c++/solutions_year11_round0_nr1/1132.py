#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#define MAX 110

using namespace std;

int op[MAX], op1[MAX], op2[MAX], n1, n2;

int move(const int x, const int d, const int l) {
    return d < 0 ? x - l : x + l;
}

int solve(const int n) {
    int x = 1, y = 1, i = 0, j = 0, k, t = 0;

    for (k = 0; k < n; k++) {
        if (op[k] > 0) {
            t += abs(op1[i] - x) + 1;
            y = move(y, op2[j] - y, min(abs(op1[i] - x) + 1, abs(op2[j] - y)));
            x = op1[i];
            i++;
        } else {
            t += abs(op2[j] - y) + 1;
            x = move(x, op1[i] - x, min(abs(op2[j] - y) + 1, abs(op1[i] - x)));
            y = op2[j];
            j++;
        }
    }

    return t;
}

int main() {
    int t, n, p, i, cnt = 1;
    char buff[10];

    scanf("%d", &t);
    while (t--) {
        n1 = n2 = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s %d", buff, &op[i]);
            if (buff[0] == 'B') op1[n1++] = op[i];
            else {
                op2[n2++] = op[i];
                op[i] = -op[i];
            }
        }
        printf("Case #%d: %d\n", cnt++, solve(n));
    }

    return 0;
}
