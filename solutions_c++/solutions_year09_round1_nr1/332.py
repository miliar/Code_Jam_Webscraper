#include <cstdio>
#include <set>
#include <cstring>
#include <vector>
#include <map>
using namespace std;


bool bases[11];
map<vector<int>, int> cache;

inline int next(int n, int b){
  int x, res = 0;
  while(n){
    x = (n%b);
    res += x*x;
    n /= b;
  }
  return res;
}

//bool nothappy[11][1000000];

set<int> used;
inline bool is_happy(int n, int b){
  used.clear();
  while(!used.count(n)){
    used.insert(n);
    n = next(n,b);
    if(n==1){
      used.clear();
      return true;
    }
  }
  used.clear();
  return false;
}

inline bool is_happy(int n){
  for(int i = 2; i <= 10; i++){
    if(bases[i]){
      if(!is_happy(n,i)) return false;
    }
  }
  return true;
}

inline int solve(){
  for(int i = 2; ; i++){
    if(is_happy(i)){
      return i;
    }
  }
  return -1;
}

int main(){
  int t;
  scanf("%d\n",&t);
  for(int i = 1; i <= t; i++){
    memset(bases,false,sizeof(bases)); 
    vector<int> vec;
    while(true){
      int b;
      scanf("%d",&b);
      if(b!=2 && b!=4){
        vec.push_back(b);
        bases[b] = true;
      }
      if(getchar()=='\n') break;
    }
    int res = cache[vec];
    if(!res){
      res = solve();
      cache[vec] = res;
    }
    printf("Case #%d: %d\n",i,res);
  }
  return 0;
}

