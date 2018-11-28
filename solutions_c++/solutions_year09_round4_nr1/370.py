#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std; 

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define clr(a, v) memset((a), (v), sizeof(a))
#define forn(i, n) for (int i = 0; i < (n); ++i)


char s[256];
int n, a[256];

int main() {
 freopen("a.in", "r", stdin);
 freopen("a.out", "w", stdout);

 int nt; scanf("%d", &nt);

 for (int tc=1; tc<=nt; ++tc) {
  scanf("%d", &n); gets(s);
  forn (i, n) {
   gets(s);
   int k=0;
   forn (j, n) if (s[j]=='1') k=j+1;
   a[i]=k;
  }
  int res=0;
  forn (i, n) {
   int j;
   for (j=i; j<n; ++j) if (a[j]<=i+1) break;
   for (int k=j; k>i; --k)
    swap(a[k], a[k-1]), ++res;   
  }
  printf("Case #%d: %d\n", tc, res);

 }

 return 0;
}
