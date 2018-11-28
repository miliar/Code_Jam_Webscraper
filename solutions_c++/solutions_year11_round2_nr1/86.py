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

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

double calcWinningProcentage(int team, vector<string> & schedule, int except_team = -1) {
    int wins = 0;
    int games = 0;
    for (int i = 0; i < schedule.size(); ++i) {
        if (i != except_team) {
            games += schedule[team][i] != '.';
            wins += schedule[team][i] == '1';
        }
    }
    if (games == 0)
        return 0.0;
    return 1.0 * wins / games;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int tests; 
    cin >> tests;
    for (int test = 0; test < tests; ++test) { 
        cerr << test << "\n";
        printf("Case #%d:\n", test + 1);
        int n;
        cin >> n;
        vector<string> schedule(n, "");
        for (int i = 0; i < n; ++i)
            cin >> schedule[i];
        vector<double> WP(n);
        for (int i = 0; i < n; ++i) {
            WP[i] = calcWinningProcentage(i, schedule);
        }
        vector<double> OWP(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j && schedule[i][j] != '.')
                    OWP[i] += calcWinningProcentage(j, schedule, i);
            }
            OWP[i] /= double((n - count(all(schedule[i]), '.')));
        }
        vector<double> OOWP(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j)
                if (i != j && schedule[i][j] != '.')
                    OOWP[i] += OWP[j];
            OOWP[i] /= double(n - count(all(schedule[i]), '.'));
        }
        for (int i = 0 ;i < n; ++i) {
            printf("%0.18lf\n",  0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
        }
    }
	return 0;
}