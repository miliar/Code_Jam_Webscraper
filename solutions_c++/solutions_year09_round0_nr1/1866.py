#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Q {
  int q[16];
};

int main()
{
  vector<Q> dic;

  int L, D, N;
  cin >> L >> D >> N;
  for (int i = 0; i < D; i++) {
    string s;
    cin >> s;
    Q q = {{0}};
    int k = 0;
    for (int j = 0; j < s.size(); j++, k++) {
      q.q[k] = 1 << (s[j] - 'a');
    }
    dic.push_back(q);
  }
  for (int i = 0; i < N; i++) {
    string s;
    cin >> s;
    Q q = {{0}};
    int k = 0;
    for (int j = 0; j < s.size(); j++, k++) {
      if (s[j] == '(') {
        j++;
        while (s[j] != ')') {
          q.q[k] |= 1 << (s[j] - 'a');
          j++;
        }
      } else {
        q.q[k] |= 1 << (s[j] - 'a');
      }
    }

    int count = 0;
    for (int j = 0; j < D; j++) {
      bool ok = true;
      Q& d = dic[j];
      for (int k = 0; k < L; k++) {
        if ((d.q[k] & q.q[k]) == 0) {
          ok = false;
          break;
        }
      }
      if (ok) count++;
    }
    cout << "Case #" << i+1 << ": " << count << endl;
  }
  
  return 0;
}
