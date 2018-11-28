#include <functional>
#include <algorithm>
#include <utility>
#include <cassert>
#include <cmath>
#include <ctime>

#include <numeric>
#include <iomanip>
#include <complex>
#include <float.h>
#include <cfloat>

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <cstdio>

#include <cstring>
#include <string>

#include <iterator>
#include <vector>
#include <bitset>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

const int MAXN = 10000 + 10;

int N, D, kT;

int pos[MAXN], dist[MAXN], dp[MAXN];

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin >> kT;

    for(int iT = 1; iT <= kT; ++iT) {
        cin >> N;
        for(int i = 0; i < N; ++i)
            cin >> pos[i] >> dist[i];
        cin >> D;
        memset(dp, 0, sizeof(dp));
        dp[0] = pos[0];
        for(int i = 0; i < N; ++i)
            for(int j = i + 1; j < N; ++j) {
                if(pos[i] + dp[i] < pos[j])
                    break;
                int cdist = dist[j];
                if(pos[j] - pos[i] < cdist)
                    cdist = pos[j] - pos[i];
                if(cdist > dp[j])
                    dp[j] = cdist;
            }

        bool ok = false;
        for(int i = 0; i < N; ++i)
            if(dp[i] + pos[i] >= D)
                ok = true;

        if(ok)
            cout << "Case #" << iT << ": " << "YES" << endl; else
            cout << "Case #" << iT << ": " << "NO" << endl; 
    }

    return 0;
}

