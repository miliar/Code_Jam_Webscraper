#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cassert>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

ll gcd(ll a, ll b)
{
  if (b==0) return a;
  return gcd(b, a%b);
}

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    ll n, pd, pg;
    cin>>n>>pd>>pg;

    ll gd = gcd(pd, 100);
    ll gg = gcd(pg, 100);

    ll a = 100/gd, b = pd/gd, c = a-b;
    ll d = 100/gg, e = pg/gg, f = d-e;

    cout<<"Case #"<<cn<<": ";

    if (a > n){
      cout<<"Broken"<<endl;
      continue;
    }

    if (b>0 && e==0){
      cout<<"Broken"<<endl;
      continue;
    }

    if (c>0 && f==0){
      cout<<"Broken"<<endl;
      continue;
    }

    cout<<"Possible"<<endl;
  }
  return 0;
}
