#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    ll n;
    int pd,pg;
    cin >> n >> pd >> pg;
    if(pg==100 && pd != 100){
      gp("Broken");
      continue;
    }
    if(pg==0 && pd != 0){
      gp("Broken");
      continue;
    }
    string s="Broken";
    ll h = n>100 ? 100 : n;
    for(int i=1; i<=h; i++){
      for(int j=0; j<=i; j++){
        if(j*100 % i != 0) continue;
        int p = j*100 /i;
        if(p==pd){
          s="Possible";
          goto A;
        }
      }
    }
  A:
    gp(s);
  }
  return 0;
}

