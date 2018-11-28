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
    int i,j,n;
    cin >> n;
    vector<int> num;
    REP(i,n){
      cin >> j;
      num.push_back(j);
    }
    int k=0;
    int mav=INT_MIN;
    while(k < (1 << n)){
      //printf("===new case===\n");
      int sean = 0;
      int pat = 0;
      int real = 0;
      REP(i,n){
        int bit = (k >> i) & 1;
        if(bit){
          pat ^= num[i];
          real += num[i];
          //printf("pat plus %d result:%d\n", num[i], pat);
        }else{
          sean += num[i];
          //printf("sean plus %d result:%d\n", num[i], sean);
        }
      }
      if(pat && pat == sean){
        if(mav < real){
          //printf("update maxval\n");
          mav = real;
        }
      }
      k++;
    }
    if (mav==INT_MIN) {gp("NO");}
    else {gp(mav);}
  }
  return 0;
}

