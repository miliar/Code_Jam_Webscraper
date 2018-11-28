#include <stdio.h>

int main() {
    int T;
    scanf("%d\n", &T);
    for (int num = 1; num <= T; ++num) {
        int combine[26][26];
        int opp[26][26];
        int C, D, N;
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j) {
                combine[i][j] = 0;
                opp[i][j] = 0;
            }
        scanf("%d", &C);
        for (int i = 0; i < C; ++i) {
            char a, b, c;
            scanf(" %c%c%c", &a, &b, &c);
            combine[a - 'A'][b - 'A'] = c - 'A';
            combine[b - 'A'][a - 'A'] = c - 'A';
        }
        scanf("%d", &D);
        for (int i = 0; i < D; ++i) {
            char a, b;
            scanf(" %c%c", &a, &b);
            opp[a - 'A'][b - 'A'] = 1;
            opp[b - 'A'][a - 'A'] = 1;
        }
        scanf("%d ", &N);
        int tot = 0;
        int list[100];
        for (int i = 0; i < N; ++i) {
            int a;
            char b;
            scanf("%c", &b);
            a = b - 'A';
            if (tot >= 1) {
                if (combine[a][list[tot - 1]] != 0) {
                    list[tot - 1] = combine[a][list[tot - 1]];
                } else {
                    int flag = 0;
                    for (int j = 0; j < tot; ++j)
                        if (opp[list[j]][a] == 1) {
                            flag = 1;
                            tot = 0;
                            break;
                        }
                    if (flag == 0)
                        list[tot++] = a;
                }
            } else {
                list[tot++] = a;
            }
        }


        printf("Case #%d: [", num);

        if (tot == 0) {
            printf("]\n");
        } else {
            for (int i = 0; i < tot - 1; ++i) {
                printf("%c, ", list[i] + 'A');
            }
            printf("%c]\n", list[tot - 1] + 'A');
        }

    }
    return 0;
}
