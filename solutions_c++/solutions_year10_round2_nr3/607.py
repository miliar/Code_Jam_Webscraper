#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;

int data[501][501];
int comb[501][501];
int mod = 100003;

void init() {
   memset(data, 0, sizeof data);
   memset(comb, 0, sizeof comb);
   comb[0][0] = 1;
   for (int i=1; i<=500; ++i) {
      comb[i][0] = 1;
      for (int j=1; j<=i; ++j)
         comb[i][j] = (comb[i-1][j-1] + comb[i-1][j] ) % mod;
   }

   for (int i=2; i<=500; ++i) data[i][1] = 1;
   for (int cur=3; cur<=500; ++cur) {
      for (int pos = cur-1; pos>1; --pos) {
         int gap = cur - pos;
         for (int i=pos-1; pos-i<=gap && i>=1; --i) {
            data[cur][pos] += data[pos][i] * comb[gap-1][pos-i-1] % mod;
            data[cur][pos] %= mod;
         }
      }
   }
}

int main() {
	freopen("problem.in", "r", stdin);
	freopen("problem.out", "w", stdout);
	int T;
   scanf("%d", &T);
   init();
	for (int tid=1; tid<=T; ++tid) {
      int n;
      scanf("%d", &n);
      int res = 0;
      for (int i=1; i<=n-1; ++i) 
         res = (res + data[n][i]) % mod;
		printf("Case #%d: %d\n", tid, res);
	}
	return 0;
}


