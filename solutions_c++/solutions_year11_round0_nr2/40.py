#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char comb[26][26];
bool opposed[26][26];

int main(void) {
    int nC, n;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        memset(comb, 0, sizeof(comb));
        memset(opposed, 0, sizeof(opposed));

        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            char combStr[4];
            scanf("%s", combStr);
            comb[combStr[0] - 'A'][combStr[1] - 'A'] = combStr[2];
            comb[combStr[1] - 'A'][combStr[0] - 'A'] = combStr[2];
        }
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            char oppStr[3];
            scanf("%s", oppStr);
            opposed[oppStr[0] - 'A'][oppStr[1] - 'A'] =
            opposed[oppStr[1] - 'A'][oppStr[0] - 'A'] = true;
        }
        int inputLen;
        char input[101];
        scanf("%d %s", &inputLen, input);

        int count[26];
        char stack[100];
        int sEnd = 0;
        memset(count, 0, sizeof(count));
        for (int i = 0; i < inputLen; ++i) {
            stack[sEnd] = input[i];
            ++sEnd;
            ++count[input[i] - 'A'];

            if (sEnd > 1) {
                if (comb[stack[sEnd - 1] - 'A'][stack[sEnd - 2] - 'A']) {
                    --count[stack[sEnd - 1] - 'A'];
                    --count[stack[sEnd - 2] - 'A'];
                    --sEnd;
                    stack[sEnd - 1] = comb[stack[sEnd] - 'A'][stack[sEnd - 1] - 'A'];
                } else {
                    for (int i = 0; i < 26; ++i) {
                        if (opposed[stack[sEnd - 1] - 'A'][i] && count[i]) {
                            sEnd = 0;
                            memset(count, 0, sizeof(count));
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d: [", cC + 1);
        for (int i = 0; i < sEnd; ++i) {
            if (i) printf(", ");
            printf("%c", stack[i]);
        }
        printf("]\n");
    }
}
