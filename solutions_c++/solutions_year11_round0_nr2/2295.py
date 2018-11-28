#include <cstdio>
#include <list>
#include <cstring>
#include <vector>
using namespace std;

int combo[150][150];
vector<int> oposto[150];
list<int> lista;

int main() {
    int t;
    scanf("%d ", &t);
    for (int k = 0; k < t; k++) {
        memset(combo, 0, sizeof(combo));
        lista.clear();
        for (int i = 0; i < 150; i++) oposto[i].clear();
        int n;
        scanf("%d ", &n);
        char c1, c2, c3;
        for (int i = 0; i < n; i++) {
            scanf("%c%c%c ",&c1, &c2, &c3);
            combo[c1 - 'A'][c2 - 'A'] = c3 - 'A';
            combo[c2 - 'A'][c1 - 'A'] = c3 - 'A';
        }
        scanf("%d ", &n);
        for (int i = 0; i < n; i++) {
            scanf("%c%c ", &c1, &c2);
            oposto[c1 - 'A'].push_back(c2 - 'A');
            oposto[c2 - 'A'].push_back(c1 - 'A');
        }
        scanf("%d ", &n);
        for (int i = 0; i < n; i++) {
            scanf("%c ", &c1);
            if (lista.empty()) {
                lista.push_back(c1 - 'A');
                continue;
            }
            int u;
            u = lista.back();
            if (combo[u][c1 - 'A'] != 0) {
                lista.pop_back();
                lista.push_back(combo[u][c1 - 'A']);
                continue;
            }
            u = c1 - 'A';
            int v;
            bool saiu = false;
            for (list<int>::iterator it = lista.begin(); it != lista.end(); it++) {
                for (int j = 0; j < oposto[u].size(); j++) {
                    v = oposto[u][j];
                    if (v == *it) {
                        lista.clear();
                        saiu = true;
                        break;
                    }
                }
                if (saiu) break;
            }
            if (saiu) continue;
            lista.push_back(u);
        }
        printf("Case #%d: [", k+1);
        bool first = true;
        for (list<int>::iterator it = lista.begin(); it != lista.end(); it++) {
            if (first) {
                printf("%c", *it + 'A');
                first = false;
                continue;
            }
            printf(", %c", *it + 'A');
        }
        printf("]\n");
    }
    return 0;
}
