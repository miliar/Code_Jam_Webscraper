#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;
typedef vector<ll> vi;

ll gcd(ll a, ll b) {
  return (b==0?a:gcd(b,a%b));
}

int main() {
  int t;
  cin>>t;
  for (int nc=1;nc<=t;++nc) {
    cout<<"Case #"<<nc<<": ";
    int n;
    ll l,h;
    cin>>n>>l>>h;
    vi num(n);
    for (int i=0;i<n;++i) cin>>num[i];
//     sort(num.begin(),num.end());
    bool found=false;
    for (int i=l;i<=h and not found;++i) {
      bool ok=true;
      for (int j=0;j<n and ok;++j) {
        if (num[j]<i) ok=(i%num[j]==0);
        else ok=(num[j]%i==0);
      }
      found=ok;
      if (found) cout<<i<<endl;
    }
    if (not found) cout<<"NO"<<endl;
  }
}
