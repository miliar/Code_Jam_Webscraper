#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int main()
{
  int tcase = 0;
  cin >> tcase;
  for (int tind = 1; tind <= tcase; tind++) {
    int n;
    int i,j;
    //istringstream strin();
    cin >> n;
    int t[2000];
    int p[2000];
    int ind[1001];
    for (i = 0; i < n; ++i) {
      cin >> t[i];
    }
    for (i = 0; i < n; ++i) {
      cin >> p[i];
      ind[i] = i;
    }
    for (i = 0; i < n; ++i) {
      for (j = i+1; j < n; ++j) {
        if (p[ind[i]] < p[ind[j]] ||
            (p[ind[i]] == p[ind[j]] && ind[i] > ind[j])) {
          swap(ind[i], ind[j]);
        }
      }
    }
    int ans = 0;
    cout << "Case #" << tind << ":";
    for (i = 0; i < n; ++i)
      cout << ' ' << ind[i];
    cout << endl;
  }
  return 0;
}
