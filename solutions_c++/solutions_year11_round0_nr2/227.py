#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

vector<char> op[256];
map<char, char> tr[256];

int main() {
    int tott, c, d, n;
    char buf[20];

    scanf("%d", &tott);
    for (int curt = 1; curt <= tott; ++curt) {
        for (int i = 0; i < 256; ++i) {
            op[i].clear();
            tr[i].clear();
        }
        scanf("%d", &c);
        for (int i = 0; i < c; ++i) {
            scanf("%s", buf);
            tr[buf[0]][buf[1]] = buf[2];
            tr[buf[1]][buf[0]] = buf[2];
        }
        scanf("%d", &d);
        for (int i = 0; i < d; ++i) {
            scanf("%s", buf);
            op[buf[0]].push_back(buf[1]);
            op[buf[1]].push_back(buf[0]);
        }
        scanf("%d", &n);
        vector<char> s;
        for (int i = 0; i < n; ++i) {
            char ch;
            scanf(" %c", &ch);
            if (!s.empty() && tr[ch].count(s.back())) {
                s.back() = tr[ch][s.back()];
            } else {
                s.push_back(ch);
                for (int j = 0; j < op[ch].size(); ++j) {
                    if (count(s.begin(), s.end() - 1, op[ch][j]) > 0) {
                        s.clear();
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ", curt);
        putchar('[');
        for (int i = 0; i < s.size(); ++i) {
            putchar(s[i]);
            if (i + 1 < s.size()) {
                printf(", ");
            }
        }
        putchar(']');
        putchar('\n');
    }
    return 0;
}

