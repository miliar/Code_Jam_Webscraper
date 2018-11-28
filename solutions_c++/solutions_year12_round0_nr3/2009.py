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
    int a,b;
    cin >> a >> b;
    int j;
    int res=0;
    for(int i=a; i<=b; i++){
      map<int, int> check;
      int rank=0;
      for(j=i; j>0; j/=10){
        rank++;
      }
      for(int j=1; j<rank; j++){
        int m=pow(10.0,j);
        int r=i%m;
        if(r==i) break;
        int s=i/m;
        int ex=r*pow(10.0,rank-j) + s;
        if(ex>i && ex>=a && ex<=b && check[ex]<=0) {
          res++;
          check[ex]=1;
        }
        m*=10;
      }
    }
    gp(res);
  }
  return 0;
}

