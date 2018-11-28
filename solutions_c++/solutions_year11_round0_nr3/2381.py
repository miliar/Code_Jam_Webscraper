#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cassert>

#define D(x) cout << #x " is " << x << endl
#define all(x) x.begin(), x.end()

using namespace std;

int main(){
  int T, K=1;
  scanf("%d", &T);
  while(T--){
    int N;
    scanf("%d", &N);
    int num = 0, xoria = 0, res = 0, _m = 1<<30;
    for(int i=0;i<N;++i){
      scanf("%d", &num);
      res += num;
      _m = min(num, _m);
      xoria = xoria ^ num;
    }
    
    if(xoria != 0){
      printf("Case #%d: NO\n", K++);
    }else{
      res -= _m;
      printf("Case #%d: %d\n", K++, res);
    }
  }
  return 0;
}
