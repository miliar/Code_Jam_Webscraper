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
#define MAX 1010

using namespace std;

int data[MAX];
int data2[MAX];
int n;
int main()
{
  freopen("D-large.in","r",stdin);
  freopen("Dlarge.out","w",stdout);
  int t;
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    scanf("%d",&n);
    FOR(i,0,n-1)
    {
      scanf("%d",&data[i]);
      data2[i] = data[i];
    }
    sort(data2,data2+n);
    double ans = 0.0f;
    FOR(i,0,n-1)
    {
      if(data2[i] != data[i]) ans += 1;
    }
    printf("Case #%d: %.6lf\n",ca,ans);
  }  
  return 0;
}
