#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

char sc[4], tmp[300], arr[300], sd[300];
int C, t, D, N, num2;
char to[300][300];
string s;
bool op[300][300];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int xx = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &C);
        memset(op, 0, sizeof(op));
        for (int i = 'A'; i <= 'Z'; i++) {
            for (int j = 'A'; j <= 'Z'; j++) {
                to[i][j] = '~';
            }
        }
        for (int i = 0; i < C; i++) {
            scanf("%s", sc);
            to[sc[0]][sc[1]] = to[sc[1]][sc[0]] = sc[2];
        }
        scanf("%d", &D);
        for (int i = 0; i < D; i++) {
            scanf("%s", sd);
            op[sd[0]][sd[1]] = op[sd[1]][sd[0]] = 1;
        }
        scanf("%d", &N);
        cin >> s;
        int num = 0;
        for (int i = 0; i < N; i++) {
            arr[num++] = s[i];
            if (num >= 2) {
                char next = to[arr[num - 2]][arr[num - 1]];
                if (next != '~') {
                    num -= 2;
                    arr[num++] = next;
                }
            }
            num2 = 0;
            bool del = 0;
            for (int j = num - 2; j >= 0; j--) {
                if (op[arr[j]][arr[num - 1]]) {
                    num2 = 0;
                    del = 1;
                    break;
                }
            }
            if (!del) {
                for (int j = 0; j < num; j++) tmp[num2++] = arr[j];
            }
            num = num2;
            for (int j = 0; j < num; j++) arr[j] = tmp[j];
        }
        printf("Case #%d: [", xx++);
        for (int i = 0; i < num; i++) {
            if (i > 0) printf(", ");
            printf("%c", arr[i]);
        }
        printf("]\n");
    }
    return 0;
}
