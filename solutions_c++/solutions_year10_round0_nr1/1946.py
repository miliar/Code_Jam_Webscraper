#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define SZ(a) ((int)a.size())
#define MOD 1000000000 

typedef pair<int, int> II;
typedef vector<II> VII;
typedef long long LL;

int ntest;
int n, k, ret;
int f[31];

int main() {
	freopen("A-large.in", "rt", stdin);
    //freopen("a.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	scanf("%d", &ntest);
	f[1] = 1;
	for (int i=2; i<=30; i++) {
	  f[i] = f[i-1] + 1 + f[i-1];
	  //cout << f[i] << endl;
   }
	
	FR(test, ntest) {             
      scanf("%d%d", &n, &k);            
      ret = 0;
      if (k % (f[n]+1) == f[n]) ret = 1;
      cout << "Case #" << test+1 << ": " << (ret?"ON":"OFF") << endl;
    }

	return 0;
}
