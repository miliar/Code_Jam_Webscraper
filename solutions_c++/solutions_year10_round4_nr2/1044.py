#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>

using namespace std;

const int N = 4000;
int m[N];
int tck[N];
int vl[N];

int main() {
  int t;
  scanf("%d",&t);
  for (int tc=1; tc<=t; ++tc) {

    int p;
    scanf("%d",&p);
    int n = 1<<p;
    int s = n-1;
    for (int i=0; i<n; ++i) {
      scanf("%d",m+i);
    }
    for (int i=s; i>0; --i) {
      scanf("%d",tck+i);
      vl[i] = 0;
    }
    vl[0] = 1;
    int ret = 0;
    for (int i=0; i<n; ++i) {
      for (int j=0,k=(2*s-i+1)/2; vl[k]==0; ++j,k/=2) {
        if (j>=m[i]) {
          vl[k] = 1;
          ++ret;
        }
      }      
    }

    printf("Case #%d: %d\n",tc,ret );
  }
  return 0;
}
