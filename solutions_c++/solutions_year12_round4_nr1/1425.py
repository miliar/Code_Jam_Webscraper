#include<cassert>
#include<queue>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>
#define eprintf(...) {fprintf(stderr, __VA_ARGS__);fflush(stderr);}

#define eps 1e-12

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;
set<pair<int,int> > was;
const int N = 2000;
int l[N],d[N],n,D;
bool dfs(int x,int v){
  if(was.count(mp(x, v) )) 
    return false;
  was.insert(mp(x, v) );
  int go = min(2*d[v] - x, d[v] + l[v]);
  if(go >= D)
    return true;
  for(int i = v + 1; i < n;i++){
    if(d[v] - d[i] <= l[i] && go >= d[i])
      if(dfs(d[v], i))
        return true;
  }
  return false;
}
int main()         
{
  /*#ifdef DEBUG
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif*/
  int __;
  scanf("%d",&__);
  forn(_,__){
    printf("Case #%d: ",_+1);
    was.clear();
    scanf("%d",&n);
    forn(i,n) 
      scanf("%d %d",&d[i],&l[i]);
    scanf("%d",&D);
    if(dfs(0, 0))
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}

