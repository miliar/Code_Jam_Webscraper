/*
/* Author: Giacomo Spigler
/* Contest: Google Code Jam 2008
*/

#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
  int cases=0;
  scanf("%d", &cases);

  for(int lll=1; lll<=cases; lll++) {
    int p, k, l;
    vector<int> f;
    vector<vector<int> > keys;
    scanf("%d %d %d", &p, &k, &l);

    for(int i=0; i<k; i++) {
      vector<int> a;
      keys.push_back(a);
    }


    for(int i=0; i<l; i++) {
      int tmp;
      scanf("%d", &tmp);
      f.push_back(tmp);
    }


    long long res=0;

    sort(f.begin(), f.end());
    while(f[f.size()-1]!=0) {
      //find best key
      sort(keys.begin(), keys.end());

//check for max num of letters per key?
      keys[0].push_back(1);
      res+=keys[0].size()*f[f.size()-1];

      f[f.size()-1]=0;
      sort(f.begin(), f.end());
    }


    printf("Case #%d: %lld\n", lll, res);
  }


  return 0;
}

