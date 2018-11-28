#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

int solve(int n[], const int size)
{
  int sum = accumulate(n, n + size, 0);
  sort(n, n + size);
  return sum - *min_element(n, n + size);
}

int main(void)
{
  int tc, cnt = 0;
  cin >> tc;
  while( tc-- ){
    int n;
    cin >> n;
    int m[n];
    for(int i=0; i<n; ++i){
      cin >> m[i];
    }

    int bit = 0;
    for(int i=0; i<n; ++i){
      bit = bit ^ m[i];
    }
    
    if( bit ) cout << "Case #" << ++cnt << ": NO" << endl;
    else cout << "Case #" << ++cnt << ": " << solve(m, n) << endl;
  }
  return 0;
}
