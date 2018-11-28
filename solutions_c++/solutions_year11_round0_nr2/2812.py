#include <cstdio>

int main (void)
{
    int comb[26][26], oppose[26], appears[26];
    char invoke[101], result[101];
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        int C, D, N;
        char input[4];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                comb[i][j] = 0;
            }
            oppose[i] = 0;
            appears[i] = 0;
        }
        scanf("%d", &C);
        if (C > 0) {
            for (int i = 0; i < C; i++) {
                scanf("%s", input);
//                printf("C: %s\t", input);
                char a, b, c;
                a = input[0];
                b = input[1];
                c = input[2];
                comb[a-'A'][b-'A'] = comb[b-'A'][a-'A'] = c;
            }
        }
        scanf("%d", &D);
        if (D > 0) {
            for (int i = 0; i < D; i++) {
                scanf("%s", input);
//                printf("D: %s\t", input);
                char a, b;
                a = input[0];
                b = input[1];
                oppose[a-'A'] = b;
                oppose[b-'A'] = a;
            }
        }
        scanf("%d", &N);
        scanf("%s", invoke);
//        printf("N: %s\n", invoke);
        int len = 0;
        for (int i = 0; i < N; i++) {
            if(len > 0) {
                if (comb[invoke[i]-'A'][result[len-1]-'A'] != 0) {
                    appears[result[len-1]-'A']--;
                    result[len-1] = comb[invoke[i]-'A'][result[len-1]-'A'];
                    appears[result[len-1]-'A']++;
                    continue;
                }
            }
            if (oppose[invoke[i]-'A'] != 0) {
                if (appears[oppose[invoke[i]-'A']-'A'] > 0) {
                    len = 0;
                    for (int j = 0; j < 26; j++) {
                        appears[j] = 0;
                    }
                    continue;
                }
            }
            result[len++] = invoke[i];
            appears[invoke[i]-'A']++;
        }
        printf("Case #%d: [", t);
        if (len > 0) {
            printf("%c", result[0]);
            for (int j = 1; j < len; j++) {
                printf(", %c", result[j]);
            }
        }
        printf("]\n");
    }
    return 0;
}



