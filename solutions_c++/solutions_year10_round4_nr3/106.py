#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

set< pair<int, int> > A, B, C;

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test_no = 1; test_no <= t; ++test_no) {
        int r; scanf("%d", &r);

        for (int stp = 0; stp < r; ++stp) {
            int x1, y1, x2, y2;
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

            for (int i = x1; i <= x2; ++i)
                for (int j = y1; j <= y2; ++j)
                    A.insert(make_pair(i, j));
        }

        int sol = 0;
        while (!A.empty()) {
            ++sol;

            B.clear(); C.clear();
            for (set< pair<int, int> >::iterator it = A.begin(); it != A.end(); ++it) {
                int x = it->first;
                int y = it->second;

                // check to see if this one will die
                if (A.find(make_pair(x - 1, y)) == A.end() && A.find(make_pair(x, y - 1)) == A.end())
                    B.insert(make_pair(x, y));

                // check to see if new one is born
                if (A.find(make_pair(x + 1, y - 1)) != A.end())
                    C.insert(make_pair(x + 1, y));
            }

            // delete dead ones
            for (set< pair<int, int> >::iterator it = B.begin(); it != B.end(); ++it)
                A.erase(A.find(*it));
            // insert new ones
            for (set< pair<int, int> >::iterator it = C.begin(); it != C.end(); ++it)
                A.insert(*it);
        }

        printf("Case #%d: %d\n", test_no, sol);
    }
}
