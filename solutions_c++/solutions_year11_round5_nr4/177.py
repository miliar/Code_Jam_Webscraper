#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

bool issq(ll n)
{
  ll t = (ll)sqrt((double)n);
  t = max(0ll, t-10);

  while(t*t<=n){
    if (t*t==n)
      return true;
    t++;
  }

  return false;
}

string bin(ll a)
{
  string tmp;
  while(a){
    tmp+=(char)('0'+a%2);
    a/=2;
  }
  reverse(tmp.begin(), tmp.end());
  return tmp;
}

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    string s; cin>>s;
    ll base = 0;
    vector<int> qs;
    for (int i=0; i<(int)s.length(); i++){
      if (s[i]!='?')
        base = (base << 1) | (s[i]-'0');
      else{
        base <<= 1;
        qs.push_back(i);
      }
    }

    int nn = qs.size();
    ll ans = 0;

    for (ll p=0; p<(1LL<<nn); p++){
      ll cur = base;
      for (int i=0; i<nn; i++){
        cur |= ((p >> i) & 1LL) * (1LL << (s.length()-1-qs[i]));
      }
      if (issq(cur)){
        ans = cur;
        break;
      }
    }

    cout<<"Case #"<<cn<<": "<<bin(ans)<<endl;
  }
  
  return 0;
}

