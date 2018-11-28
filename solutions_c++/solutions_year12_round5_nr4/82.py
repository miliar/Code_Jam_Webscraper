#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>

#define MAX_N 1005
#define MAX_CHAR 256
#define PA pair<char, char>
#define PA2 pair<double, int>

using namespace std;

int tests;
int n,minn,k;
int answer;
int p[MAX_N];
int cnt[MAX_CHAR],ens;
bool is[MAX_N * MAX_N];
char substr[MAX_N * MAX_N][2];
int w[MAX_N * MAX_N];
char in[MAX_N];
bool ad[MAX_CHAR][MAX_CHAR];
int indeg[MAX_N * MAX_N],outdeg[MAX_N * MAX_N];
vector<int> V[MAX_N * MAX_N];
set<PA > S;
set<PA >::iterator it;
queue<int> Q;

inline bool special(char c) {
  return (c == 'o' or c == 'i' or c == 'e' or c == 'a' or c == 's'
    or c == 't' or c == 'b' or c == 'g');
}

inline char cha(char c) {
  if (c == 'o') return '0';
  if (c == 'i') return '1';
  if (c == 'e') return '2';
  if (c == 'a') return '3';
  if (c == 's') return '4';
  if (c == 't') return '5';
  if (c == 'b') return '6';
  if (c == 'g') return '8';
  return 0;
}

inline void getInput() {
  scanf("%d", &k);
  scanf("%s", in);
  return ;
}

inline int abso(int tmpx) {
  return tmpx > 0 ? tmpx : -tmpx;
}

inline void solve() {
  n = strlen(in);
  for (int i = 0 ; i < MAX_CHAR ; i ++) cnt[i] = 0;
  for (int i = 0 ; i < n - 1 ; i ++) cnt[in[i]] ++;
  S.clear();
  for (int i = 0 ; i < n - 1 ; i ++) {
    S.insert(PA(in[i], in[i + 1]));
  }
  ens = 0;
  for (it = S.begin() ; it != S.end() ; it ++) {
    if (!special(it->first) and !special(it->second)) {
      substr[ens][0] = it->first;
      substr[ens][1] = it->second;
      ens ++;
    } else if (!special(it->first)) {
      substr[ens][0] = it->first;
      substr[ens][1] = it->second;
      ens ++;
      substr[ens][0] = it->first;
      substr[ens][1] = cha(it->second);
      ens ++;
    } else if (!special(it->second)) {
      substr[ens][0] = it->first;
      substr[ens][1] = it->second;
      ens ++;
      substr[ens][0] = cha(it->first);
      substr[ens][1] = it->second;
      ens ++;
    } else {
      substr[ens][0] = it->first;
      substr[ens][1] = it->second;
      ens ++;
      substr[ens][0] = it->first;
      substr[ens][1] = cha(it->second);
      ens ++;
      substr[ens][0] = cha(it->first);
      substr[ens][1] = it->second;
      ens ++;
      substr[ens][0] = cha(it->first);
      substr[ens][1] = cha(it->second);
      ens ++;
    }
  }
  for (int i = 0 ; i < MAX_CHAR ; i ++) {
    indeg[i] = 0;
    outdeg[i] = 0;
    p[i] = -1;
    is[i] = false;
    V[i].clear();
    indeg[i] = 0;
    for (int j = 0 ; j < MAX_CHAR ; j ++) ad[i][j] = false;
  }
  answer = ens + 1;
  for (int i = 0 ; i < ens ; i ++) {
    indeg[substr[i][1]] ++;
    outdeg[substr[i][0]] ++;
    ad[substr[i][0]][substr[i][1]] = true;
    V[substr[i][1]].push_back(substr[i][0]);
  }
  int tmp = 0;
  for (int i = 0 ; i < MAX_CHAR ; i ++) {
    tmp += abso(outdeg[i] - indeg[i]);
  }
  answer += max(tmp / 2 - 1, 0);
  /*
  for (int i = 0 ; i < MAX_CHAR ; i ++) {
    if (!is[i]) {
      is[i] = true;
      int tmp = 0;
      Q.push(i);
      while (!Q.empty()) {
        for (int j = 0 ; j < MAX_CHAR )
      }
      answer += max(tmp / 2, 1);
    }
  }
  */
  /*
  for (int i = 0 ; i < ens ; i ++) {
    for (int j = 0 ; j < ens ; j ++) {
      if (i != j and substr[i][1] == substr[j][0]) {
        indeg[j] ++;
        V[i].push_back(j);
      }
    }
  }
  for (int i = 0 ; i < ens ; i ++) {
    if (indeg[i] == 0) Q.push(i);
  }
  printf("XX %d\n", ens);
  for (int i = 0 ; i < ens ; i ++) {
    printf("YY %d\n", (int) V[i].size());
  }
  if (Q.empty()) {
    for (int i = 0 ; i < ens ; i ++) {
      if (!is[i]) {
        is[i] = true;
        Q.push(i);
        break;
      }
    }
  }
  answer = 0;
  while (!Q.empty()) {
    int ver = Q.front();
    printf("QUEUE %d : %d : %c %c\n", ver, p[ver], substr[ver][0], substr[ver][1]);
    Q.pop();
    is[ver] = true;
    if (p[ver] == -1) answer += 2;
    else answer ++;
    for (int i = 0 ; i < V[ver].size() ; i ++) {
      if (!is[V[ver][i]]) {
        is[V[ver][i]] = true;
        p[V[ver][i]] = ver;
        Q.push(V[ver][i]);
        break;
      }
    }
    if (Q.empty()) {
      for (int i = 0 ; i < ens ; i ++) {
        if (!is[i]) {
          is[i] = true;
          Q.push(i);
          break;
        }
      }
    }
  }
  */
  printf(" %d", answer);
  return ;
}

int main() {
  scanf("%d", &tests);
  for (int test = 1 ; test <= tests ; test ++) {
    getInput();
    printf("Case #%d:", test);
    solve();
    printf("\n");
  }
  return 0;
}