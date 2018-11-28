#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int cs(const string &s) 
{
  int cs = 1;
  char c = s[0];
  for (int i = 1; i < s.size(); i++) {
    cs += (s[i] != c);
    c = s[i];
  }
  return cs;
}

int main()
{
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    int k;
    string s;
    cin >> k >> s;

    int p[k];
    for (int i = 0; i < k; i++) {
      p[i] = i;
    }

    int ans = s.size();
    do {
      string t;
      for (int i = 0; i < s.size(); i++) {
	t += s[p[i%k] + i/k*k];
      }

      ans = min(ans, cs(t));
    } while (next_permutation(p, p+k));


    cout << "Case #" << C << ": " << ans << endl;
  }

  return 0;
}
