#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

int memo[200][20];
int n,s,p;
int total[200];

int f(int ind,int sup)
{
  //cout << ind << " " << sup << " " << p << endl;
  if(ind >= n) return 0;
  int & ret = memo[ind][sup];
  if(ret != -1) return ret;
  int x = total[ind] / 3;
  int y = x;
  int z = total[ind] %3;
  if(total[ind] > 0) y++;
  if(z > 0) x++;
  if(z ==2) y++;
  ret = f(ind+1,sup) + (x >= p);
  if(sup > 0 && x < y) ret = max(ret,f(ind + 1,sup - 1) + (y >= p));
  return ret;
}

int main()
{
  freopen("B-small-attempt0.in","r",stdin);
  freopen("B.out","w",stdout);
  int t;  
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    memset(memo,-1,sizeof(memo));
    scanf("%d %d %d",&n,&s,&p);
    FOR(i,0,n-1) scanf("%d",&total[i]);
    printf("Case #%d: %d\n",ca,f(0,s));
  }
  return 0;
}
