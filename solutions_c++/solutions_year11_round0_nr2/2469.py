#include <iostream>
#include <cstdio>
#include <list>

using namespace std;

int main() {
    int T; scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        int i, j;
        // Initialization
        char combine[26][26];
        for (i = 0; i < 26; ++i) {
            for (j = 0; j < 26; ++j) {
                combine[i][j] = 0;
            }
        }
        int oppose[26][26];
        for (i = 0; i < 26; ++i) {
            for (j = 0; j < 26; ++j) {
                oppose[i][j] = 0;
            }
        }
        int appeared[26];
        for (i=0; i<26; ++i) {
            appeared[i] = 0;
        }

        int C; scanf("%d ", &C);
        for(int Ci = 0; Ci < C; ++Ci) {
            char elem1, elem2, elem3;
            scanf("%c%c%c ", &elem1, &elem2, &elem3);
            combine[elem1 - 'A'][elem2 - 'A'] = elem3;
            combine[elem2 - 'A'][elem1 - 'A'] = elem3;
        }

        int D; scanf("%d ", &D);
        for(int Di = 0; Di < D; ++Di) {
            char elem1, elem2;
            scanf("%c%c ", &elem1, &elem2);
            oppose[elem1 - 'A'][elem2 - 'A'] = 1;
            oppose[elem2 - 'A'][elem1 - 'A'] = 1;
        }

        char list[110];
        list[0] = 0;
        char *s = list;

        int N; scanf("%d ", &N);
        for(int Ni = 0; Ni < N; ++Ni) {
            char c = getchar();
            //printf("Got c as : %c\n", c);
            if(*s != '\0' && combine[c-'A'][*s-'A'] != 0) {
                //printf("Combining %c and %c to %c\n", c, *s, combine[c - 'A'][*s - 'A']);
                appeared[*s - 'A']--;
                *s = combine[c-'A'][*s-'A'];
                //printf("Appeared[%c] = %d\n", *s , appeared[*s - 'A']);
            }
            else {
                int cleared = 0;
                *(++s) = c; // Put character
                for(i = 0; i < 26; ++i) {
                    if(oppose[c-'A'][i] == 1 && appeared[i] >= 1) {
                        // Clear everything.
                        //printf("Opposing %c and %c: Clear\n", c, (char)i + 'A', combine[c - 'A'][*s - 'A']);
                        s = list;
                        for(j = 0; j < 26; ++j) {
                            appeared[j] = 0;
                        }
                        cleared = 1;
                        break;
                    }
                }
                if (cleared == 0) {
                    appeared[c - 'A']++;
                    //printf("Appeared[%c] = %d\n", c, appeared[c - 'A']);
                }
            }
            *(s+1) = '\0';
            //printf("Intermediate result: %s\n", list + 1);
        }
        *++s = '\0';
        printf("Case #%d: [", Ti );
        char *it = list + 1;
        if(*it != '\0') {
            printf("%c", *it);
            ++it;
        }
        while(*it != '\0') {
            printf(", %c", *it);
            ++it;
        }
        printf("]\n");
    }
}
