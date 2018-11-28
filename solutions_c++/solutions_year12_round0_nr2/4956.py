#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

int main(){
  int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {
    printf("Case #%d: ", test);

    int n, s, p;
    cin >> n >> s >> p;

    int ct1 = 0; // can surprise without increasing count
    int ct2 = 0; // can surprise with increasing count
    int ct = 0;
    rep(i, n) {
      int x;
      cin >> x;
      if(x == 0) {
        if(0 >= p) ct++;
      }
      else if(x == 1) {
        if(1 >= p) ct++;
      }
      else if(x == 29) {
        if(10 >= p) ct++;
      }
      else if(x == 30) {
        if(10 >= p) ct++;
      }
      else {
        int nosurprise = (x + 2) / 3;
        int surprise = (x - 2) / 3 + 2;
        if(nosurprise >= p) ct++;
        else if(surprise >= p) ct2++;
        else ct1++;
      }
    }

    cout << ct + min(s, ct2) << endl;
  }
}
