#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
typedef long long LL;

#define INF 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FS first
#define SD second
#define MP make_pair

char M[200][200];
int P[200];
int W[200];
double O[200];

int main() {
  int t;scanf("%d",&t);
  FORE(test,1,t) {
    int n;scanf("%d\n",&n);
    FOR(i,0,n) {
      W[i] = P[i] = 0;
      O[i] = 0.0;
    }
    FOR(i,0,n) {
      FOR(j,0,n) {
        scanf("%c",&M[i][j]);
        if (M[i][j] == '1') {
          P[i]++;
          W[i]++;
        }
        else if (M[i][j] == '0') {
          P[i]++;
        }
      }
      scanf("\n");
    }
    FOR(i,0,n) {
      double s = 0.0;
      FOR(j,0,n) {
        if (M[i][j] !='.') {
          int w = W[j];
          if (M[i][j] == '0') {
            --w;
          }
          s += (double)w/(P[j]-1.0);
        }
      }
      O[i] = s/(double)P[i];
    }
    printf("Case #%d:\n", test);
    FOR(i,0,n) {
      double s = 0.0;
      FOR(j,0,n) {
        if (M[i][j] !='.') {
          s += O[j];
        }
      }
      printf("%.10lf\n", (double)W[i]/(4.0*P[i]) + 0.5*O[i] + 0.25*s/(double)P[i] );
    }

  }


}
