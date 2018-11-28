#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>

using namespace std;

const int MAX_N = 10005;

int n;
int pos[MAX_N];
int lengths[MAX_N];
int maxDist[MAX_N];
int target;

int main() {
    int nCases;
    scanf("%d", &nCases);
    for (int iCase = 1; iCase <= nCases; iCase++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &pos[i], &lengths[i]);
        }
        scanf("%d", &target);
        //cout << "target=" << target << endl;
        
        fill(maxDist, maxDist + n, -1);
        
        assert(pos[0] <= lengths[0]);
        maxDist[0] = pos[0];
        
        bool canReachTarget = false;
        
        for (int i = 0; i < n; i++) {
            if (pos[i] + maxDist[i] >= target) {
                canReachTarget = true;
                break;
            }
            for (int j = i + 1; j < n; j++) {
                if (pos[j] - pos[i] > maxDist[i]) break;
                int dist = min(lengths[j], pos[j] - pos[i]);
                maxDist[j] = max(maxDist[j], dist);
            }
        }

        printf("Case #%i: %s\n", iCase, canReachTarget ? "YES" : "NO");
  }
    return 0;
}
