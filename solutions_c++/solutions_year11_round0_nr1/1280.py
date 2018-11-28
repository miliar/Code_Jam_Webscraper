#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <stdio.h>

#define MAX 100

using namespace std;

main() {
  int N, T;
  int bQ[MAX], oQ[MAX], bLen, oLen;
  int bPos, oPos;
  int bTime, oTime;
  int order[MAX];
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> N;
    // Reset values
    bLen = oLen = bTime = oTime = 0;
    bPos = oPos = 1;
    for (int j = 0; j < N; j++) {
      char c; int pos;
      cin >> c >> pos;
      // Mark order of events
      order[j] = c;
      // Add to event queue
      if (c == 'O')
	oQ[oLen++] = pos;
      else
	bQ[bLen++] = pos;
    }

    int oCounter, bCounter;
    oCounter = bCounter = 0;
    for (int j = 0; j < N; j++) {
      if (order[j] == 'O') {
	int dest = oQ[oCounter++];
	// Get time needed to complete event
	int timestep = abs(oPos-dest) + 1;
	// Get time of completion
	oTime = max(bTime + 1, oTime + timestep);
	// Adjust position
	oPos = dest;
      } else {
	int dest = bQ[bCounter++];
	int timestep = abs(bPos-dest) + 1;
	bTime = max(oTime + 1, bTime + timestep);
	bPos = dest;
      }
    }
    printf("Case #%d: %d\n", i+1, max(oTime,bTime));
  }
}
