#include <cstdio>
#include <iostream>

using namespace std;

int main(void) {
  int t;
  cin >> t;
  for(int c=1;c<=t;c++) {
    int n, k;
    cin >> n >> k;
    cout << "Case #" << c << ": ";
    cout << (((k+1)%(1<<n) == 0)?"ON":"OFF") << endl;
  }
  return(0);
}
