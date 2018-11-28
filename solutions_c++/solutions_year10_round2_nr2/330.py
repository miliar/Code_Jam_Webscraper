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

int xi[100];
int vi[100];

int main() {
  int c;
  int n,k,b,t;
  scanf("%d",&c);
  for (int tc=1;tc<=c;++tc) {
    scanf("%d%d%d%d",&n,&k,&b,&t);
    int ret = 0;
    int cnt = 0;
    for (int i=0; i<n; ++i) scanf("%d",xi+n-i-1);
    for (int i=0; i<n; ++i) scanf("%d",vi+n-i-1);
    for (int i=0; i<n && k>0; ++i) {
      if ((long long)vi[i]*t >= b-xi[i]) {
        --k;
        ret += cnt;
      } else {
        ++cnt;
      }
    }
    printf("Case #%d: ",tc);
    if (k>0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n",ret);
    }
  }
  return 0;
}
