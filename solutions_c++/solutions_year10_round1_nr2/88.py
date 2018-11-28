#include <iostream>
using namespace std;

const int MAXN = 101;
int a[MAXN];
long long mincost[257];
long long newmincost[257];
long long overallmincost;
int T, D, I, M, N;

int iabs(int x) {
  if(x >= 0) {
    return x;
  } else {
    return -x;
  }
}

int main(int argc, char *argv[]) {
  cin >> T >> ws;
  for(int t=1; t<=T; t++) {
    cin >> D >> I >> M >> N >> ws;
    for(int i=0; i<N; i++) {
      cin >> a[i] >> ws;
    }
    mincost[256] = D;
    for(int p=0; p<256; p++) {
      mincost[p] = iabs(a[0]-p);
    }
    // Insert after modify
    if(M > 0) {
      for(int p=0; p<256; p++) {
        for(int lastp=0; lastp<256; lastp++) {
          mincost[p] = min(mincost[p], mincost[lastp] + I*((iabs(p-lastp)-1)/M+1));
        }
      }
    }

    for(int i=1; i<N; i++) {
      // Delete
      for(int p=0; p<=256; p++) {
        newmincost[p] = mincost[p] + D;
      }
      
      // Modify to p
      for(int p=0; p<256; p++) {
        for(int lastp=0; lastp<=256; lastp++) {
          if(iabs(p-lastp)<=M || lastp == 256) {
            newmincost[p] = min(newmincost[p], mincost[lastp] + iabs(a[i] - p));
          }
        }
      }
      
      // Insert after modify
      if(M > 0) {
        for(int p=0; p<256; p++) {
          for(int lastp=0; lastp<256; lastp++) {
            newmincost[p] = min(newmincost[p], newmincost[lastp] + I*((iabs(p-lastp)-1)/M+1));
          }
        }
      }
      
      for(int p=0; p<=256; p++) {
        mincost[p] = newmincost[p];
      }
    }
    
    overallmincost = mincost[0];
    for(int p=1; p<=256; p++) {
      overallmincost = min(overallmincost, mincost[p]);
    }
    
    cout << "Case #" << t << ": " << overallmincost << endl;
  }
  
  return 0;
}
