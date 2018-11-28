#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <queue>
#include <cstring>

using namespace std;

bool vis[1000];
int X1[1000];
int Y1[1000];
int X2[1000];
int Y2[1000];

bool cross(int a, int b) {
  if((X1[a] <= X2[b] && X2[b] <= X2[a] ||
     X1[a] <= X1[b] && X1[b] <= X2[a] ||
     X1[b] < X1[a] && X2[a] < X2[b]) &&
    (Y1[a] <= Y2[b] && Y2[b] <= Y2[a] ||
     Y1[a] <= Y1[b] && Y1[b] <= Y2[a] ||
     Y1[b] < Y1[a] && Y2[a] < Y2[b])) {
    if(X2[b] == X1[a] && Y2[b] == Y1[a]) return false;
    if(X2[a] == X1[b] && Y2[a] == Y1[b]) return false;
    return true;
  }
  return false;
}

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int R; cin >> R;
    
    memset(vis, 0, sizeof(vis));
    for(int i = 0; i < R; i++) {
      cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
      X2[i]++; Y2[i]++;
    }

    int result = 0;
    for(int i = 0; i < R; i++) {
      if(vis[i]) continue;
      vector<int> v;
      queue<int> q;
      q.push(i);
      vis[i] = true;
      while(!q.empty()) {
        int x = q.front(); q.pop();
        v.push_back(x);
        for(int j = 0; j < R; j++) {
          if(!cross(x, j) || vis[j]) continue;
          q.push(j);
          vis[j] = true;
        }
      }
      int maxx = X1[i];
      int maxy = Y1[i];
      int minrow = X1[i] + Y1[i];
      for(int i = 0; i < v.size(); i++) {
        minrow = min(minrow, X1[v[i]] + Y1[v[i]]);
        maxx = max(maxx, X2[v[i]] - 1);
        maxy = max(maxy, Y2[v[i]] - 1);
      }
      result = max(result, maxx + maxy - minrow + 1);
    }

    cout << "Case #" << t << ": " << result << endl;
  }
}
