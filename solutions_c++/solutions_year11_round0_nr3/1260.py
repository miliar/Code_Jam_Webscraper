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
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair


VI A;
PI Sean[1001];
int DP_pat[2][1<<20][3];//[0]flag, [1]min, [2]max
int N;


int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    cin>>N;
    A.clear();
    int sum = 0;
    int sumxor = 0;
    REP(i,N)
    {
      int tmp;
      cin>>tmp;
      A.PB(tmp);
      sum += tmp;
      sumxor ^= tmp;
    }
    memset(DP_pat,0,sizeof(DP_pat));
    DP_pat[0][A[0]][0] = 1;
    DP_pat[0][A[0]][1] = A[0];
    DP_pat[0][A[0]][2] = A[0];
    DP_pat[0][0][0] = 1;
    DP_pat[0][0][1] = 0;
    DP_pat[0][0][2] = 0;
    for(int i=0;i<N-1;i++)
    {
      for(int j = 0;j<((1<<20) - 1);j++)
      {
        if(DP_pat[i&1][j][0]==1)
        {
          int new_j = j^A[i+1];
          //A[i+1]‚ð‰Á‚¦‚éê‡
          int new_val_min = DP_pat[i&1][j][1] + A[i+1];
          int new_val_max = DP_pat[i&1][j][2] + A[i+1];
          if(DP_pat[(i+1)&1][new_j][0] != 1)
          {
            DP_pat[(i+1)&1][new_j][0] = 1;
            DP_pat[(i+1)&1][new_j][1] = new_val_min;
            DP_pat[(i+1)&1][new_j][2] = new_val_max;
          }
          else
          {
            DP_pat[(i+1)&1][new_j][1] = min(new_val_min, DP_pat[(i+1)&1][new_j][1]);
            DP_pat[(i+1)&1][new_j][2] = max(new_val_max, DP_pat[(i+1)&1][new_j][2]);
          }
          //A[i+1]‚ð‰Á‚¦‚È‚¢ê‡
          new_j = j;
          new_val_min = DP_pat[i&1][j][1];
          new_val_max = DP_pat[i&1][j][2];
          if(DP_pat[(i+1)&1][new_j][0] != 1)
          {
            DP_pat[(i+1)&1][new_j][0] = 1;
            DP_pat[(i+1)&1][new_j][1] = new_val_min;
            DP_pat[(i+1)&1][new_j][2] = new_val_max;
          }
          else
          {
            DP_pat[(i+1)&1][new_j][1] = min(new_val_min, DP_pat[(i+1)&1][new_j][1]);
            DP_pat[(i+1)&1][new_j][2] = max(new_val_max, DP_pat[(i+1)&1][new_j][2]);
          }
        }
      }
    }
    int flag = 0;
    int ret = 0;
    for(int j = 0;j<((1<<20) - 1);j++)
    {
      if(DP_pat[(N-1)&1][j][0]== 1 && (sumxor^j)== j)
      {
#ifdef DEBUG
cout<<"j="<<j<<endl;
#endif
        if(DP_pat[(N-1)&1][j][2]!=sum)
        {
          flag = 1;
          ret = max(ret,DP_pat[(N-1)&1][j][2]);
        }
        if(DP_pat[(N-1)&1][j][1]!=0)
        {
          flag = 1;
          ret = max(ret,sum - DP_pat[(N-1)&1][j][1]);
        }
      }
    }
    if(flag==0)
    {
      cout<<"Case #"<<t<<": "<<"NO"<<endl;
    }
    else
    {
      cout<<"Case #"<<t<<": "<<ret<<endl;
    }

  }
  return 0;
}

