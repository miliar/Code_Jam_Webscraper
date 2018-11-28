#include <cstdio>
#include <algorithm>

using namespace std;

int n, K;
char board[55][55];
char rot[55][55];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  
  int cs;
  scanf("%d", &cs);
  for (int r = 1; r <= cs; ++r) {
    scanf("%d %d", &n, &K);
    for (int i = 0; i < n; ++i)
      scanf("%s", board[i]);
    
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        rot[i][j] = board[n - j - 1][i];
        
    for (int i = n - 2; i >= 0; --i)
      for (int j = 0; j < n; ++j) {
        if (rot[i][j] == '.') continue;
        int k = i;
        while (k + 1 < n && rot[k + 1][j] == '.') {
          swap(rot[k][j], rot[k + 1][j]);
          k++;
        }
      }

    int arr[2] = {0};
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        if (rot[i][j] == '.') continue;
        int flag = (rot[i][j] == 'R') ? 0 : 1;
        int y = i, x = j;
        int cnt = 0;
        while (x < n && rot[i][j] == rot[y][x]){ cnt++; x++; }
        if (cnt >= K) arr[flag] = 1;
        
        y = i, x = j, cnt = 0;
        while (y < n && rot[i][j] == rot[y][x]){ cnt++; y++; }
        if (cnt >= K) arr[flag] = 1;
        
        y = i, x = j, cnt = 0;
        while (y < n && x < n && rot[i][j] == rot[y][x]) { cnt++; x++; y++; }
        if (cnt >= K) arr[flag] = 1;
        
        y = i, x = j, cnt = 0;
        while (y < n && x >= 0 && rot[i][j] == rot[y][x]) { cnt++; x--; y++; }
        if (cnt >= K) arr[flag] = 1;
      }
      printf("Case #%d: ", r);
      if (arr[0] + arr[1] == 0) printf("Neither\n");
      else if (arr[0] + arr[1] == 2) printf("Both\n");
      else if (arr[0]) printf("Red\n");
      else printf("Blue\n");
  }
  return 0;
}