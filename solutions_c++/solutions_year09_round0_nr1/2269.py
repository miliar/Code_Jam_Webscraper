// BEGIN CUT HERE
// #define _GLIBCXX_DEBUG
#include "cout.h"
// END CUT HERE
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>
#include <complex>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long LL;
typedef complex<double> CMP;
#define Fill(a, b) memset((a), (b), sizeof(a))
#define REP(a, b) for (size_t (a) = 0; (a)<(size_t)(b); ++(a))
#define sz size()
#define Tr(c, i) for(typeof((c).begin()) i= (c).begin(); (i) != (c).end(); ++(i))
#define All(c) (c).begin(), (c).end()
#define Present(c, x) ((c).find(x) != (c).end()) // for Map or Set
#define CPresent(c, x) (find(All(c), x) != end()) // for vector

int main(void)
{
  vector <string> lang;
  int L, D, N;
  string word;
  cin >> L >> D >> N;
  REP(i, D) {
    cin >> word;
    lang.push_back(word);
  }

  REP(i, N) {
    int p = 0;
    vector < set < char > > m;
    cin >> word;
    REP(k, L) {
      set < char > mm;
      m.push_back(mm);
    }

    REP(j, word.sz) {
      if (word[j] == '(') {
        j++;
        while(word[j] != ')') {
          m[p].insert(word[j]);
          j++;
        }
      } else {
        m[p].insert(word[j]);
      }
      p++;
    }

    int count = 0;
    REP(j, lang.sz) {
      word = lang[j];
      bool ok = true;
      REP(k, word.sz) {
        char c = word[k];
        if (! Present(m[k], c)) {
          ok = false;
          break;
        }
      }
      if (ok)
        count++;
    }
    cout << "Case #" << (i+1) << ": " << count << endl;
  }


  return 0;
}



