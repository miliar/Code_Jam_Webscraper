#include <deque>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int testCase;
  cin >> testCase;

  for(int loop=1; loop<=testCase; loop++) {
    int n;
    cin >> n;

    deque<long long> a, b;
    for(int i=0; i<n; i++) {
      int temp;
      cin >> temp;
      a.push_back(temp);
    }
    for(int i=0; i<n; i++) {
      int temp;
      cin >> temp;
      b.push_back(temp);
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    long long ans = 0;
    while(!a.empty() && a.front() * b.back() <= 0) {
      ans += a.front() * b.back();
      a.pop_front();
      b.pop_back();
    }
    while(!a.empty() && a.back() * b.front() <= 0) {
      ans += a.back() * b.front();
      a.pop_back();
      b.pop_front();
    }
    while(!a.empty()) {
      ans += a.front() * b.back();
      a.pop_front();
      b.pop_back();
    }

    cout << "Case #" << loop << ": " << ans << endl;
  }
 
  return 0;
}
