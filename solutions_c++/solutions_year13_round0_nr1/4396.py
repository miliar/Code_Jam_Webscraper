#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#define OUT(x) cerr << #x << ": " << (x) << endl
#define SZ(x) ((int)x.size())
#define FOR(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long LL;

int T;
char b[5][5];

const int x1 = 'X' * 4, x2 = 'X' * 3 + 'T';
const int o1 = 'O' * 4, o2 = 'O' * 3 + 'T';

bool done(int sum) {
    if (sum == x1 || sum == x2) {
        printf("X won\n");
        return true;
    }
    if (sum == o1 || sum == o2) {
        printf("O won\n");
        return true;
    }
    return false;
}

bool solve() {
    FOR(i, 4) {
        int sum = 0;
        FOR(j, 4) sum += b[i][j];
        if (done(sum)) return true;
    }
    FOR(j, 4) {
        int sum = 0;
        FOR(i, 4) sum += b[i][j];
        if (done(sum)) return true;
    }
    int sum = 0;
    FOR(i, 4) sum += b[i][i];
    if (done(sum)) return true;
    sum = 0;
    FOR(i, 4) sum += b[i][3 - i];
    if (done(sum)) return true;
    return false;
}

int main() {
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        FOR(i, 4) scanf("%s", b[i]);
        printf("Case #%d: ", id);
        if (solve()) continue;
        int cnt = 0;
        FOR(i, 4) FOR(j, 4) cnt += (b[i][j] == '.');
        if (cnt == 0) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }
    }
    return 0;
}
