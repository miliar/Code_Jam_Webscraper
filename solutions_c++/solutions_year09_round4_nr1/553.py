#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <cmath>
#include <numeric>
#include <bitset>
#include <stack>

using namespace std;
 
int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
#define zmax(a,b) (((a)>(b))?(a):(b))
#define zmin(a,b) (((a)>(b))?(b):(a))
#define zabs(a) (((a)>=0)?(a):(-(a)))
#define iif(c,t,f) ((c)?(t):(f))
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

int A[40];

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int N; cin >> N;
    set<pair<int, int> > q;
    for(int i = 0; i < N; i++) {
      string x; cin >> x;
      A[i] = x.find_last_of('1') + 1;
    }
    int res = 0;
    for(int i = 0; i < N; i++) {
      if(A[i] > i + 1) {
        int j;
        for(j = i + 1; A[j] > i + 1; j++);
        while(j > i) {
          swap(A[j], A[j - 1]);
          j--;
          res++;
        }
      }
    }
    cout << "Case #" << t << ": " << res << endl;
  }

  return 0;
}
