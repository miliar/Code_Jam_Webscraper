#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
  int N; cin >> N;
  for (int n = 1; n <= N; n++) {
    int S; cin >> S;
    string s; getline(cin, s);

    map<string, int> ids;
    for (int i = 0; i < S; i++) { getline(cin, s); ids[s] = i; }

    int Q; cin >> Q; getline(cin, s);

    int res = 0, cntCur = 0;
    bool data[200]; memset(data, 0, sizeof data);

    for (int i = 0; i < Q; i++) {
      getline(cin, s);
      int id = ids[s];
      if (!data[id]) {
        if (cntCur == S - 1) {
          memset(data, 0, sizeof data);
          cntCur = 0;
          res++;
        }
        data[id] = true;
        cntCur++;
      }
    }

    cout << "Case #" << n << ": " << res << endl;
  }

  return 0;
}