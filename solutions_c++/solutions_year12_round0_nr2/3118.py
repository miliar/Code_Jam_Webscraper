#include <iostream>
#include <string>
#include <vector>

using namespace std;

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <cmath>
#include <set>

typedef long long LL;
typedef vector<string> Vs;
typedef vector<int> Vi;
typedef vector<bool> Vb;
typedef vector<long long> Vll;
typedef vector<double> Vd;
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

int main() {
  // freopen("b.in","r",stdin);

  int T;
  cin >> T;
  
  forUp(t, T) {
    int n_googlers, n_surprising, p;
    cin >> n_googlers >>  n_surprising >> p;
    Vi points(n_googlers);
    forUp(i,n_googlers) cin >> points[i];

    int cnt=0;
    forUp(i,n_googlers) {
      if ((points[i]+2)/3 >= p) {
        // Surprising not required
        cnt++;
      } else if (n_surprising) {
        // Surprising required
        if ((points[i] >= 3 && points[i] <= 27 && points[i] % 3 == 0 && points[i]/3 == p-1) ||
            (points[i] >= 2 && points[i] <= 26 && (points[i] % 3 == 2) && (points[i]+1)/3 == p-1)) {
          cnt++;
          n_surprising--;
        }
      }
    }
    
    cout << "Case #" << t+1 << ": " << cnt << endl;
  }
  
  return 0;
}






