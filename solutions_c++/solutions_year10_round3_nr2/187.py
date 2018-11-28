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
static const double EPS = 1e-5;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;

//#define DEBUG_PRINT

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int ret = 0;
    int L,P,C;
    cin>>L;
    cin>>P;
    cin>>C;
    int i,j;
    ll mul_val = C;

    while(1)
    {
      ll val = L*mul_val;
      if(val>=P)break;
      mul_val *=mul_val;
      ret++;
    }
    cout<<"Case #"<<t<<": "<<ret<<endl;
  }
  return 0;
}
