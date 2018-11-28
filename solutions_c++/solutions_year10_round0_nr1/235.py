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
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
typedef long long LL;
typedef unsigned int UINT;

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,K;
    cin>>N;
    cin>>K;
//cout<<"N="<<N<<"  K="<<K<<endl;
    string result;
    int term = 1<<N;
    int state=term - 1;
    result = "OFF";
    if((K%term) == state)
    {
      result = "ON";
    }

    cout<<"Case #"<<t<<": "<<result<<endl;
  }
  return 0;
}
