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

int pos[3];
int times[3];
int n,x;
char turn[3];
int main()
{
  int t;
  freopen("A-large.in","r",stdin);
  freopen("Alarge.out","w",stdout);
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    scanf("%d",&n);
    memset(times,0,sizeof(times));
    pos[0] = pos[1] = 1;
    int waktu = 0;
    while(n--)
    {
      scanf("%s %d",turn,&x);
      int ind;
      if(turn[0] == 'O') ind =0;
      else if(turn[0] == 'B') ind = 1;
      int cnt = 1;
      cnt += abs(pos[ind] - x) + times[ind];
      pos[ind] = x;
      times[ind] = max(cnt,waktu + 1);
      waktu = max(times[0],times[1]);
    }
    printf("Case #%d: %d\n",ca,waktu);
  }
  return 0;
}
