#include<iostream>
#include<cstring>
using namespace std;

int dy[] = {-1, 0, 0, 1};
int dx[] = {0, -1, 1, 0};
int ny, nx;
char ans[105][105];
int a[105][105];
char next;

char solve(int y, int x) {
  if (ans[y][x] > 0) return ans[y][x];
  int low, dir;

  low = a[0][0];
  for (dir = 0; dir < 4; dir++) {
    low <?= a[y+dy[dir]][x+dx[dir]];
  }
  for (dir = 0; dir < 4; dir++) {
    if (a[y+dy[dir]][x+dx[dir]] == low) break;
  }
  if (low < a[y][x]) {
    ans[y][x] = solve(y+dy[dir], x + dx[dir]);
  }
  else {
    ans[y][x] = next++;
  }
  return ans[y][x];
}

int main() {
  int cases, q, y, x;
  cin >> cases;
  for (q = 1; q <= cases; q++) {
    cin >> ny >> nx;
    memset(a, 1<<6, sizeof(a));
    for (y = 1; y <= ny; y++) {
      for (x = 1; x <= nx; x++) {
	cin >> a[y][x];
      }
    }
    memset(ans, 0, sizeof(ans));
    next = 'a';
    for (y = 1; y <= ny; y++) {
      for (x = 1; x <= nx; x++) {
	solve(y, x);
      }
    }
    printf("Case #%d:\n", q);
    for (y = 1; y <= ny; y++) {
      for (x = 1; x <= nx; x++) {
	if (x > 1) cout << ' ';
	cout << ans[y][x];
      }
      cout << endl;
    }
  }
}
