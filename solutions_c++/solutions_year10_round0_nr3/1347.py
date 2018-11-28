int T, // test cases 
R, // rides per day
k, // max per ride
N; // groups

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int g[1000]; // group size
int e[1000]; // earning (sum of groups, starting from here)
int n[1000]; // next start

int euro(){
  // compute earning per starting point and next starting point
  int t=0; // last
  int ee=0;
  for (int h=0; h<N; h++) {
    while (ee+g[t] <= k && (t!=h || ee==0)) {
      ee+=g[t];
      t=(t+1) % N;
    }
    e[h]=ee, n[h]=t;
    ee-=g[h];
  }
  
  // compute full loop, starting at 0 (and ending at 0)
  int loop_e=0, loop_R=0;
  int loop_start, pre_loop_e, pre_loop_R;
  {
    int h=0;
    set<int> seen;
    vector<int> seq;
    do {
      seen.insert(h);
      seq.push_back(h);
      loop_e += e[h];
      loop_R ++;
      h=n[h];
    } while (seen.find(h) == seen.end());
      loop_start = h;
      // Determine pre-loop sequence
      pre_loop_e = 0;
      pre_loop_R = 0;
      for (h=0; h!=loop_start; h=n[h]) {
        pre_loop_e += e[h];
        pre_loop_R ++;
      }
      loop_e -= pre_loop_e;
      loop_R -= pre_loop_R;
  }
  
  //
  // Compute earning
  //
  ee = 0;
  int h = 0;
  
  // do we have loops?
  if (R >= pre_loop_R + loop_R) {
    // skip pre-loop
    ee += pre_loop_e;
    R -= pre_loop_R;
    h = loop_start;

    // compute number of loops, and remainder
    int loops = R / loop_R;
    ee += loops * loop_e;
    R = R % loop_R;
  }
  
  // follow remainder of runs
  for (; R>0; R--,h=n[h]) {
    ee += e[h];
  }
  
  return ee;
}

int main()
{
  // Input
  scanf("%d\n",&T);
  fprintf(stderr,"T = %d: \n",T);

  // Output
  for (int x=1; x<=T; x++) {
    fprintf(stderr,"Case #%d: \n",x);

    scanf("%d %d %d\n",&R, &k, &N);
    for (int i=0; i<N; i++) {
      scanf("%d",&g[i]);
      assert(g[i] > 0);
    }
    
    printf("Case #%d: %d\n",x,euro());
  }
  return 0;
}
