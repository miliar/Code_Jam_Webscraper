#include <iostream>
#include <algorithm>
#include <vector>
#include <complex>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <bitset>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef complex<double> C;

const double pi = 3.141592653589793238462643383279;
const double napier = 2.718281828459045235360287471352;
const C eye = C(0, 1);

#define FOR(i,n) for (unsigned i = 0; i < (n); ++i)
#define REP(i,n) for (unsigned i = 1; i <= (n); ++i)
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).begin(), (v).end()

int L, D, N;

typedef bitset<26> LT;
typedef vector<LT> W;
vector<W> words;

LT parse_letter(string &s, int &pos)
{
  LT letter;
  if (s[pos] == '(') {
    ++pos;
    while (s[pos] != ')') {
      letter[s[pos] - 'a'] = 1;
      ++pos;
    }
  } else {
    letter[s[pos] - 'a'] = 1;
  }
  ++pos;
  return letter;
}

W make_word(string s)
{
  W w;
  int pos = 0;
  FOR (i, L)
    w.push_back(parse_letter(s, pos));
  return w;
}

bool match_words(W &a, W &b)
{
  bool flag = true;
  FOR (i, L) {
    if ((a[i] & b[i]).none()) {
      flag = false;
      break;
    }
  }
  return flag;
}

int main()
{
  cin >> L >> D >> N;

  FOR (i, D) {
    string s;
    cin >> s;
    words.push_back(make_word(s));
  }

  FOR (i, N) {
    string s;
    cin >> s;
    W w = make_word(s);

    int cnt = 0;
    FOR (j, words.size())
      if (match_words(w, words[j]))
        ++cnt;
    cout << "Case #" << i + 1 << ": " << cnt << endl;
  }

  return 0;
}
