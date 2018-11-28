#include <iostream>

using namespace std;

typedef long long ll;

int gcd(int u, int v){
    if(u == v || u == 0 || v == 0)
        return u|v;
    if(u%2 == 0){ // if u is even
        if(v%2 == 0) // if u and v are even
            return (2*gcd(u/2, v/2));
        else // u is even and v is odd
            return  gcd(u/2, v);
    }
    else if(v%2 == 0) // if u is odd and v is even
        return gcd(u, v/2);
    else{ // both are odd
        if(u>=v)
            return gcd((u-v)/2, v);
        else
            return gcd((v-u)/2, u);
    }
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    ll n;
    int pd, pg;
    cin >> n >> pd >> pg;
    cout << "Case #" << test << ": ";
    if (pg == 100 && pd != 100) {
      cout << "Broken" << endl;
      continue;
    }
    if (pd == 0) {
      cout << "Possible" << endl;
      continue;
    }
    if (pg == 0) {
      cout << "Broken" << endl;
      continue;
    }
    ll lcm = (ll)(pd * 100) / (ll)gcd(pd, 100);
    //cout << lcm << endl;
    if ((ll)(lcm / (ll)pd) <= n) {
      cout << "Possible" << endl;
    }
    else {
      cout << "Broken" << endl;
    }
  }
  return 0;
}

