#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
using namespace std;
 
int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
#define zmax(a,b) (((a)>(b))?(a):(b))
#define zmin(a,b) (((a)>(b))?(b):(a))
#define zabs(a) (((a)>=0)?(a):(-(a)))
#define iif(c,t,f) ((c)?(t):(f))
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

int res;
map<int, int> mp;

void pop(int x) {
  int& v = mp[x];
  bool nd = false;
  while(v > 1) {
    nd = true;
    res++;
    v -= 2;
    mp[x - 1]++;
    mp[x + 1]++;
  }
  if(nd) {pop(x - 1); pop(x + 1);}
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int N; cin >> N;
    res = 0;
    mp.clear();
    for(int i = 0; i < N; i++) {
      int P, V;
      cin >> P >> V;
      mp[P] += V;
      pop(P);
    }
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}
