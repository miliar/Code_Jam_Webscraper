#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

bool hasLetter[10005];
int set[10005];
char word[10005][15];
char list[30];
int points[10005];
pair<int, int> sortby[10005];

int main() {
    int T, t, n, m, i, j, k, x, tmp;

    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; i++) {
            scanf("%s", word[i]);
        }
        printf("Case #%d:", t);
        fprintf(stderr, "case %d / %d\n", t, T);
        for (i = 0; i < m; i++) {
            scanf("%s", list);
            for (j = 0; j < n; j++) set[j] = strlen(word[j]);
            memset(points, 0, sizeof(points));

            for (j = 0; j < 26; j++) {
                memset(hasLetter, 0, sizeof(hasLetter));

                for (k = 0; k < n; k++) {
                    int tmp = 0;
                    for (x = 0; word[k][x]; x++) {
                        if (word[k][x] == list[j]) tmp |= (1<<x);
                    }
                    if (tmp) hasLetter[set[k]] = true;
                    sortby[k] = make_pair((set[k] << 11) + tmp, k);
                }
                for (k = 0; k < n; k++) {
                    if (hasLetter[set[k]] && (sortby[k].first % (1<<11) == 0)) points[k]++;
                }
                sort(sortby, sortby+n);
                set[sortby[0].second] = tmp = 1;
                for (k = 1; k < n; k++) {
                    if (sortby[k].first == sortby[k-1].first) set[sortby[k].second] = tmp;
                    else set[sortby[k].second] = ++tmp;
                }
            }
            int best;
            for (best = j = 0; j < n; j++) if (points[j] > points[best]) best = j;
            printf(" %s", word[best]);
        }
        printf("\n");
    }
    return 0;
}



