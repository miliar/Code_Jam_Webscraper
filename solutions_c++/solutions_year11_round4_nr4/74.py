#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 20) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

const int maxN = 402;

int am[maxN][maxN];
int dp[maxN][maxN];

int solve(int v, int p, vector<vector<int> > & short_al, vector<vector<int> > & al) {
    if (am[v][1])
        return 0;
    int & res = dp[v][p];
    if (res >= 0)
        return res;
    res = 0;
    for (int i = 0; i < short_al[v].size(); ++i) {
        int v2 = short_al[v][i];
        int add = 0;
        for (int j = 0; j < al[v2].size(); ++j) {
            int v3 = al[v2][j];
            if (am[p][v3] == 0 && am[v][v3] == 0 && v3 != v) 
                ++add;
        }
        if (am[v2][1] == 0)
            --add;
        res = max(res, add + solve(v2, v, short_al, al));
    }
    return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        cerr << test << " ";
        int n, m;
        memset(dp, -1, sizeof(dp));
        memset(am, 0, sizeof(am));
        cin >> n >> m;
        vector<vector<int> > al(n, vector<int> (0));
        for (int i = 0; i < m; ++i) {
            int a, b;
            scanf("%d,%d", &a, &b);
            al[a].push_back(b);
            al[b].push_back(a);
            am[a][b] = am[b][a] = 1;
        }
        vector<int> dist_from_home(n, INF);
        dist_from_home[0] = 0;
        queue<int> Q;
        Q.push(0);
        while (!Q.empty()) {
            int v = Q.front();
            Q.pop();
            for (int i = 0; i < al[v].size(); ++i) {
                int v2 = al[v][i];
                if (dist_from_home[v2] == INF) {
                    dist_from_home[v2] = dist_from_home[v] + 1;
                    Q.push(v2);
                }
            }
        }
        vector<int> dist_to_enemy(n, INF);
        dist_to_enemy[1] = 0;
        Q.push(1);
        while (!Q.empty()) {
            int v = Q.front();
            Q.pop();
            for (int i = 0; i < al[v].size(); ++i) {
                int v2 = al[v][i];
                if (dist_to_enemy[v2] == INF) {
                    dist_to_enemy[v2] = dist_to_enemy[v] + 1;
                    Q.push(v2);
                }
            }
        }
        vector<vector<int> > n_al(n, vector<int> (0));
        for (int i = 0; i < n; ++i) {
            for( int j = 0; j < al[i].size(); ++j) {
                int v2 = al[i][j];
                if (dist_from_home[i] + 1 + dist_to_enemy[v2] == dist_from_home[1])
                    n_al[i].push_back(v2);
            }
        }
        printf("Case #%d: ", test + 1);
        printf("%d ", dist_from_home[1] - 1);
        int res = 0;
        res = al[0].size();
        if (am[0][1] == 0)
            --res;
        res += solve(0, 0, n_al, al);
        printf("%d\n", res);

    }

	return 0;
}