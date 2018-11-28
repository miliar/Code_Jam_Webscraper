#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <map>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;

typedef long long LL;
#define REP(i,e) for (int (i) = 0; (i) < (e); ++(i))
#define foreach(__my_iterator,__my_object) for (typeof((__my_object).begin()) __my_iterator = (__my_object).begin(); __my_iterator!= (__my_object).end(); __my_iterator++)

const int MAXN = 10010;
LL d[MAXN];
LL l[MAXN];

void solve(int N, int D){
  bool ok = false;
  queue < pair <int, int> > q;
  int pos = 1;

  if(d[0] + d[0] >= D) ok = true;
  for(;pos<N;){
    if(d[0]+d[0] < d[pos]) break;
    q.push( make_pair(0, pos));
    pos++;
  }
  
  while(!q.empty()){
    int prev = q.front().first;
    int cur = q.front().second;
    q.pop();
    int reach = min(d[cur] + (d[cur]-d[prev]), d[cur]+l[cur]);
    if(reach >=D) ok = true;
    for(;pos<N;){
      if(reach < d[pos]) break;
      q.push( make_pair(cur, pos));
      pos++;
    }
  }
  if(ok) printf("YES\n");
  else printf("NO\n");
}

int main(){
  int T,D,N;
  cin >> T; 
  REP(i, T){
    cin >> N;
    REP(j, N) cin >> d[j] >> l[j];
    cin >> D;
    printf("Case #%d: ", i+1);
    solve(N,D);
  }

  return 0;
}
/*
echo "
4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14
 */
