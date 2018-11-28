/*
  ID: nigo1
  LANG: C++
  TASK: B
*/
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <stack>

#define TIME pf("%f", (double)clock()/CLOCKS_PER_SEC);


using namespace std;

int T, W, L, N;

pair <int, int> r[1024];
pair <double, double> ans[1024];
bool used[1024];

void solve1 () {
    memset (used, 0, sizeof used);

    double left = -r[0].first;

    for (int i = 0; i < N; i++) {
        double top = .0;
        bool f = 1;

        for (int j = 0; j < N; j++) {
            if (used[j]) continue;

            if (!f)
                if ((double)r[j].first + top > (double)L) continue;

            used[j] = 1;

            if (!f)
                ans[r[j].second] = make_pair (max (0.0, left + r[j].first), top + r[j].first);
            else
                ans[r[j].second] = make_pair (max (0.0, left + r[j].first), top);

            if (!f)
                top += 2.0*r[j].first;
            else
                top += r[j].first;
           // cout << left << " "<< top << endl;
            f = 0;
        }

        for (int j = 0; j < N; j++)
            left = max (left, ans[r[j].second].first + r[j].first);

    }
}
void solve2 () {
    memset (used, 0, sizeof used);

    double top = -r[0].first;

    for (int i = 0; i < N; i++) {
        double left = .0;
        bool f = 1;

        for (int j = 0; j < N; j++) {
            if (used[j]) continue;

            if (!f)
                if ((double)r[j].first + left > (double)W) continue;

            used[j] = 1;

            if (!f)
                ans[r[j].second] = make_pair (left + r[j].first, max (0.0, top + r[j].first));
            else
                ans[r[j].second] = make_pair (left, max (0.0, top + r[j].first));

            if (!f)
                left += 2.0*r[j].first;
            else
                left += r[j].first;
           // cout << left << " "<< top << endl;
            f = 0;
        }

        for (int j = 0; j < N; j++)
            top = max (top, ans[r[j].second].first + r[j].first);
    }
}
int main()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);

    scanf ("%d", &T);

    for (int test = 1; test <= T; test++) {
        printf ("Case #%d:", test);
        memset (ans, 0, sizeof ans);
        memset (r, 0, sizeof r);
        scanf ("%d%d%d", &N, &W, &L);

        for (int i = 0; i < N; i++) {
            int x;
            scanf ("%d", &x);
            r[i] = make_pair (x, i);
        }

       /* if (test != 26) {
            cout << endl;
            continue;
        }*/
        sort (r, r + N);
        reverse (r, r + N);

        solve1();

        bool s2 = 0;
        for (int i = 0; i < N; i++) {
            printf (" %lf %lf", ans[i].first, ans[i].second);
          // if (ans[i].first > (double)W or ans[i].second > (double)L) s2 = 1, cout << "1";
        }

       /* if (s2) {
            solve2();

            for (int i = 0; i < N; i++) {
                printf (" %lf %lf", ans[i].first, ans[i].second);
              // if (ans[i].first > W or ans[i].second > L) s2 = 1, cout << "2";
            }
        }*/

        printf ("\n");
    }
}
