#include <cstdio>
#include <cstring>
#include <map>
#include <set>

using namespace std;

const int MAXN = 1000;
char S[MAXN + 1];

map<char, char> leet;
map<pair<char, char>, int> G;
set<pair<char, char> > q;
int k;

void add(char u, char v)
{
  ++G[make_pair(u, v)];
}

void solve()
{
  int N = strlen(&S[0]);

  if (N == 1) {
    printf("%d\n", 1 + (leet.find(S[0]) != leet.end()));
    return;
  }

  q.clear();
  G.clear();

  for (int i = 0; i < N-1; ++i) {
    if (q.find(make_pair(S[i], S[i+1])) != q.end()) continue;
    q.insert(make_pair(S[i], S[i+1]));

    add(S[i], S[i+1]);
    if (leet.find(S[i]) != leet.end()) add(leet[S[i]], S[i+1]);
    if (leet.find(S[i+1]) != leet.end()) add(S[i], leet[S[i+1]]);
    if (leet.find(S[i]) != leet.end() && leet.find(S[i+1]) != leet.end()) add(leet[S[i]], leet[S[i+1]]);
  }

  int res = 1;

  map<char, int> out_pow, in_pow;

  for (map<pair<char, char>, int>::iterator z = G.begin(); z != G.end(); ++z) {
    out_pow[z->first.first] += z->second;
    in_pow[z->first.second] += z->second;
    res += z->second;
  }

  int delta = 0;

  for (map<char, int>::iterator z = out_pow.begin(); z != out_pow.end(); ++z) {
    char ch = z->first;
    if (out_pow[ch] > in_pow[ch]) { res += out_pow[ch] - in_pow[ch]; delta = 1; }
  }

  printf("%d\n", res - delta);
}

int main()
{
  leet['o'] = '0'; leet['0'] = 'o';
  leet['i'] = '1'; leet['1'] = 'i';
  leet['e'] = '3'; leet['3'] = 'e';
  leet['a'] = '4'; leet['4'] = 'a';
  leet['s'] = '5'; leet['5'] = 's';
  leet['t'] = '7'; leet['7'] = 't';
  leet['b'] = '8'; leet['8'] = 'b';
  leet['g'] = '9'; leet['9'] = 'g';

  int T; scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    scanf("%d%s", &k, &S[0]);

    solve();
  }

  return 0;
}
