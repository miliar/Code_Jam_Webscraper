#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define SIZE(s) int((s).size())
#define FILL0(a) memset(a, 0, sizeof(a))
#define FILL1(a) memset(a, -1, sizeof(a))

typedef pair<int, int> PII;

void constructVals(int M, vector<PII>& nodes, vector<int>& vals) {
    for (int i = (M - 1) / 2 - 1; i >= 0; --i) {
        int chld1 = 2 * (i + 1) - 1;
        int chld2 = 2 * (i + 1);
        if (nodes[i].first == 0) {
            vals[i] = vals[chld1] | vals[chld2];
        }
        else {
            vals[i] = vals[chld1] & vals[chld2];
        }
    }
}

int getRes(int M, int V, int ind, vector<PII>& nodes, vector<int>& vals) {
    if (vals[ind] == V)
        return 0;
    if (ind >= (M - 1) / 2)
        return -1;

    int chld1 = 2 * (ind + 1) - 1;
    int chld2 = 2 * (ind + 1);
    if (nodes[ind].second == 0) {  // not allowed
        if (nodes[ind].first == 0) { // OR
            if (V == 0) {
                int res1 = getRes(M, 0, chld1, nodes, vals);
                int res2 = getRes(M, 0, chld2, nodes, vals);
                if (res1 == -1 || res2 == -1)
                    return -1;
                else
                    return res1 + res2;
            }
            else {
                int res1 = getRes(M, 1, chld1, nodes, vals);
                int res2 = getRes(M, 1, chld2, nodes, vals);
                if (res2 != -1 && (res1 == -1 || res2 < res1))
                    res1 = res2;
                return res1;
            }
        }
        else {  // AND
            if (V == 0) {
                int res1 = getRes(M, 0, chld1, nodes, vals);
                int res2 = getRes(M, 0, chld2, nodes, vals);
                if (res2 != -1 && (res1 == -1 || res2 < res1))
                    res1 = res2;
                return res1;
            }
            else {
                int res1 = getRes(M, 1, chld1, nodes, vals);
                int res2 = getRes(M, 1, chld2, nodes, vals);
                if (res1 == -1 || res2 == -1)
                    return -1;
                else
                    return res1 + res2;
            }
        }
    }
    else {  // allowed
        if (nodes[ind].first == 0) { // OR
            if (V == 0) {
                int res1 = getRes(M, 0, chld1, nodes, vals);
                int res2 = getRes(M, 0, chld2, nodes, vals);
                int res = res1;
                if (res2 != -1 && (res == -1 || res2 < res))
                    res = res2;
                if (res == -1)
                    return res;
                ++res;
                if (res1 != -1 && res2 != -1)
                    res = min(res, res1 + res2);
                return res;
            }
            else {
                int res1 = getRes(M, 1, chld1, nodes, vals);
                int res2 = getRes(M, 1, chld2, nodes, vals);
                int res = res1;
                if (res2 != -1 && (res == -1 || res2 < res))
                    res = res2;
                return res;
            }
        }
        else {  // AND
            if (V == 0) {
                int res1 = getRes(M, 0, chld1, nodes, vals);
                int res2 = getRes(M, 0, chld2, nodes, vals);
                int res = res1;
                if (res2 != -1 && (res == -1 || res2 < res))
                    res = res2;
                return res;
            }
            else {
                int res1 = getRes(M, 1, chld1, nodes, vals);
                int res2 = getRes(M, 1, chld2, nodes, vals);
                int res = res1;
                if (res2 != -1 && (res == -1 || res2 < res))
                    res = res2;
                if (res == -1)
                    return res;
                ++res;
                if (res1 != -1 && res2 != -1)
                    res = min(res, res1 + res2);
                return res;
            }
        }
    }
}

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int M, V;
        cin >> M >> V;
        vector<PII> nodes(M);
        vector<int> vals(M);
        int nd = 0;
        for (int j = 0; j < (M - 1) / 2; ++j) {
            int G, C;
            cin >> G >> C;
            nodes[nd].first = G;
            nodes[nd].second = C;
            ++nd;
        }
        for (int j = 0; j < (M + 1) / 2; ++j) {
            int I;
            cin >> I;
            nodes[nd].first = I;
            vals[nd] = I;
            ++nd;
        }

        constructVals(M, nodes, vals);
        int res = getRes(M, V, 0, nodes, vals);
        if (res == -1) {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
        else {
            printf("Case #%d: %d\n", i, res);
        }
    }

    return 0;
}
