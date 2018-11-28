#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

#define REP(i,i0,in) for(int i=(i0); i<(in); i++)

int compute(vector<int> V){
  sort(V.begin(), V.end());
  int ac=0;
  int sum=0;
  REP(i,0,V.size()){
    ac ^= V[i];
    sum += V[i];
  }
  
  if (ac!=0)
    return -1;
  REP(i,0,V.size()){
    if (ac ^ V[i] == V[i])
      return sum-V[i];
  }
}

int main(){
  int T;
  cin >> T;
  REP(t,0,T){
    int N;
    cin >> N;
    vector<int> V;
    V.resize(N);
    REP(i,0,N){
      cin >> V[i];
    }
    int ans = compute(V);
    cout << "Case #" << (t+1) << ": ";
    if (ans == -1){
      cout << "NO" << endl;
    } else {
      cout << ans << endl;
    }
  }
  return 0;
}
