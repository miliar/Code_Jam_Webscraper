#include<iostream>
#include<strstream>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int solve(){
  int A,B;
  cin >> A >> B;
  ostrstream As;
  As << A << '\0';
  const int d=strlen(As.str());
  const int o = pow(10.0,d-1);
  vector<int> xs;
  int ans = 0;
  for(int i=A;i<=B;++i){
    int x=i;
    xs.clear();
    for(int j=0;j<d;++j){
      x= x/10 + (x%10)*o;
      if(A<=x && x<=B){
        xs.push_back(x);
      }
    }
    sort(xs.begin(),xs.end());
    int u=unique(xs.begin(),xs.end())-xs.begin();
    //cerr << u << " unique versions for " << i << endl;
    ans += u-1;
  }
  return ans/2;
}
int main(){
  int t;
  cin >> t;
  for(int i=1;i<=t;++i){
    cout << "Case #" << i << ": " << solve() << endl;
  }
}