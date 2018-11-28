#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <stdint.h>

using namespace std;

int main(int argc, char *argv[]) {
  int cases;
  cin >> cases;

  for(int cas = 1; cas <= cases; ++cas) {
    uint64_t R, k, N;
    uint64_t ppl;
    uint64_t profit = 0;
    uint64_t lastIndex = 0, queueIndex = 0;
    uint64_t queue[1000];

    cin >> R >> k >> N;


    for(uint64_t i=0; i < N; ++i) {
      cin >> ppl;
      queue[i] = ppl;
    }

    for(uint64_t times=0; times < R; ++times) {
      uint64_t seats = k;
      do {
        seats -= queue[queueIndex];
        profit += queue[queueIndex];
        queueIndex = queueIndex+1 >= N ? 0 : queueIndex+1;
      } while(seats >= queue[queueIndex] && queueIndex != lastIndex);
      lastIndex = queueIndex;
      if(lastIndex == 0) {
        uint64_t ntimes = times+1;
        uint64_t nprofit = profit;
        while(times + ntimes < R) {
          times += ntimes;
          profit += nprofit;
        }
      }
    }

    cout << "Case #" << cas << ": " << profit << endl;
  }

  return 0;
}
