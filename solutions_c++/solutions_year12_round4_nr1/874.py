#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
int inline ABS(int a){ return a>0?a:-a; }
typedef pair<int,int> pi;
typedef unsigned long long ULL;
typedef long long LL;
int gcd (int a, int b)
{
   if (b == 0)
      return a;
   else
      return gcd (b, a % b);
}
/* Main code starts from here */

int d[100001], l[100000], di[1000000];
int main() {
	int t,T;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
	  int n;
	  cin >>n;
	  for (int i = 0; i < n; i++) cin >>d[i] >>l[i];
	  int D;
	  cin >>D;
	  memset(di, -1, sizeof di);
	  di[0] = d[0];
	  int flag = 0;
	  for (int i = 0; i < n && di[i] != -1; i++) {
	    if (di[i] + d[i] >= D) {
	      flag = 1;
	      break;
	    }
	    for (int j = i + 1; j < n; j++) {
	      if (d[j] - d[i] <= di[i]) {
	        di[j] = max(di[j], min(l[j], d[j] - d[i]));
	      }
	    }
	  }

	  printf("Case #%d: ", t);
	  if (flag) puts("YES");
	  else puts("NO");
	}
	return 0;
}
