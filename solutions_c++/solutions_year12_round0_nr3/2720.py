#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

int a,b;
bool flags[10000200];

int f(long long x)
{
  long long ret = 0;
  long long y = x;
  int len = 0;
  while(y > 0)
  {
    y /= 10;
    len++;
  }
  if(len <= 0) return 0;
  y = 1;
  FOR(i,1,len-1) y *= 10;
  //cerr << "============================" << endl;
  //cerr << y << endl;
  long long aa = x;
  FOR(i,0,len-1)
  {
    int z = aa / y;
    aa = (aa % y) * 10 + z;
    if(aa <= x) continue;
    if(flags[aa]) continue;
    flags[aa] = true;
    //cerr << x << " " << aa << endl;
    if(aa >= a && aa <= b) ret++;
  }
  FOR(i,0,len-1)
  {
    int z = aa/y;
    aa = (aa % y) * 10 + z;
    flags[aa] = false;
  }
  return ret;
}

int main()
{
  freopen("C-large.in","r",stdin);
  freopen("C-large.out","w",stdout);
  memset(flags,false,sizeof(flags));
  int t;
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    int ans = 0;
    scanf("%d %d",&a,&b);
    FOR(x,a,b)
    {
      ans += f(x);
    }
    printf("Case #%d: %d\n",ca,ans);
  }
  return 0;
}
