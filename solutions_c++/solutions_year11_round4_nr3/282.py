#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

typedef long long ll;

int main(int argc, char *argv[])
{
  vector<int> primes;
  vector<bool> flags(1001001, true);
  for (int i=2; i<(int)flags.size(); i++){
    if (flags[i]){
      primes.push_back(i);
      for (int j=i+i; j<(int)flags.size(); j+=i)
        flags[j]=false;
    }
  }

  int cases; cin>>cases;
  for (int cn = 1; cn <= cases; cn++) {
    ll n; cin>>n;

    if (n==1) {
      cout<<"Case #"<<cn<<": "<<0<<endl;
      continue;
    }

    map<ll, pair<ll, ll> > mm;
    for (int i=0; i<(int)primes.size(); i++){
      ll p = primes[i];
      mm[p]=make_pair(p, 1);
    }

    int ans = 1;

    while (mm.size()){
      ll cur = mm.begin()->first;
      ll p = mm.begin()->second.first;
      ll r = mm.begin()->second.second;
      mm.erase(mm.begin());
      if (cur > n) break;

      if (r>1) ans++;
      mm.insert(make_pair(cur*p, make_pair(p, r+1)));
    }

    cout<<"Case #"<<cn<<": "<<ans<<endl;
  }
  
  return 0;
}
