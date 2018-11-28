#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <memory.h>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef long double dbl;

#define x first
#define y second
#define pnt pair <int, int>
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

#define maxl 30
#define maxn 10010

int T;
int N, M;
char s[maxn][maxl];
int len[maxn];
int cont[maxn][26];
char seq[maxn];

int cands[maxn], valid[maxn], clen;

vector <int> lenv[11], letp[26][1100];

int main() {
  scanf("%d", &T);
  forn (q, T) {
    scanf("%d %d", &N, &M);

    forn (i, 11) {
      lenv[i].clear();
    }
    forn (i, 26) {
      forn (j, 1024) {
        letp[i][j].clear();
      }
    }
    forn (i, N) {
      scanf("%s", s[i]);
      memset(cont[i], 0, sizeof(int) * 26);
      int k = len[i] = strlen(s[i]);
      forn (j, k) {
        cont[i][s[i][j] - 'a'] |= 1 << j;
      }
    }

    printf("Case #%d:", q + 1);
    forn (w, M) {
      scanf("%s", seq);
  
      int best = 0, besti = 0;
      forn (an, N) {
        int cur = 0;

        clen = 0;
        forn (i, N) {
          if (len[i] == len[an]) {
            cands[clen] = i;
            valid[clen++] = 1;
          }
        }
        forn (i, 26) {
          int c = seq[i] - 'a';
          int any = 0, err = !cont[an][c];
          forn (j, clen) {
            int k = cands[j];
            any |= !!cont[k][c];
            valid[j] &= cont[k][c] == cont[an][c];
          }
          cur += any & err;
          int cnew = 0;
          forn (j, clen) {
            cands[cnew] = cands[j];
            cnew += valid[j];
            valid[j] = 1;
          }
          clen = cnew;
        }
        if (cur > best) {
          best = cur;
          besti = an;
        }
      }
      printf(" %s", s[besti]);
    }
    puts("");
  }

  return 0;
}

