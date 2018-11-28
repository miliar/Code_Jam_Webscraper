#include <iostream>
#include <vector>
#include <fstream>
#include <iostream>
#include <algorithm>
#define REP(i,n) for(int i=0;(i)<(int)(n);(i)++)
using namespace std;

int gcd(int a, int b){
  if(a % b ==0) return b;
  else return gcd(b, a%b);
}

string solve(){
  long long N;
  int D,G;
  cin >> N >> D >> G;

  int x = 0;
  if(D != 0){
    x = gcd(100,D);
    x = 100 / x;
  }
  //  cout << x << endl;

  if(x > N) return "Broken";
  if(G==100 && D!=100) return "Broken";
  if(G==0 && D!=0) return "Broken";
  return "Possible";
}

int main(){
  int nProb;
  cin >> nProb;
  string ans;
  for(int i=0;i<nProb;i++){
    ans = solve();
    printf("Case #%d: ", i+1);
    cout << ans << endl;
  }
  return 0;
}
