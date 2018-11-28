#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <functional>
#include <sstream>
#include <cassert>
using namespace std;

#pragma comment(linker, "/STACK:56777216")

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

int N, S, p;
vector<int> a[100];
int b[100];

int main() {
#ifndef ONLINE_JUDGE
//    freopen("../DefaultProject/1.txt", "rb", stdin);
    freopen("../DefaultProject/B-large.in", "rb", stdin);
    freopen("../DefaultProject/B-large.out", "wb", stdout);
#endif

    int T;
    scanf("%d", &T);
    rep(tc, T) {
        printf("Case #%d: ", tc + 1);

        scanf("%d%d%d", &N, &S, &p);
        rep(i, N) {
            int v;
            scanf("%d", &v);

            a[i].clear();
            int value = v / 3;
            b[i] = v % 3;

            switch (b[i]) {
            case 0:
                a[i].push_back(value); a[i].push_back(value); a[i].push_back(value);
                break;
            case 1:
                a[i].push_back(value); a[i].push_back(value); a[i].push_back(value + 1);
                break;
            case 2:
                a[i].push_back(value); a[i].push_back(value + 1); a[i].push_back(value + 1);
                break;
            default:
                assert(false);
                break;
            }
        }

        vector<bool> processed(N, false);
        rep(i, N) {
            if (S == 0) break;
            if (b[i] == 1) continue;

            if (a[i][2] == p - 1) {
                if (b[i] == 0) {
                    if (a[i][0] > 0 && a[i][2] < 10) {
                        a[i][0]--;
                        a[i][2]++;
                        processed[i] = true;
                    }
                } else {
                    if (a[i][1] > 0 && a[i][2] < 10) {
                        a[i][1]--;
                        a[i][2]++;
                        processed[i] = true;
                    }
                }

                if (processed[i]) {
                    S--;
                }
            }
        }

        while (S > 0) {
            rep(i, N) {
                if (processed[i]) continue;

                switch (b[i]) {
                case 0:
                    if (a[i][0] > 0 && a[i][2] < 10) {
                        a[i][0]--;
                        a[i][2]++;
                        processed[i] = true;
                    }
                    break;
                case 1:
                    if (a[i][0] > 0 && a[i][1] < 10) {
                        a[i][0]--;
                        a[i][1]++;
                        processed[i] = true;
                    }
                    break;
                case 2:
                    if (a[i][1] > 0 && a[i][2] < 10) {
                        a[i][1]--;
                        a[i][2]++;
                        processed[i] = true;
                    }
                    break;
                default:
                    assert(false);
                    break;
                }

                if (processed[i]) {
                    S--;
                }
            }
        }

        int cnt = 0;
        rep(i, N) {
            if (a[i][2] >= p)
                cnt++;
        }

        printf("%d\n", cnt);
    }

    return 0;
}
