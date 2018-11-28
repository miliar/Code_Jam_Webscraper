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

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

int main(int argc, char ** argv) {

  if(argc < 2) return -1;
  ifstream f (argv[1]);
  if(!f.is_open()) return -1;

  int big_t;
  f >> big_t;

  int n,s,p,t;

  int s_needed, ans;

  int flo,rest;

  rep(i,big_t) {

    f >> n;
    f >> s;
    f >> p;

    s_needed = 0;
    ans = 0;

    rep(j,n) {
      
      f >> t;

      flo = t/3;
      rest = t-flo*3;

      if(flo >= p) {
        ans++;
        continue;
      }

      switch(rest) {
      
        case 0:
          if(t > 0 && flo+1 == p) {
            s_needed++;
          }
          break;

        case 1:
          if(flo+1 == p) {
            ans++;
          }
          break;

        case 2:
          if(flo+1 == p) {
            ans++;
          } else if(flo+2 == p) {
            s_needed++;
          }
          break;
      }
    }

    ans += min(s,s_needed);

    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  return 0;
}
