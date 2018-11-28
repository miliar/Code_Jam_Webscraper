#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
#define ll long long 

ll gcd( ll a, ll b){
  return (b == 0 ? a : gcd(b, a%b));  
}

int main(){
  int T;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    int N;
    cin >> N;
    ll a[N];
    for (int i=0; i<N; i++) cin >> a[i];
    sort (a, a+N);
    ll k = a[0];
    N--;
    for (int i=0; i<N; i++) a[i] = a[i+1] - a[i];
    ll g = a[0];
    for (int i=1; i<N; i++){
      g = gcd( g, a[i]);
    }
    ll ans = g - (k % g);
    if (ans == g) ans = 0;

    printf ("Case #%d: %lld\n", iii+1, ans);
  }
}
