#include <iostream>
#include <vector>
#define MAXN 32

using namespace std;

int n, test, k;
pair<int, int> a[MAXN];

void init() {
     int i;
     for (i = 0; i <= n; i++) {
         a[i].first = 0;
         a[i].second = 0;
     }
     a[1].first = 1;
}

int main() {
    int i, j, t;

    freopen("tmp.in", "rt", stdin);
    freopen("tmp.out", "wt", stdout);

    cin >> test;
    for (i = 0; i < test; i++) {
        cin >> n >> k;
        init();
        for (j = 0; j < k; j++) {
            for (t = 1; t <= n; t++) {
                if (a[t].first == 1)
                   a[t].second = !a[t].second;
            }

            for (t = 2; t <= n; t++) {
                if (a[t - 1].first == 1 && a[t - 1].second == 1)
                   a[t].first = 1;
                else
                   a[t].first = 0;
            }
        }
        printf("Case #%d: ", i + 1);
        if (a[n].first == 1 && a[n].second == 1)
           printf("ON\n");
        else printf("OFF\n");
    }    
 return 0;
}
