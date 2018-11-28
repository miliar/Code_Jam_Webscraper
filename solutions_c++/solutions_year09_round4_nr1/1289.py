#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define rep(i,n) for(int i=0;i<int(n);++i)

#define N 50             //max number of vertices in one part
#define INF 100000000    //just infinity

int n;
char linha[N][N];

int h[N];
int id[N],pos[N],di[N];

int main() {
  int nt0;

  scanf(" %d", &nt0);
  rep(nt,nt0) {
    scanf(" %d", &n);
    rep(i,n) {
      scanf(" %s", linha[i]);

      h[i] = 0;
      rep(j,n) if(linha[i][j]=='1') h[i] = j;
    }

    int ans = INF;
    rep(i,n) id[i] = i;
    do {
      int ferrou = 0;
      rep(i,n) if(h[id[i]] > i) {
	ferrou = 1;
	break;
      }
      if(ferrou) continue;

      int cost = 0;
      for(int i=1 ; i<n ; i++) {
	for(int j=i ; j<n ; j++)
	  if(id[i-1] > id[j]) cost++;
      }

      ans = min(ans, cost);
    } while(next_permutation(id,id+n));

    printf("Case #%d: %d\n", nt+1, ans);
  }

  return 0;
}
