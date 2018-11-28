#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long ll;

int readint() { 
  int i, j, s;
  while (!isdigit(i = getchar()) && i != '-');
  if (i == '-') { s = -1; j = 0; }
  else { s = 1; j = i - '0'; }
  while (isdigit(i = getchar())) j = ((j << 1) + (j << 3) + (i - '0'));
  return j * s;
}

const int MOD = 10009;

int N, K;
vector<string> terms;
int cnt[100][300];


int main() {
  int cases = readint();
  rep (ca, cases) {
    string pol, tmp;
    cin >> pol >> K;
    terms.clear();
    rep (i, pol.length()) {
      if (isalpha(pol[i])) {
        tmp += pol[i];
        continue;
      }
      if (tmp != "") terms.pb(tmp);
      tmp = "";
    }
    if (tmp != "") terms.pb(tmp);

    N = readint();
    memset(cnt, 0, sizeof(cnt));
    rep (i, N) {
      cin >> tmp;
      rep (j, tmp.length()) cnt[i][(int)tmp[j]]++;
    }

    int ans[20] = {0};
    rep (i, terms.size()) {
      string S = terms[i];
      sort(all(S));
      S.erase(unique(all(S)), S.end());
      int M = S.length();
      
      map<vector<int>, int> dp[20];
      dp[0][vector<int>(M)] = 1;
      rep (k, K) {
        tr (dp[k], ite) {
          const vector<int> &prvv = ite->first;
          int prvc = ite->second;
          rep (i, N) {
            vector<int> v = prvv; 
            rep (j, M) v[j] += cnt[i][(int)S[j]];
            dp[k + 1][v] += prvc;
            dp[k + 1][v] %= MOD;
          }
        }
      }

      string T = terms[i];
      for (int k = 1; k <= K; k++) {
        tr (dp[k], ite) {
          const vector<int> &v = ite->first;
          int x = ite->second;
          rep (i, T.size()) {
            // printf("%c: %d\n", T[i], (int)S.find(T[i]));
            x *= v[(int)S.find(T[i])];
            x %= MOD;
          }
          ans[k] += x;
          ans[k] %= MOD;
        }
      }
    }

    printf("Case #%d: ", ca + 1);
    for (int k = 1; k <= K; k++) {
      if (k > 1) putchar(' ');
      printf("%d", ans[k]);
    }
    puts("");
  }
}
