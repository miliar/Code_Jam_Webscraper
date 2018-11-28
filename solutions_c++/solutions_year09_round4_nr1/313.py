/* GCJ'09 Template v.2e-9
 * Per Austrin
 */
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;

int CASES;

void init() {
  scanf("%d", &CASES);

}


void solve(int P) {
  int n;
  int val[100];

  scanf("%d", &n);

  char row[1000];
  for (int i = 0; i < n; ++i) {
    scanf("%s", row);
    val[i] = -1;
    for (int j = 0; j < n; ++j) if (row[j] == '1') val[i] = j;
  }

  int ans = 0;
  bool changing = true;
  while (changing) {
    changing = false;
    for (int i = n-1; i >= 0; --i) {
      if (val[i] > i) {
	changing = true;
	int j;
	int rep = -1;
	for (j = i; rep == -1; ++j)
	  if (val[j] <= i) rep = j;
	//	printf("bad %d at %d, replacement %d at %d\n", val[i], i, val[rep], rep);

	for (j = rep; j > i; --j) swap(val[j], val[j-1]), ++ans;
	//	printf("[%d]: ", ans);
	//	for (int i = 0; i < n; ++i) printf(" %d", val[i]);
	//	printf("\n");
	break;
      }
    }
  }

  

  
  printf("Case #%d: %d\n", P, ans);
}

int main(void) {
  init();
  for (int i = 1; i <= CASES; ++i) solve(i);
  return 0;
}
