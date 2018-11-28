#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<map>
#include<sstream>
#include<set>
#include<string>
#include<numeric>
#include<vector>
#include<cmath>

#define PB push_back
#define SZ(x) int((x).size())
#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);i++)

using namespace std;


const int MAX_N = 10005;

bool change[MAX_N];
bool val[2 * MAX_N];

int M;
const int inf = 1000000;

int dpt[MAX_N + 1][2];

int r(int n, bool t) {
  if(n >=(M-1)/2)
    return val[n]==t?0:inf;
  int &dp = dpt[n][t];
  if(dp > -1)
    return dp;
  dp=inf;
  int y[2][2];
  REP(i,2)
    REP(j,2)
    y[i][j]=min(r(2*n+1,i)+r(2*n+2,j),inf);

  int mini[2][2] = {
    {y[0][0], min(y[1][0], min(y[0][1], y[0][0]))},
    {min(min(y[1][1],y[0][1]),y[1][0]) , y[1][1]}};

  dp=min(dp,mini[t][val[n]]);
  if(change[n])
    dp=min(dp,1+mini[t][!val[n]]);
  return dp;
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1 ; t <= T ; t++)
    {
      printf("Case #%d: ", t);
      bool V;
      cin>>M>>V;
      memset(dpt,255,sizeof(dpt));
      REP(n,(M-1)/2)
        cin>>val[n]>>change[n];
      for(int n=(M-1)/2;n<M;n++)
        cin>>val[n];
      int y=r(0,V);
      if(y==inf)
        cout<<"IMPOSSIBLE";
      else
        cout<<y;
      puts("");
    }

  return 0;
}
