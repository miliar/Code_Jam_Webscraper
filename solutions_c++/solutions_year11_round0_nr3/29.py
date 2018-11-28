#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

int main(){
  int t; cin >> t;
  int c[1002];
  for(int caso = 1; caso <= t; caso++){
    int n; cin >> n;
    int x = 0, s = 0;
    for(int i = 0; i < n; i++) cin >> c[i], x ^= c[i], s += c[i];
    printf("Case #%d: ", caso);
    if(x || n == 1) cout << "NO" << endl;
    else{
      int a = *min_element(c, c + n);
      cout << s - a << endl;
    }
  }
}
