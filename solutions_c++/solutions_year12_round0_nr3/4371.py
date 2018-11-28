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

int f(int x){
  int mn = 1<<30;
  int t = 1;
  while(t * 10 <= x)
    t *= 10;
  forn(_,7){
    int k = x%10;
    x = t * k + x / 10;
    mn = min(x, mn);
  }
  return mn;
}

int main()         
{
  #ifdef DEBUG
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif
  int __;
  scanf("%d",&__);
  forn(_, __){
    deb(_);
    printf("Case #%d: ",_+1);
    int a,b,ans = 0;
    scanf("%d %d\n",&a,&b);
    for(int i = a;i<=b;i++)
      for(int j = a;j < i;j++)
        if(f(i) == f(j))
          ans++;
    printf("%d\n",ans);
  }
  return 0;
}

