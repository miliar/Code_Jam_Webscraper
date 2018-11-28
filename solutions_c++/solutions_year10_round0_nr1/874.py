#include <iostream>
#include <algorithm>
#define fr(i,N) for(i = 0; i <(int)N; i++)
#define SZ(u) ((int)u.size())

using namespace std;

int main() {
  int t, T, N, K;
  cin >> T;

  fr (t, T) {
    cin >> N >> K;
    cout << "Case #" << t+1 << ": "
      << (((K%(1<<N)) == (1<<N)-1) ? "ON" : "OFF") << endl;
  }
  return 0;
}
