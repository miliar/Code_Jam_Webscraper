#include<iostream>
#include<algorithm>
#include<vector>
#include<functional>

using namespace std;
typedef long long lint;

int main()
{
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n;
    cin >> n;
    vector<int> v1(n), v2(n);
    for (int i=0; i<n; ++i) cin >> v1[i];
    for (int i=0; i<n; ++i) cin >> v2[i];
    sort(v1.begin(), v1.end(), less<int>());
    sort(v2.begin(), v2.end(), greater<int>());
    lint ans(0);
    for (int i=0; i<n; ++i) ans += (lint)v1[i] * v2[i];
    cout << "Case #" << tc << ": " << ans << endl;
  }
  
  return 0;
}



