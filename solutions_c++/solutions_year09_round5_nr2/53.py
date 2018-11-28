#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "B"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

const int MOD = 10009;
const int LETTERS = 26;
const int MAX_LETTER_COUNT = 50 * 100;
const int MAX_POWER = 4;

map<char, int> GetPowers(const string& monomial) {
  map<char, int> result;
  for (int i = 0; i < monomial.length(); ++i) {
    result[monomial[i]]++;
  }
  return result;
}

int GetValue(const map<char, int>& powers, const map<char, int>& values, const vector< vector<int> >& power_mods) {
  int value = 1;
  for (map<char, int>::const_iterator it = powers.begin(); it != powers.end(); ++it) {
    map<char, int>::const_iterator it2 = values.find(it->first);
    if (it2 != values.end()) {
      value *= power_mods[it2->second][it->second];
      value %= MOD;
    } else {
      value = 0;
    }
  }
  return value;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  vector< vector<int> > power_mods(MAX_LETTER_COUNT + 1, vector<int>(MAX_POWER + 1, 0));
  for (int j = 1; j <= MAX_LETTER_COUNT; ++j) {
    power_mods[j][0] = 1;
    for (int k = 1; k <= MAX_POWER; ++k) {
      power_mods[j][k] = (power_mods[j][k - 1] * j) % MOD;
    }
  }
  for (int test_index = 0; test_index < test_count; ++test_index) {
    cerr << "test " << test_index + 1 << " of " << test_count << endl;
    string poly;
    int max_words;
    cin >> poly >> max_words;
    int word_count;
    cin >> word_count;
    vector<string> words(word_count);
    for (int i = 0; i < word_count; ++i) {
      cin >> words[i];
    }
    vector< map<char, int> > letter_counts(word_count);
    for (int i = 0; i < word_count; ++i) {
      for (int j = 0; j < words[i].length(); ++j) {
        letter_counts[i][words[i][j]]++;
      }
    }
    vector<string> monomials;
    poly += '+';
    string cur_monomial = "";
    for (int i = 0; i < poly.length(); ++i) {
      if (poly[i] == '+') {
        monomials.push_back(cur_monomial);
        cur_monomial = "";
      } else {
        cur_monomial += poly[i];
      }
    }
    vector< map<char, int> > powers(monomials.size());
    for (int i = 0; i < monomials.size(); ++i) {
      powers[i] = GetPowers(monomials[i]);
    }

    vector< map< map<int, int>, int > >such_words_count(max_words + 1);
    map<int, int> empty;
    such_words_count[0][empty] = 1;
    for (int used = 0; used < max_words; ++used) {
      for (map< map<int, int>, int>::const_iterator it = such_words_count[used].begin();
           it != such_words_count[used].end();
           ++it) {
        map<int, int> current = it->first;
        for (int word_index = 0; word_index < word_count; ++word_index) {
          map<int, int> next = current;
          next[word_index]++;
          int sum = such_words_count[used + 1][next] + it->second;
          if (sum >= MOD) {
            sum -= MOD;
          }
          such_words_count[used + 1][next] = sum;
        }
      }
    }


    cout << "Case #" << test_index + 1 << ":";

    for (int used = 1; used <= max_words; ++used) {
      int result = 0;
      for (map< map<int, int>, int>::const_iterator it = such_words_count[used].begin();
           it != such_words_count[used].end();
           ++it) {
        int term = it->second % MOD;
        map<int, int> word_counts = it->first;
        map<char, int> values;
        for (map<int, int>::const_iterator it2 = word_counts.begin(); it2 != word_counts.end(); ++it2) {
          int word_index = it2->first;
          for (map<char, int>::const_iterator it3 = letter_counts[word_index].begin(); it3 != letter_counts[word_index].end(); ++it3) {
            values[it3->first] += it2->second * it3->second;
          }
        }
        int sum = 0;
        for (int i = 0; i < powers.size(); ++i) {
          sum += GetValue(powers[i], values, power_mods);
          if (sum >= MOD) {
            sum -= MOD;
          }
        }
        result = (result + sum * term) % MOD;
      }
      cout << ' ' << result;
    }
    cout << endl;
  }
  return 0;
}
