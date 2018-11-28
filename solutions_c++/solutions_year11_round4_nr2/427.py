#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector<PI>	VPI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define PB(a)  push_back(a)
#define MP(a,b)  make_pair(a,b)
#define MEMZ(a) memset(a,0,sizeof(a))
#define ITER(c) __typeof((c).begin())
#define PRESENT(c, e) ((c).find((e)) != (c).end())
#define CPRESENT(c, e) (find(all(c), (e)) != (c).end())
#define TR(c, i) for (ITER(c) i = (c).begin(); i != (c).end(); ++i)

#define INF INT_MAX

#define MOD 1000000009

int sheet[510][510];

int R,C,D;

int search(int r,int c, int n)
{
  int ret = 0;
  while(1)
  {
    ll sum1,sum2,sum3,sum4;
    int nn = n+1;
    if((r-nn)<0 || (r+nn)>=R || (c-nn)<0 || (c+nn)>=C)return ret;
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for(int i = 1;i<nn;i++)
    {
      //横チェック
      for(int j = c-nn;j<=c+nn;j++)
      {
        sum1 += sheet[r-i][j]*i;
        sum2 += sheet[r+i][j]*i;
      }
      //縦チェック
      for(int j = r-nn;j<=r+nn;j++)
      {
        sum3 += sheet[j][c-i]*i;
        sum4 += sheet[j][c+i]*i;
      }
    }
    //大外は角をけずる
    //横チェック
    for(int j = c-nn+1;j<=c+nn-1;j++)
    {
      sum1 += sheet[r-nn][j]*nn;
      sum2 += sheet[r+nn][j]*nn;
    }
    //縦チェック
    for(int j = r-nn+1;j<=r+nn-1;j++)
    {
      sum3 += sheet[j][c-nn]*nn;
      sum4 += sheet[j][c+nn]*nn;
    }
    if(sum1==sum2 && sum3== sum4)ret = 2*nn+1;
    //偶数のケース
    if((r-nn)<0 || (r+1+nn)>=R || (c-nn)<0 || (c+1+nn)>=C)return ret;
    sum1 = 0;
    sum2 = 0;
    sum3 = 0;
    sum4 = 0;
    for(int i = 0;i<nn;i++)
    {
      //横チェック
      for(int j = c-nn;j<=c+1+nn;j++)
      {
        sum1 += sheet[r-i][j]*(2*i+1);
        sum2 += sheet[r+1+i][j]*(2*i+1);
      }
      //縦チェック
      for(int j = r-nn;j<=r+1+nn;j++)
      {
        sum3 += sheet[j][c-i]*(2*i+1);
        sum4 += sheet[j][c+1+i]*(2*i+1);
      }
    }
    //大外は角をけずる
    //横チェック
    for(int j = c-nn+1;j<=c+1+nn-1;j++)
    {
      sum1 += sheet[r-nn][j]*(2*nn+1);
      sum2 += sheet[r+1+nn][j]*(2*nn+1);
    }
    //縦チェック
    for(int j = r-nn+1;j<=r+1+nn-1;j++)
    {
      sum3 += sheet[j][c-nn]*(2*nn+1);
      sum4 += sheet[j][c+1+nn]*(2*nn+1);
    }
    if(sum1==sum2 && sum3== sum4)ret = 2*nn+2;
    n++;
  }
  return ret;
}

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int ret = 0;
    cin>>R>>C>>D;
    REP(r,R)
    {
      string tmp;
      cin>>tmp;
      REP(c,C)
      {
        sheet[r][c] = tmp[c] - '0';
      }
    }
    REP(r,R)
    {
      REP(c,C)
      {
        int tmp;
        tmp = search(r,c,0);
        ret = max(ret,tmp);
      }
    }
    if(ret==0)
      cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
    else
      cout<<"Case #"<<t<<": "<<ret<<endl;
  }
  return 0;
}

