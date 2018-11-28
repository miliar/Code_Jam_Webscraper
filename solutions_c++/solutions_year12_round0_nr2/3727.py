#include <iostream>
#include <algorithm>

using namespace std;

int n, s, p, data[100];

int solve(){
  int res = 0;
  for(int i=0;i<n;i++){
    if((p-1)*3 < data[i]) res++;
    else if(s > 0 && (p-1)*3 < data[i]+2 && data[i] >= p){
      res++;
      s--;
    }
  }
  return res;
}

main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> n >> s >> p;
    for(int i=0;i<n;i++) cin >> data[i];
    cout << "Case #" << t << ": ";
    cout << solve() << endl;
  }
}
