#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>
#include <vector>
#include <iostream>

using namespace std;

const char *tok = " \t\r\n";

void partition(vector<int> &v, int owners, int &cry, int &larger) {
  int i, sz, sum[4] = {0,0,0,0};

  sz = v.size();
  for(i=0;i<sz;i++) {
    if ((owners & (1 << i)) != 0) {
      sum[0] += v[i];
      sum[2] ^= v[i];
    } else {
      sum[1] += v[i];
      sum[3] ^= v[i];
    }
  }

  if (sum[0] > sum[1]) larger = sum[0]; else larger = sum[1];
  if (sum[2] != sum[3] || sum[0]==0 || sum[1]==0) cry = 1; else cry = 0;
}

int bits(vector<int> &v, int bit) {
  int i, b=0, sz, mask = 1 << bit;
  sz = v.size();
  for(i=0;i<sz;i++)
    if (v[i] & mask != 0)
      b++;
  return b;
}

int main() {
  int T,C,i,j,k,x;
  vector<int> v;   
  int cry,larger,best;

  cin >> T;
  
  for(i=1;i<=T;i++) {
    cin >> C;
    v.clear();
    best = -1;
    cry = 0;
    for(j=0;j<C;j++) {
      cin >> k;
      v.push_back(k);
    }

    for(j=0;j<30;j++) {
      k = bits(v, j);
      if (k%2) {
	cry = 1;
	break;
      }	
    }

    if (cry) {
      printf("Case #%d: NO\n",i);
      continue;
    }

    x = 1;
    for(j=0;j<C-1;j++) x <<= 1;

    // each (2^(C-1)) - 1 partition case
    for(j=0;j<x;j++) {
      partition(v,j,cry,larger);
      if (!cry && larger > best)
	best = larger;
    }

    if (best < 0)
      printf("Case #%d: NO\n",i);
    else
      printf("Case #%d: %d\n",i,best);
  }

  return 0;
}
