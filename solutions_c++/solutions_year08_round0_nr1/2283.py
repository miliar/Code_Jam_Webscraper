#include <iostream>
#include <map>

using namespace std;

int changes[2000][200];
//int prev[2000][200];

int solve(int P) {
  int s, q;
  if(scanf("%d%*c",&s) != 1) return 0;

  map<string, int> eng;
//  string revs[200];

  for(int i = 0; i < s; i++) {
    string e;
    getline(cin, e);
    eng[e] = i;
//    revs[i] = e;
  }

  memset(changes, 0, sizeof(changes));
//  memset(prev, 0, sizeof(prev));

  scanf("%d%*c",&q);

  for(int i = 1; i <= q; i++) {
    string e;
    getline(cin, e);
    int k = eng[e];
    int best = k==0?1:0;
    for(int j = 0; j < s; j++) {
      if(j == k) continue;
      if(changes[i-1][j] < changes[i-1][best]) best = j;
    }
    for(int j = 0; j < s; j++) {
      if(j == k) {
        changes[i][j] = changes[i-1][best] + 1;
//        prev[i][j] = best;
      } else {
        changes[i][j] = changes[i-1][j];
//        prev[i][j] = j;
      }
    }
  }

  int res = 1 << 30;
  int best = 0;

  for(int i = 0; i < s; i++) {
    if(changes[q][i] < res) {
      res = changes[q][i];
      best = i;
    }
  }

//  string t = "";

//  for(int i = q; i > 0; i--) {
//    t = revs[best] + t;
//    best = prev[i][best];
//  }


  printf("Case #%d: %d\n", P, res);

  return 1;
}

int main() {
  int n; cin >> n;
  for(int k=1;solve(k)&&k<n;k++);
}
