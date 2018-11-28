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

int main(void)
{
  int T,t;
  int ret;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N;
    cin>>N;
    vector<PI> vp;
    REP(i,N)
    {
      string s;
      int tmp;
      cin>>s>>tmp;
      int f = 0;
      if(s=="B")f = 1;
      vp.PB(MP(tmp,f));
    }
    VI pos(2,1);
    VI ct(2,0);
    ret = 0;
    int index=0;
    while(index<N)
    {
      int tmp_time;
      int npos = vp[index].first;
      int f = vp[index].second;
      index++;
      int opos = f^1;
      tmp_time = abs(npos - pos[f]) + 1;
      ret = max(ct[f] + tmp_time, ct[opos]+1);
      pos[f] = npos;
      ct[f] = ret;
    }


    cout<<"Case #"<<t<<": "<<ret<<endl;
  }
  return 0;
}

