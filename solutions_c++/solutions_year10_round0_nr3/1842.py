#include <iterator>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstdlib> 
#include <fstream>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <limits>
#include <cstring>
#include <cmath>
using namespace std;

typedef long long ll;

void
solve(int testCaseNum)
{
    int R, k, N;
    cin >> R >> k >> N;

    int g;
    vector<int> groupVec;
    for (int i = 0; i < N; ++i) {
        cin >> g;
        groupVec.push_back(g);
    }

    int nextHead[N];
    int rideAll[N];
    memset(rideAll, 0, sizeof(rideAll));

    const ll nAll = accumulate(groupVec.begin(), groupVec.end(), (ll)0);

    if ((ll)k >= nAll) {
        for (int i = 0; i < N; ++i) {
            nextHead[i] = i;
            rideAll[i] = 1;
        }
    }
    else {
        for (int i = 0; i < N; ++i) {
            int rest = k;
            for (int j = i; ; ++j) {
                if (j == N) {
                    j = 0;
                    rideAll[i] = 1;
                }

                rest -= groupVec[j];

                if (rest < 0) {
                    nextHead[i] = j;
                    break;
                }
            }
        }
    }


    int nRideAll = 0;
    int head = 0;
    for (int i = 0; i < R; ++i) {
        if (rideAll[head])
            nRideAll++;

        head = nextHead[head];
    }

    ll ans = (ll)nRideAll * nAll;

    for (int i = 0; i < head; ++i)
        ans += groupVec[i];
    
    cout << "Case #" << testCaseNum << ": " << ans << endl;
}


int
main()
{
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i)
        solve(i);
}
    
