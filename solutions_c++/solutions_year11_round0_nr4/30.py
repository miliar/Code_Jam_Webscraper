#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
int x[1002], seen[1002];
int main(){
  int tt; cin >> tt;
  for(int caso = 1; caso <= tt; caso++){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) cin >> x[i];
    for(int i = 0; i < n; i++) seen[i] = false;
    int res = 0;
    for(int i = 0; i < n; i++) if(!seen[i]){
      int u = i, cnt = 0;
      while(!seen[u]){
        cnt++;
        seen[u] = true;
        u = x[u] - 1;
      }
      res += cnt == 1 ? 0 : cnt;
    }
    cout << "Case #" << caso << ": " << res << endl;
  } 
}
