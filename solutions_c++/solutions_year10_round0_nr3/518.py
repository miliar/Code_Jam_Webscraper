#include <iostream>
using namespace std;

const int maxN = 1000;
long long g[maxN];
long long revenue[maxN];
long long next[maxN];

int main(int argc, char *argv[]) {
  long long T, R, k, N, j, rr, total, starti, loopstarti, looprevenue, looplength, numloops;
  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    cin >> ws >> R >> k >> N >> ws;
    for(int i=0; i<N; i++) {
      cin >> g[i];
    }
    for(int i=0; i<N; i++) {
      revenue[i] = 0;
      j=i;
      while(true) {
        if(revenue[i] + g[j] <= k) {
          revenue[i] += g[j];
        } else {
          break;
        }
        j = (j+1) % N;
        if(j==i) break;
      }
      next[i] = j;
    }
    
    total = 0;
    starti = 0;
    if(R <= maxN) {
      for(int r=0; r<R; r++) {
        total += revenue[starti];
        starti = next[starti];
      }
    } else {
      for(int r=0; r<maxN; r++) {
        total += revenue[starti];
        starti = next[starti];
      }
      rr = maxN;
      loopstarti = starti;
      looprevenue = 0;
      while(true) {
        looprevenue += revenue[starti];
        starti = next[starti];
        rr++;
        if(starti==loopstarti) break;
      }
      looplength = rr - maxN;
      numloops = (R - maxN) / looplength;
      total += numloops * looprevenue;
      starti = loopstarti;
      for(int r=maxN+numloops*looplength; r<R; r++) {
        total += revenue[starti];
        starti = next[starti];
      }
    }
    
    cout << "Case #" << t << ": " << total << endl;
  }
  return 0;
}
