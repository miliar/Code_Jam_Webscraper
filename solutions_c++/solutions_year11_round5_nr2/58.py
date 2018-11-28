#include<cstdio>
#include<map>
#include<set>

using namespace std;

map<map<int, int>, int> memo;
set<int> X;
int XX=0;
int rec(map<int, int> o)
{
  if(memo.count(o))
    return memo[o];

  int ret = -1;
  for(set<int>::iterator it=X.begin(); it!=X.end(); ++it) {
    int f = *it, i;
    if(o[f] == 0) continue;
    map<int, int> t = o;
    for(i=f; ; ++i) {
      if(t[i] == 0) break;
      t[i]--;
      ret = max(ret, min(rec(t), i-f+1));
    }
  }
  return memo[o] = ret == -1 ? 1000 : ret;
}

void solve()
{
  int N;
  map<int, int> O;
  scanf("%d", &N);

  X.clear();
  for(int i=0; i<N; ++i) {
    int k;
    scanf("%d", &k);
    O[k]++;
    X.insert(k);
  }

  if(N == 0) {
    puts("0");
    return;
  }

  memo.clear();
  printf("%d\n", rec(O));
}

int main()
{
  int T;
  scanf("%d", &T);

  for(int C=1; C<=T; ++C) {
    fprintf(stderr, "%d\n", C);
    printf("Case #%d: ", C);
    solve();
  }
  return 0;
}

