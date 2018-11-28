#include <cstdio>

#include <algorithm>
#include <vector>
using namespace std;

#define x first
#define y second

vector< pair<int, int> > v;

void insert(int pos) {
    for (int i = 0; i < v.size(); ++i)
        if (v[i].x == pos) {
            ++v[i].y;
            return;
        }
    v.push_back(make_pair(pos, 1));
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test_no = 1; test_no <= t; ++test_no) {
        int n; scanf("%d", &n);

        v.resize(0);
        for (int i = 0; i < n; ++i) {
            int a, b;
            scanf("%d %d", &a, &b);
            v.push_back(make_pair(a, b));
        }

        sort(v.begin(), v.end());

        int sol = 0;
        while (true) {
            bool finished = true;
            for (int i = 0; i < v.size(); ++i)
                if (v[i].y > 1) {
                    finished = false;

                    int p1 = i, p2 = i;
                    while (p1 > 0 && v[p1 - 1].x + 1 == v[p1].x && v[p1 - 1].y > 0)
                        --p1;
                    while (p2 + 1 < v.size() && v[p2 + 1].x - 1 == v[p2 + 1].y > 0)
                        ++p2;
                    --v[p1].y; --v[p2].y;

                    insert(v[p1].x - 1);
                    insert(v[p2].x + 1);
                    //v.push_back(make_pair(v[p1].x - 1, 1));
                    //v.push_back(make_pair(v[p2].x + 1, 1));

                    sol += p2 - p1 + 1;
                    break;
                }
            if (finished) break;

            sort(v.begin(), v.end());

            /*
            for (int i = 0; i < v.size(); ++i)
                printf("%d %d\n", v[i].x, v[i].y);
            printf("\n");
            */
        }
        printf("Case #%d: %d\n", test_no, sol);
    }
}
