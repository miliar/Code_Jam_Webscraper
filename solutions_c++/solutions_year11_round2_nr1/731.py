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
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

const int MAXN = 105;

int cc;
int n;
char in[MAXN][MAXN];

double wp(int k, int ignore = -1) {
    if (ignore == -1) ignore = k;
    double score = 0;
    int games = 0;
    for (int i = 0; i < n; i++) {
        if (in[k][i] == '.' || i == ignore) continue;
        games++;
        score += in[k][i] - '0';
    }
    return score / games;
}

double owp(int k, int ignore = -1) {
    if (ignore == -1) ignore = k;
    double score = 0;
    int games = 0;
    for (int i = 0; i < n; i++) {
        if (in[k][i] == '.' || i == k) continue;
        games++;
        score += wp(i, ignore);
    }
    return score / games;
}

double oowp(int k, int ignore = -1) {
    if (ignore == -1) ignore = k;
    double score = 0;
    int games = 0;
    for (int i = 0; i < n; i++) {
        if (in[k][i] == '.' || i == k) continue;
        games++;
        score += owp(i, i);
    }
    return score / games;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%s", in[i]);
        cout << "Case #" << cas << ":" << endl;
        cout << setprecision(10);
        for (int i = 0; i < n; i++) {
            double res = 0;
            res = 0.25 * wp(i) + 0.50 * owp(i) + 0.25 * oowp(i);
            cout << fixed << res << endl;
        }
    }
	return 0;
}