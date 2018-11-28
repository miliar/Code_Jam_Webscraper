#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

const int maxs = 200;
const int maxq = 2000;
const int maxl = 1000000;
const int inf = 0x7fffffff;

int opt[maxq][maxs];
string list[maxs];
char str[maxl];
int s, q, len;

void Init() {
     len = 0;
     scanf("%d", &s);
     gets(str);
     int i;
     for (i = 0; i < s; i++) {
         gets(str);
         list[len++] = str;
     }
     sort(list, list + len);
     len = unique(list, list + len) - list;
}

void Work() {
     int i, j, k, l;
     for (i = 0; i < s; i++)
         opt[0][i] = 0;
     scanf("%d", &q);
     gets(str);
     string curr;
     for (i = 1; i <= q; i++) {
         gets(str);
         curr = str;
         k = lower_bound(list, list + len, curr) - list;
         for (j = 0; j < s; j++)
             opt[i][j] = inf;
         for (j = 0; j < s; j++)
             if (opt[i - 1][j] < inf)
                if (j != k) opt[i][j] <?= opt[i - 1][j];
                else {
                     for (l = 0; l < s; l++)
                         if (l != k) opt[i][l] <?= opt[i - 1][j] + 1;
                }
     }
     int ans = inf;
     for (i = 0; i < s; i++)
         ans <?= opt[q][i];
     printf("%d\n", ans);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        Init();
        Work();
    }
    return 0;
}
