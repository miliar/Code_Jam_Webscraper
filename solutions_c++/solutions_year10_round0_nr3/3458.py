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
    uint64_t seats = k;
    uint64_t profit = 0;

    cin >> R >> k >> N;

    list<uint64_t> queue, againqueue, nextagainqueue;

    for(uint64_t i=0; i < N; ++i) {
      cin >> ppl;
      queue.push_back(ppl);
    }

    for(uint64_t times=0; times < R; ++times) {
      list<uint64_t> nextagainqueue;

      nextagainqueue.clear();
      seats = k;

      bool didstop = false;
      while(queue.size() > 0) {
        ppl = queue.front();
        if(seats >= ppl) {
          seats -= ppl;
          profit += ppl;
          queue.pop_front();
          nextagainqueue.push_back(ppl);
        } else {
          didstop = true;
          break;
        }
      }

      if(!didstop) {
        while(againqueue.size() > 0) {
          ppl = againqueue.front();
          if(seats >= ppl) {
            seats -= ppl;
            profit += ppl;
            againqueue.pop_front();
            nextagainqueue.push_back(ppl);
          } else {
            break;
          }
        }
      }

      for(list<uint64_t>::iterator it = nextagainqueue.begin(); it != nextagainqueue.end(); ++it)
        againqueue.push_back(*it);
    }

    cout << "Case #" << cas << ": " << profit << endl;
  }

  return 0;
}
