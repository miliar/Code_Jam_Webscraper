#include<cstdio>
#include<algorithm>
#include<queue>
#include<vector>
#include<iostream>
#include<cstring>
#include<map>
#include<set>
#include<utility>
#include<string>
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
int Ca;
int memo[5000];
int need[3000];
int p, ans;
int rec(int n,int depth){
  if(depth == 0){

    return need[n-(1 << p)];
  }
  int ret = min(rec(2*n, depth-1), rec(2*n+1, depth-1));
  //printf("%d %d %d\n", n, depth, ret);
  if(ret < depth) ans++;
  return ret;
}
    
  
int main(){
  scanf("%d", &Ca);
  for(int ii = 0; ii < Ca; ii++){
    scanf("%d", &p);
    for(int i = 0; i < (1 << p); i++){
      scanf("%d", need+i);

    }

    for(int i = 0; i < (1 << p)-1; i++){
      int hoge;
      scanf("%d", &hoge);
    }
    ans = 0;
    rec(1, p);
    printf("Case #%d: ", ii+1);
    printf("%d\n", ans);
  }
}
    
    
    

    

