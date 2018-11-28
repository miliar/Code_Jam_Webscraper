#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int ti = 1; ti <= T; ++ti) {
    int n, s, p;
    cin >> n >> s >> p;

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int score;
      cin >> score;
      int mm = score / 3 + (score % 3 != 0);
      if (mm >= p)
        ++ans;
      else if (s > 0)
      {
        // (x   x x)   --> (x-1 x   x+1)
        // (x-1 x x) --> (x-1 x-1 x+1)
        if (score % 3 != 1 && 0 <= mm - 1 && mm + 1 <= 10 && mm + 1 >= p)
          ++ans, --s;
      }
    }

    cout << "Case #" << ti << ": " << ans << "\n";
  }
  return 0;
}
