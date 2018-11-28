
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>

using namespace std;

int l[12345], d[12345];
int last[12345];
int main() {

   int tests, itest;
   scanf("%d", &tests);
   for(itest = 1; itest <= tests; itest++) {
      
      int n;
      scanf("%d",&n);
      int possible = false;
      int i, j;
      memset(last, -1, sizeof(last));
      for(i = 0; i < n; i++) {
	 scanf("%d%d", l+i, d +i);
      }
      int D;
      scanf("%d", &D);
      last[0] = l[0];
//      int tmp;
      for(i = 0; i < n; i++) {
	 if(last[i] > 0) {
	    for(j = i + 1; j < n && l[j] - l[i] <= last[i]; j++) {
	       if(last[j] < 0)
		  last[j] = min(l[j] - l[i], d[j]);
	    }
	    if(D - l[i] <= last[i]) {
	       possible = true;
	    }
	 }
      }
      printf("Case #%d: %s\n", itest, possible?"YES":"NO");
   }
   return 0;
}
