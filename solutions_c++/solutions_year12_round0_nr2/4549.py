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
#define RESET(t) memset(t, -1, sizeof(t))
#define MAX 10000050



int main() {
  int T;scanf("%d",&T);
  FORE(test, 1, T) {
    int n,s,p;scanf("%d%d%d",&n,&s,&p);
    int ret = 0;
    FOR(i,0,n) {
      int a;scanf("%d",&a);
      if (a <= 1) {
        ret += p <= a;
      }
      else if (a >= 29) {
        ++ret;
      }
      else {
        if (a % 3 == 0) {
          if (a / 3 >= p) {
            ++ret; 
          }
          else if (s > 0 && a / 3 + 1 >= p) {
             --s;
             ++ret;
          }
        }
        else if (a % 3 == 1) {
          if (a / 3 + 1 >= p) {
            ++ret; 
          }
        }
        else {
          if (a / 3 + 1 >= p) {
            ++ret; 
          }
          else if (s > 0 && a / 3 + 2 >= p) {
             --s;
             ++ret;
          }
        }
      }
    }
    printf("Case #%d: %d\n", test,ret);
  }
}

