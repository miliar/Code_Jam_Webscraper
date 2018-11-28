#include <cstdio>
#include <string>

using namespace std;


int main() {
    int t, i, j, k, ncombine, nopposed, nchars;
    char n[128], combine[64][4], opposed[64][4];
    string s;
    string::iterator it;
    bool find;

    scanf("%d", &t);
    for (i = 1; i <= t; i++) {
        scanf("%d", &ncombine);
        for (j = 0; j < ncombine; j++) {
            scanf("%s", combine[j]);
        }
        scanf("%d", &nopposed);
        for (j = 0; j < nopposed; j++) {
            scanf("%s", opposed[j]);
        }
        scanf("%d %s", &nchars, n);

        s = "";
        for (j = 0; j < nchars; j++) {
            s += n[j];
            if (s.size() > 1) {
                find = 0;
                for (k = 0; k < ncombine; k++) {
                    if ((s.at(s.size()-1) == combine[k][0] && s.at(s.size()-2) == combine[k][1]) ||
                        (s.at(s.size()-1) == combine[k][1] && s.at(s.size()-2) == combine[k][0])) {
                            s.erase(s.end()-2, s.end());
                            s += combine[k][2];
                            find = 1;
                            break;
                        }
                }
                if (!find) {
                    for (k = 0; k < nopposed; k++) {
                        if (s.at(s.size()-1) == opposed[k][0]) {
                            for (it = s.begin(); it != s.end(); it++) {
                                if (*it == opposed[k][1]) {
                                    s.clear();
                                    find = 1;
                                    break;
                                }
                            }
                        } else if(s.at(s.size()-1) == opposed[k][1]) {
                            for (it = s.begin(); it != s.end(); it++) {
                                if (*it == opposed[k][0]) {
                                    s.clear();
                                    find = 1;
                                    break;
                                }
                            }
                        }
                        if (find) {
                            break;
                        }
                    }
                }
            }
        }

        if (s.size() == 0) {
            printf("Case #%d: []\n", i);
        } else if (s.size() == 1) {
            printf("Case #%d: [%c]\n", i, s.at(0));
        } else {
            printf("Case #%d: [", i);
            for (j = 0; j < s.size()-1; j++) {
                printf("%c, ", s.at(j));
            }
            printf("%c]\n", s.at(j));
        }
    }

    return 0;
}
