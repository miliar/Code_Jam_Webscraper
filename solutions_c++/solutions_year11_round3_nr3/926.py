#include <iostream>
#include <vector>

using namespace std;

int gcd(int a, int b)
{
  return b ? gcd(b, a%b) : a;
}

int lcm(int a, int b)
{
  return a / gcd( max(a, b), min(a, b) ) * b;
}

int main(void)
{
  int tc;
  int cnt = 0;
  cin >> tc;
  while( tc-- ){
    int n, h, l;

    cin >> n >> l >> h;
    int m[n+1];
    for(int i=0; i<n; ++i){
      cin >> m[i];
    }    

    int r = 1;

    const int size = n + 1;
    for(int i=l; i<=h; ++i){
      m[n] = i;
      int div = 0;

      for(int j=0; j<n; ++j){
        if( i % m[j] == 0 || m[j] % i == 0 ) {
          ++div;
        }
      }
      if( div == n ){
        r = i;
        break;
      }
    }

    cout << "Case #" << ++cnt << ": " << flush;
    if(l <= r && r <= h ) cout << r << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
