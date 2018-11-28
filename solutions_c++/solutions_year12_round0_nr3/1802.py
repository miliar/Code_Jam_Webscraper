#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <cstring>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <cassert>
#include <queue>
#include <iterator>

typedef long long LL;
typedef long double LD;

using namespace std;

const int MAX_A = 2000000;

int main() {
#ifndef LOCAL
//  freopen(".in", "r", stdin);
//  freopen(".out", "w", stdout);
#endif

    vector< pair<int, int> > all;
    for (int i = 1; i <= MAX_A; i++) {
        char buf [20];
        sprintf(buf, "%d", i);
        int k = strlen(buf);
        sprintf(buf + k, "%d", i);
        for (int s = k - 1, j; s >= 0; s--) {
            buf[s + k] = '\0';
            if (buf[s] == '0')
                continue;
            sscanf(buf + s, "%d", &j);
            if (j > i)
                all.push_back(make_pair(i, j));
        }
    }
    sort(all.begin(), all.end());
    all.erase(unique(all.begin(), all.end()));

    int nTests;
    cin >> nTests;

    for (int test = 1; test <= nTests; test++) {
        int a, b;
        cin >> a >> b;

        int cnt = 0;
        for (int j = 0; j < all.size(); j++)
            if (a <= all[j].first && all[j].second <= b)
                cnt++;

        cout << "Case #" << test << ": " << cnt << '\n';
    }

    return 0;
}


