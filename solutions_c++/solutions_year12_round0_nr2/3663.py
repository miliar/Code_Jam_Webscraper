#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {

  int t,n,s,p,ans;
  cin >> t;
  for (int i=1;i<=t;i++) {
    cin >> n >> s >> p;
    int scores[n];
    int surp = 0;
    int ans = 0;
    for (int j=0;j<n;j++) {
      cin >> scores[j];
      if (scores[j] > 3*p-3) {
        ans++;
      }
      else if (p-2 < 0) {
        continue;
      }
      else if (scores[j] == 3*p-3) {
        surp++;
      }
      else if (scores[j] == 3*p-4) {
        surp++;
      }
    }
    ans+=min(s,surp);
    printf("Case #%d: %d\n",i,ans);
  }

  return 0;
}
