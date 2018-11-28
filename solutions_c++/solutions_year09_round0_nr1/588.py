#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) do { fprintf(stderr, format, ## args); fflush(stderr); } while (0)
#define PRINT(format, args...) do { fprintf(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

struct Entry {
  Entry *pn[26];
  Entry() { memset(pn, 0, sizeof pn); }
};

Entry tr;
vector< vector<char> > qr;

void TrieInsert(Entry *tr, const char *ss);
int TrieQuery(const Entry *tr, const vector< vector<char> > &qr, int p, int L);

int main() {
  char bf[1008];
  int t, T, i, j, L, W;
  scanf("%d %d %d", &L, &W, &T);
  for (i=0; i<W; i++) {
    scanf("%s", bf);
    TrieInsert(&tr, bf);
  }
  for (t=1; t<=T; t++) {
    scanf("%s", bf);
    qr.clear();
    qr.resize(L);
    for (i=j=0; i<L; i++, j++)
      if (bf[j]!='(')
        qr[i].push_back(bf[j]);
      else
        while (bf[++j]!=')')
          qr[i].push_back(bf[j]);
    PRINT("Case #%d: %d\n", t, TrieQuery(&tr, qr, 0, L));
  }
  return 0;
}

void TrieInsert(Entry *tr, const char *ss) {
  int i=*ss-'a';
  if (i<0)
    return;
  if (tr->pn[i]==NULL)
    tr->pn[i]=new Entry();
  TrieInsert(tr->pn[i], ss+1);
}

int TrieQuery(const Entry *tr, const vector< vector<char> > &qr, int p, int L) {
  if (p==L)
    return 1;
  int i, A=0;
  for (i=0; i<SIZE(qr[p]); i++)
    if (tr->pn[qr[p][i]-'a']!=NULL)
      A+=TrieQuery(tr->pn[qr[p][i]-'a'], qr, p+1, L);
  return A;
}
