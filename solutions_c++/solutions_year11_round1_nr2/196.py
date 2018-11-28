#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <stdio.h>
#include <set>
#include <assert.h>
using namespace std;
int has[100][300];
char agree[100][100][1024], maximal[100][1024];
int main() {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    int n, m;
    string s;
    cin >> n >> m;
    vector<string> D, L;
    for (int i = 0; i < n; ++i) {
      cin >> s;
      D.push_back(s);
    }
    for (int i = 0; i < m; ++i) {
      cin >> s;
      L.push_back(s);
    }
    memset(has, 0, sizeof(has));
    memset(agree, 0, sizeof(agree));
    memset(maximal, 1, sizeof(maximal));
    for (int i = 0; i < n; ++i)
      for (int mask = 0; mask < 1<<D[i].size(); ++mask)
	for(int j1 = 0; j1 < D[i].size(); ++j1)
	  for (int j2 = j1+1; j2 < D[i].size(); ++j2) 
	    if (((!!(mask&(1<<j1))) != (!!(mask&(1<<j2)))) &&
		D[i][j1] == D[i][j2])
	      maximal[i][mask] = 0;
  for (int i = 0; i < n; ++i)
      for (int j = 0; j < D[i].size(); ++j)
	has[i][D[i][j]] = 1;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
	if (D[i].size() == D[j].size())
	  for (int mask = 0; mask < 1<<D[i].size(); ++mask) {
	    bool bad = false;
	    for (int r = 0; r < D[i].size(); ++r)
	      if ((mask&(1<<r)) && D[i][r] != D[j][r]) {
		bad = true;
		break;
	      }
	    if (!bad)
	      agree[i][j][mask] = 1;
	  }
    printf("Case #%d:", rr);
    for (int q = 0; q < m; ++q) {
      int best = -1;
      string ans = "";
      for (int i = 0; i < n; ++i) {
	char bad[100];
	memset(bad, 0, sizeof(bad));
	int score = 0, mask = 0;
	for (int at = 0; at < 26; ++at) {
	  char guess = 0;
	  for (int t = 0; t < n; ++t)
	    if (!bad[t] && maximal[t][mask] && agree[i][t][mask] && has[t][L[q][at]]) {
	      guess = 1;
	      break;
	    }
	  if (guess)
	    if (!has[i][L[q][at]]) {
	      score++;
	      for (int t = 0; t < n; ++t)
		if (has[t][L[q][at]])
		  bad[t] = 1;
	    }
	    else
	      for (int r = 0; r < D[i].size(); ++r)
		if (D[i][r] == L[q][at])
		  mask |= 1<<r;
	}
	if (score > best) 
	  best = score, ans = D[i];
      }
      printf(" %s", ans.c_str());
    }
    printf("\n");
  }
  return 0;
}
