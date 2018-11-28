#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;

#define maxn 10010
#define maxm 110

#define psb push_back

int T, n, m;
string D[maxn];
string L[maxm];
string ans[maxm];
string md[maxn];

vector<string> v1, v2;
char st[30];

bool yes(string D[], string &now, char letter) {
  for(int i = 0; i < n; i++) {
    if (md[i] == now && D[i].find(letter) != string::npos) return true;
  }
  return false;
}

void guess(char letter, string &now, string &word) {
  for(int i = 0; i < word.length(); i++)
    if (word[i] == letter) now[i] = word[i];
}

int evaluate(string D[], string &ls, string &word) {
  string now;
  for(int i = 0; i < word.length(); i++)
    now += "?";
  for(int i = 0; i < n; i++) {
    md[i] = "";
    for(int j = 0; j < D[i].length(); j++)
      md[i] += "?";
  }
  int cnt = 0;
  for(int i = 0; i < 26; i++) {
    if (yes(D, now, ls[i])) {
      guess(ls[i], now, word);
      for(int j = 0; j < n; j++)
        guess(ls[i], md[j], D[j]);
      if (word.find(ls[i]) == string::npos) cnt ++;
      if (word == now) return cnt;
    }
  }
}

int main() {

  freopen("B-small.in", "rt", stdin);
  freopen("B-small.out", "wt", stdout);
  
  scanf("%d\n", &T);
  for(int cT = 0; cT < T; cT ++) {
  
    scanf("%d%d\n", &n, &m);
    for(int i = 0; i < n; i++) {
      memset(st,0,sizeof(st));
      gets(st);
      D[i] = st;
    }
    for(int i = 0; i < m; i++) {
      memset(st,0,sizeof(st));
      gets(st);
      L[i] = st;
    }
    for(int i = 0; i < m; i++) {
      int max1 = -1, max2 = -1;
      for(int j = 0; j < n; j++) {
        int t = evaluate(D, L[i], D[j]);
        if (t > max1) {max1 = t; max2 = j; }
      }
      ans[i] = D[max2];
    }
    printf("Case #%d:", cT+1);
    for(int i = 0; i < m; i++)
      printf(" %s", ans[i].c_str());
    puts("");
  
  }
  
  return 0;

}
