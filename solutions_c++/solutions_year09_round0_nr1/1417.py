#include<iostream>
#include<map>
#include<string>
using namespace std;

#define N 100000

int next[N][26], n[20], a[20][30];
int last, ans, L;

void insert(const string &s) {
  int cur, i;

  cur = 0;
  for (i = 0; i < L; i++) {
    if (next[cur][s[i]-'a'] == 0) next[cur][s[i]-'a'] = ++last;
    cur = next[cur][s[i]-'a'];
  }
}

void parse(const string &s) {
  int i, j;
  
  j = 0;
  for (i = 0; i < L; i++) {
    if (s[j] != '(') {
      n[i] = 1;
      a[i][0] = s[j]-'a';
      j++;
    }
    else {
      j++;
      n[i] = 0;
      while (s[j] != ')') {
	a[i][n[i]] = s[j]-'a';
	n[i]++;
	j++;
      }
      j++;
    }
  }
}

void rek(int cur, int x) {
  if (x == L) {
    ans++;
    return;
  }
  for (int i = 0; i < n[x]; i++) {
    if (next[cur][ a[x][i] ] > 0) rek(next[cur][ a[x][i] ], x+1);
  }
}

int main() {
  int D, NQ, i;
  string s;

  cin >> L >> D >> NQ;
  for (i = 0; i < D; i++) {
    cin >> s;
    insert(s);
  }
  for (i = 1; i <= NQ; i++) {
    cin >> s;
    parse(s);
    ans = 0;
    rek(0, 0);
    printf("Case #%d: %d\n", i, ans);
  }
  return 0;
}
