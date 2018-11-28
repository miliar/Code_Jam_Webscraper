#include <iostream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

const int maxs=100;
const int maxq=1000;
int s,n,q;
char str[150];
map<string, int> number;
int next[maxs+10];
int a[maxq+10];
int p[maxq+10];
int ans;

void init() {
  scanf("%d\n", &s);
  number.clear();
  int k=0;
  for (int i=1; i<=s; ++i) {
    gets(str);
    if (number[str] == 0) {
      ++k;
      number[str] = k;
    }
  }
  scanf("%d\n", &q);
  memset(next, 0, sizeof(next));
  for (int i=1; i<=q; ++i) {
    gets(str);
    a[i] = number[str];
    if (next[a[i]] == 0) next[a[i]] = i;
  }
  for (int i=1; i<=s; ++i) {
    if (next[i] == 0) {
      next[i] = q+1;
    }
  }
  memset(p, 0, sizeof(p));
  for (int i=1; i<q; ++i) {
    for (int j=i+1; j<=q; ++j) {
      if (a[i] == a[j]) {
	p[i] = j;
	break;
      }
    }
  }
  for (int i=1; i<=q; ++i) {
    if (p[i] == 0) p[i] = q+1;
  }
  //for (int i=1; i<=q; ++i) cout<<p[i]<<" ";
}

void solve() {
  ans = 0;
  int x = 1;
  for (int i=2; i<=s; ++i) {
    if (next[i]>next[x]) x = i;
  }
  int now = next[x];
  while (now <= q) {
    ++ans;
    //cout<<now<<endl;
    for (int i=1; i<=s; ++i) {
      while (next[i]<now) {
	next[i] = p[next[i]];
      }
    }
    for (int i=1; i<=s; ++i) {
      if (next[i]>next[x]) x = i; 
    }
    now = next[x];
  }
}

int main() {
  scanf("%d\n", &n);
  for (int kase=1; kase<=n; ++kase) {
    init();
    solve();
    printf("Case #%d: %d\n", kase, ans);
  }
  return 0;
}

