#include <cstdio>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int main() {
    int T, C, D, N;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        map<pair<char,char>, char> combinations;
        set<pair<char,char> > oppositions;
        scanf("%d", &C);
        for (int j = 0; j < C; j++) {
            char combine[10];
            scanf("%s", combine);
            assert(strlen(combine) == 3);
            char result = combine[2];
            combine[2] = '\0';
            assert(strlen(combine) == 2);
            combinations[make_pair(combine[0], combine[1])] = result;
            combinations[make_pair(combine[1], combine[0])] = result;
        }
        scanf("%d", &D);
        for (int j = 0; j < D; j++) {
            char oppose[10];
            scanf("%s", oppose);
            assert(strlen(oppose) == 2);
            oppositions.insert(make_pair(oppose[0], oppose[1]));
            oppositions.insert(make_pair(oppose[1], oppose[0]));
        }
        scanf("%d", &N);
        char sequence[200];
        scanf("%s", sequence);

        char result[200];
        int j = 0;
        for (char* seq = sequence; *seq; seq++) {
            result[j] = *seq;
            if (j < 1) {
                j++;
                continue;
            }
            if (combinations.find(make_pair(result[j], result[j-1])) != combinations.end()) {
                result[j-1] = combinations[make_pair(result[j], result[j-1])];
            } else {
                // oppositions?
                bool f = false;
                for (int k = 0; k < j; k++) {
                    pair<char,char> p = make_pair(result[k], result[j]);
                    if (oppositions.find(p) != oppositions.end()) {
                        j = 0;
                        f = true;
                        break;
                    }
                }
                if (!f) j++;
            }
        }
        result[j] = '\0';
        printf("Case #%d: [", i+1);
        for (j = 0; result[j]; j++) {
            if (j > 0) printf(", ");
            printf("%c", result[j]);
        }
        printf("]\n");
    }
    return 0;
}
