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
    int i,j;
    //istringstream strin();
    int n;
    int md[10001];
    mset(md, 255);
    int d[10001];
    int l[10001];
    int D;
    cin >> n;
    for (i = 0; i < n; ++i) {
      cin >> d[i] >> l[i];
    }
    cin >> D;
    md[0] = d[0];
    bool res = false;
    for (i = 0; i < n; ++i) {
      if (md[i] < 0) {
        //cerr << i << " cannot reach" << endl;
        continue;
      }
      //cerr << i << ' ' << md[i] << endl;
      int k = md[i];
      for (j = i + 1; j < n; ++j) {
        if (d[j] - d[i] > k) {
          break;
        }
        int p = min(d[j] - d[i], l[j]);
        if (md[j] < p) {
          md[j] = p;
        }
      }
      if (d[i] + k >= D) {
        res = true;
        break;
      }
    }

    cout << "Case #" << tind << ": " << (res ? "YES" : "NO") << endl;
  }
  return 0;
}
