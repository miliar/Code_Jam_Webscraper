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

//•’Ê‚Ìgcd(Å‘åŒö–ñ”)
LL gcd(LL x,LL y)
{
  if(y>x)swap(x,y);
  LL m = x%y;
  if(m==0)return y;
  return gcd(y,m);
}

//•’Ê‚Ìlcm(Å¬Œö”{”)
LL lcm(LL x,LL y)
{
  return (x/gcd(x,y))*y;
}

int main(void)
{
  int T,t;
  ll ret;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    ll N,Pg,Pd;
    cin>>N>>Pd>>Pg;

    if(Pd==0 && Pg==0)
    {
      cout<<"Case #"<<t<<": "<<"Possible"<<endl;
      continue;
    }
    if(Pd==0 || Pg==0)
    {
      cout<<"Case #"<<t<<": "<<"Broken"<<endl;
      continue;
    }
    if(Pd<100 && Pg==100)
    {
      cout<<"Case #"<<t<<": "<<"Broken"<<endl;
      continue;
    }
    ll gcdPd = gcd(Pd,100);
    Pd /= gcdPd;
    ll gcd100 = 100/gcdPd;

    if(gcd100>N)
    {
      cout<<"Case #"<<t<<": "<<"Broken"<<endl;
      continue;
    }
    cout<<"Case #"<<t<<": "<<"Possible"<<endl;
  }
  return 0;
}

