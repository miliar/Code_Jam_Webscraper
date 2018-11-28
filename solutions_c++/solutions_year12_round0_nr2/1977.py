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

vi t;
int p;

#define M 101
int memo[M][M] = {0};

int solve(int n, int s){

  if(n<0) return 0;
  if(memo[n][s]>=0) return memo[n][s];

  int r1=0;
  int r2=0;

  // if t[n] is surprising
  if(s>0){
    int m=(t[n]+4)/3;
    if(m-2>=0 && m<=10){
      // can't be surprising
      int add=0;
      if(m>=p) add=1;
      r1 = add + solve(n-1, s-1);
    }
  }

  // if t[n] is not surprising
  int m=(t[n]+2)/3;
  int add=0;
  if(m>=p) add=1;
  r2 = add + solve(n-1, s);

  int r = max(r1, r2);

  //printf("n=%d s=%d r=%d\n", n, s, r);
  memo[n][s]=r;

  return r;
}

int main () {
  int test, T;

  cin >> T;
  int n, s;
  int i, j;
  REP (test, T) {
    cin >> n;
    cin >> s;
    cin >> p;
    REP(i,M) REP(j,M) memo[i][j]=-1;

    t.clear();
    REP(i,n){
      int tmp;
      cin >> tmp;
      t.push_back(tmp);
    }
    gp(solve(n-1, s));
  }
  return 0;
}

