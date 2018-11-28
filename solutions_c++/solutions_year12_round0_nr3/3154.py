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

int ndigs(int x) {
  int cnt=0;
  while (x) {
    cnt++;
    x/=10;
  }
  return cnt;
}


int main() {
  // freopen("c.in","r",stdin);

  int T;
  cin >> T;
  
  forUp(t, T) {
    int A,B;
    cin >> A >> B;
    int len=ndigs(A);
    int size=1; forUp(i,len) size*=10;
    int cnt=0;

    for(int n=A; n<=B; n++) {
      map<int,bool> used;
      for(int end=10; end<size; end*=10) {
        int m = (n%end)*size/end + (n/end);
        if (n < m && m <= B && !used[m]) {
          cnt++;
          used[m]=true;
        }
      }
    }
    
    cout << "Case #" << t+1 << ": " << cnt << endl;
  }
  
  return 0;
}






