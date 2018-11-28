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
    uint64_t N, K;
    cin >> N >> K;

    bool snappers[40];

    for(uint64_t i = 0; i < N; ++i)
      snappers[i] = false;

    for(uint64_t i = 0; i < K; ++i) {
      for(uint64_t j = 0; j <= N; ++j) {
        if(j == N) {
          for(uint64_t k = 0; k < j; ++k)
            snappers[k] = false;
        } else {
          if(snappers[j] == false) {
            for(uint64_t k = 0; k < j; ++k)
              snappers[k] = false;
            snappers[j] = true;
            break;
          }
        }
      }
      /*for(uint64_t j=0;j<N;++j) {
        cout << (snappers[j] ? "1" : "0");
      }
      cout << endl;*/
    }

    bool on = true;
    for(uint64_t i = 0; i < N; ++i) {
      if(!snappers[i]) {
        on = false;
        break;
      }
    }

    cout << "Case #" << cas << ": " << (on ? "ON" : "OFF") << endl;
  }

  return 0;
}
