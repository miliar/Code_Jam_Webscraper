#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;

#include <unordered_map>

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

const int n = 20;
int nums[n];
int ansvec1;
int ansvec2;

unordered_map<int, int> foundsums;

bool permute(int sum, int vec, int i) {

  if(i >= n) return false;

  if(permute(sum,vec,i+1)) {
    return true;
  }

  sum += nums[i];
  vec += (1 << i);
  
  if(present(foundsums,sum)) {
    ansvec1 = foundsums[sum];
    ansvec2 = vec;
    return true;
  }

  foundsums[sum] = vec;

  return permute(sum,vec,i+1);
}

int main(int argc, char ** argv) {

  if(argc < 2) return -1;
  ifstream f (argv[1]);
  if(!f.is_open()) return -1;

  uint64_t g,w,m;
  int t;
  int dummy;
  
  f >> t;


  rep(i,t) {

    foundsums.clear();

    f >> dummy;

    rep(j,n) {
      f >> nums[j];
    }
    

    cout << "Case #" << i+1 << ":" << endl;

    if(!permute(0,0,0)) {
      cout << "Impossible" << endl;
    }

    vector<int> ans1,ans2;

    rep(j,n) {
      if((ansvec1 >> j) % 2) ans1.pb(nums[j]);
    }
    cout << ans1[0];
    for(int j=1; j<ans1.size(); j++) cout << " " << ans1[j];
    cout << endl;

    rep(j,n) {
      if((ansvec2 >> j) % 2) ans2.pb(nums[j]);
    }
    cout << ans2[0];
    for(int j=1; j<ans2.size(); j++) cout << " " << ans2[j];
    cout << endl;
  }
  return 0;
}
