#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> node[5000 * 15 + 1];
char ch[5000 * 15 + 1];
char s[5000];
vector<int> c[16];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int count = 0;
    int L, N, D;
    scanf("%d %d %d", &L, &N, &D);
    node[0] = vector<int>();
    for (int i = 0; i < N; i++) {
        scanf("%s", s);
        int cur = 0;
        for (int j = 0; j < L; j++) {
            bool f = false;
            for (int k = 0; k < node[cur].size(); k++)
                if (s[j] == ch[node[cur][k]]) {
                    cur = node[cur][k];
                    f = true;
                    break;
                }
            if (!f) {
                count++;
                ch[count] = s[j];
                node[cur].push_back(count);
                node[count] = vector<int>();
                cur = count;
            }
        }
    }
    bool e[26];
    for (int i = 0; i < D; i++) {
        int p = 0;
        c[0] = vector<int>();
        c[0].push_back(0);
        for (int j = 1; j < 16; j++) c[j] = vector<int>();
        scanf("%s", s);
        for (int j = 0; j < L; j++) {
            memset(e, false, sizeof e);
            if (s[p] == '(') {
                while (true) {
                    p++;
                    if (s[p] == ')') break;
                    e[s[p] - 'a'] = true;
                }
            } else {
                e[s[p] - 'a'] = true;
            }
            p++;
            int size = (int)c[j].size();
            for (int k = 0; k < size; k++) {
                int lsize = node[c[j][k]].size();
                for (int m = 0; m < lsize; m++) {
                    if (e[ch[node[c[j][k]][m]] - 'a']) {
                        c[j + 1].push_back(node[c[j][k]][m]);
                    }
                }
            }
        }
        sort(c[L].begin(), c[L].end());
        unique(c[L].begin(), c[L].end());
        printf("Case #%d: %d\n", i + 1, c[L].size());
    }
    return 0;
}
