#include <iostream>
#include <cstdio>
#include <list>

using namespace std;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); i++)
#define FORU(i, n) for (uint i = 0; i < (n); i++)
#define FORR(i, n) for (int i = (n)-1; i >= 0; i--)
#define FORRU(i, n) for (uint i = (n)-1; i >= 0; i--)
#define FOREACH(it, v) for (__typeof__(v.begin()) it = (v).begin(); it != (v).end(); ++it)

int main() {
    int tcases;

    scanf("%d", &tcases);

    for (int tcase = 1; tcase <= tcases; tcase++) {
        int r, k, n;
        int sum = 0;
        list<int> q;
        list<int> qtmp;

        scanf("%d %d %d", &r, &k, &n);
        for (int i = 0; i < n; i++) {
            int g;
            scanf("%d", &g);
            q.push_back(g);
        }

        for (int i = 0; i < r; i++) {
            // FOREACH(it, q) {
                // printf("%d -> ", *it);
            // }
            // printf("\n");

            int x = k;
            qtmp.clear();
            while (q.size() > 0 && q.front() <= x) {
                x -= q.front();
                qtmp.push_back(q.front());
                q.pop_front();
            }

            sum += (k - x);

            q.insert(q.end(), qtmp.begin(), qtmp.end());
        }

        printf("Case #%d: %d\n", tcase, sum);
    }

    return 0;
}
