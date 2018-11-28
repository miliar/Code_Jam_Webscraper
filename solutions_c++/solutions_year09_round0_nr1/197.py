#include <iostream>
#include <string>
#include <cstring>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, (n))

int L, D, N;
string dic[10000];
int have[30][300];

int main() {
  string word;
  cin >> L >> D >> N;
  REP(i, D) cin >> dic[i];
  REP(i, N) {
    cin >> word;
    memset(have, 0, sizeof have);
    int k = 0;
    REP(j, L) {
      if (word[k] == '(') {
	k++;
	while (isalpha(word[k])) {
	  have[j][word[k++]] = 1;
	}
	k++;
      } else have[j][word[k++]] = 1;
    }

    int ans = 0;
    REP(j, D) {
      int flag = 1;
      REP(k, L) 
	if (!have[k][dic[j][k]]) {
	  flag = 0;
	  break;
	}
      ans += flag;
    }
    cout << "Case #" << (i + 1) << ": " << ans << endl;
  }
}
