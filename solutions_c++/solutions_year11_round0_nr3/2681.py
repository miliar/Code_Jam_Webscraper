//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define LL long long
#define ST first
#define ND second
#define PII pair<int,int>
#define VI vector<int>

using namespace std;
int t,n,k,x;
int minn,sum;
int main() {
  scanf("%d",&t);
  for(int i = 1; i<=t; i++) {
    scanf("%d",&n);
    x = 0; minn = 1000000000; sum = 0;
    for(int j = 1; j<=n; j++) {
      scanf("%d",&k);
      minn = MIN(minn,k);
      sum += k;
      x = x ^ k;
    }
    printf("Case #%d: ",i);
    if(x == 0) printf("%d\n",sum - minn);
    else printf("NO\n");
  }


  return 0;
}
