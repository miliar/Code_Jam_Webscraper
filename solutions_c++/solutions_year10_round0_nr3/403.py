#include <cstdio>
#include <vector>

using namespace std;

typedef long long bigint;

struct Position {
  bigint groupSize;
  bigint profit;
  bigint profitBefore;
  int nextPos;
  int reached;
};

int main() {
  int nCases, nGroups;
  bigint nRuns, capacity;
  vector<Position> pos;

  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%lld%lld%d", &nRuns, &capacity, &nGroups);
    pos.resize(nGroups);
    for (int i = 0; i < nGroups; i++) {
      scanf("%lld", &pos[i].groupSize);
    }

    bigint load = 0;
    for (int i = 0, j = 0; i < nGroups; i++) {
      for (; j < i + nGroups; j++) {
        int newLoad = load + pos[j % nGroups].groupSize;
        if (newLoad > capacity) break;
        load = newLoad;
      }
      pos[i].nextPos = j % nGroups;
      pos[i].profit = load;
      pos[i].reached = -1;
      load -= pos[i].groupSize;
    }

    int i = 0;
    bigint profit = 0;
    bool cycleFound = false;

    for (bigint iRun = 0; iRun < nRuns;) {
      if (!cycleFound && pos[i].reached != -1) {
        cycleFound = true;
        bigint cycleLength = iRun - pos[i].reached;
        bigint cycleProfit = profit - pos[i].profitBefore;
        bigint nCycles = (nRuns - iRun) / cycleLength;
        profit += cycleProfit * nCycles;
        iRun += cycleLength * nCycles;
      }
      else {
        pos[i].reached = iRun;
        pos[i].profitBefore = profit;
        profit += pos[i].profit;
        i = pos[i].nextPos;
        iRun++;
      }
    }

    printf("Case #%i: %lli\n", iCase, profit);
  }
  return 0;
}
