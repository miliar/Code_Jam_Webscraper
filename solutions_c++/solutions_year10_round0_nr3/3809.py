#include "stdio.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
  int t;
  scanf("%d\n", &t);
  unsigned int r, n;
  unsigned long int k;
  vector<unsigned int> g;
  g.resize(1000);
  unsigned long int tot;
  for (int i=0; i<t; i++) {
    scanf("%u %lu %u\n", &r, &k, &n);
    for (int j=0; j<n; j++) {
      unsigned int u;
      scanf("%u ", &u);
      g[j] = u;
    }
    tot =0;
    for(int j=0; j<n; j++) {
      //printf ("%d ", g[j]);
      tot += g[j];
    }
    //printf("  = %lu\n", tot);
    scanf("\n");
    //printf(" r is %d, k is %lu, n is %d \n", r, k, n);
    tot = 0;
    unsigned long int fill;
    int z = 0;
    for(int j=0; j<r; j++) {
      fill = 0;
      for(int y=0; y<n; y++) {
        fill += g[z];
        //printf("    ---- going for ride is %d\n", g[z]);
        if(fill > k) {
          fill -= g[z];
          break;
        }
        z++;
        if(z == n) z=0;
      }
      tot += fill;
      //printf("   --- fill after ride is %lu += %lu\n", fill, tot);
    }
    printf("Case #%d: %lu\n", i+1, tot);
  }
}
