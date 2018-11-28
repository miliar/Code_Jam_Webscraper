#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX_N 1000

int T;
int N;
int bag[MAX_N];

void solve(){
  int sum = 0;
  for(int i=0;i<N;i++) sum ^= bag[i];
  if(sum != 0) cout << "NO" << endl;
  else {
    sum = 0;
    int m = 10000000;
    for(int i=0;i<N;i++){
      sum += bag[i];
      m = min(m, bag[i]);
    }
    cout << sum-m << endl;
  }
}

int main(){
  cin >> T;
  for(int i=1;i<=T;i++){
    cin >> N;
    for(int j=0;j<N;j++) cin >> bag[j];
    
    cout << "Case #" << i << ": ";
    solve();
  }
}
