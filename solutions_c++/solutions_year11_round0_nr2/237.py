#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <time.h>
#include <cmath>
#include <cassert>
using namespace std;

typedef long long ll;

char spec[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
char st[2000];
vector<string> comb;
vector<string> opp;
int cnt[8];

int get_spec(char c) {
  for(int i = 0; i < 8; i++) {
    if(spec[i] == c) return i;
  }
  return -1;
}

bool good_comb(string & s, char a, char b) {
  if(s[0] == a && s[1] == b) return true; swap(a, b);
  if(s[0] == a && s[1] == b) return true;
  return false;
}

bool good_opp(string & s, char a) {
  if(s[0] == a && cnt[get_spec(s[1])] > 0) return true;
  if(s[1] == a && cnt[get_spec(s[0])] > 0) return true;
  return false;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tests; scanf("%d", &tests);
  for(int tt = 1; tt <= tests; tt++) {
    printf("Case #%d: ", tt);
    comb.clear(); opp.clear();
    memset(cnt, 0, sizeof cnt);
    int n;
    for(scanf("%d", &n); n--;) {
      string s; cin >> s;
      comb.push_back(s);
    }
    for(scanf("%d", &n); n--;) {
      string s; cin >> s;
      opp.push_back(s);
    }
    st[0] = 0;
    scanf("%d", &n); string s; cin >> s;
    for(int i = 0; i < n; i++) {
      int u = get_spec(s[i]); 
      if(st[0] == 0 || u == -1) {
	if(u != -1) cnt[u]++;
	st[++st[0]] = s[i];
	continue;
      }
      bool ok = false;
      for(int j = 0; j < (int)comb.size(); j++) {
	if(good_comb(comb[j], s[i], st[st[0]])) {
	  cnt[get_spec(st[st[0]])]--;
	  st[st[0]] = comb[j][2];
	  u = get_spec(comb[j][2]);
	  if(u != -1) cnt[u]++;
	  ok = true;
	  break;
	} 
      }
      if(ok) continue;
      for(int j = 0; j < (int)opp.size(); j++) {
	if(good_opp(opp[j], s[i])) {
	  st[0] = 0;
	  memset(cnt, 0, sizeof cnt);
	  ok = true;
	  break;
	} 
      }
      if(ok) continue;
      u = get_spec(s[i]);
      cnt[u]++; st[++st[0]] = s[i];
    }
    printf("[");
    if(st[0]) {
      for(int j = 1; j < st[0]; j++) {
	printf("%c, ", st[j]);
      }
      printf("%c", st[st[0]]);
    }
    printf("]\n");
  }

}
