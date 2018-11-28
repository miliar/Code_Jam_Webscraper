#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
using namespace std;

int n, malte, minm, m;
int ans[2010], ansmin[2010];
vector <int> pref[2010];

int rec(int c){
  int x, r, t;
  vector <int> :: iterator i;
  
  //  printf("min=%d, c=%d, malte=%d\n", minm, c, malte);

  if (c == -1 && malte < minm){
    minm = malte;
    for (t = 1; t <= n; t++)
      ansmin[t] = ans[t];
    return 1;
  }
  if (malte >= minm) return 0;

  for (i = pref[c].begin(); i != pref[c].end(); i++){
    if (*i > 0){
      x = *i;
      if (ans[x] == 0) continue;
      if (ans[x] == 1) return rec(c-1);
      ans[x] = 1;
      malte++;
      //      printf("%d -> 1\n", x);
      r = rec(c-1);
      //	printf("%d -> -1\n", x);
      ans[x] = -1;
      malte--;
      continue;
      
    }
    else{
      x = -(*i);
      if (ans[x] == 1) continue;
      if (ans[x] == 0) return rec(c-1);
      ans[x] = 0;
      //      printf("%d -> 0\n", x);
      r = rec(c-1);
      ans[x] = -1;
      //	printf("%d -> -1\n",x);
      continue;
    }
  }
  return 0;

}

void imprimevetor(){
  int i;
  for (i = 1; i <= n; i++){
    if (ansmin[i] == 1)
      printf(" 1");
    else
      printf(" 0");
  }
}

int main(){
  int c, t, i, j, k, x, y;

  scanf("%d", &c);
  for (k = 1; k <= c; k++){
    memset(ans, -1, 2010*sizeof(int));
    //memset(ansmin, -1, 2010*sizeof(int));
    minm = 3000;
    malte = 0;
    scanf("%d", &n);
    scanf("%d", &m);
    for (i = 0; i < m; i++){
      pref[i].clear();
    }
    for (i = 0; i < m; i++){
      scanf("%d", &t);
      for (j = 0; j < t; j++){
	scanf("%d %d", &x, &y);
	y = y*2 -1;
	x = x*y;
	pref[i].push_back(x);
	//	printf("vai %d\n", x);
      }
    }

    rec(m-1);
    printf("Case #%d:", k);
    if (minm == 3000) printf(" IMPOSSIBLE");
    else imprimevetor();
    printf("\n");
  }
  return 0;
}
