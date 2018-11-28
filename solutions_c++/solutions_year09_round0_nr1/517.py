#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<int> VI;

int readTok() {
  char c; cin >> c;
  if (c == '(') {
    int r = 0;
    while ((cin >> c) && (c != ')'))
      r ^= 1 << (c-'a');
    return r;
    }
  else return 1 << (c-'a');
  }

VI readPattern(int L) {
  VI ret;
  for (int i = 0; i < L; ++i)
    ret.push_back(readTok());
  return ret;
  }

bool match(string &s, VI &p, int L) {
  for (int i = 0; i < L; ++i)
    if (!(p[i] & (1 << (s[i]-'a'))))
      return false;
  return true;
  }

int main() {
  int L, D, N; cin >> L >> D >> N;
  vector<string> words(D);
  for (int i = 0; i < D; ++i)
    cin >> words[i];
  for (int c = 1; c <= N; ++c) {
    VI pattern = readPattern(L);
    int count = 0;
    for (int i = 0; i < D; ++i)
      if (match(words[i], pattern, L)) ++count;
    cout << "Case #" << c << ": " << count << '\n';
    }
  }