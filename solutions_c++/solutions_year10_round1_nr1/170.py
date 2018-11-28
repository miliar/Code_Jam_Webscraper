#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;

int N, K, a[55][55];

void rotate() {
  int y, x1, x2;
  for (y = 0; y < N; y++) {
    for (x1 = N-1; x1 >= 0; x1--) {
      if (a[y][x1]) continue;
      for (x2 = x1-1; x2 >= 0; x2--) {
	if (a[y][x2]) {
	  swap(a[y][x1], a[y][x2]);
	  break;
	}
      }
      if (x2 < 0) break;
    }
  }
}

int dy[] = {1, 1, 0, -1};
int dx[] = {0, 1, 1, 1};
int count_winning() {
  int ret = 0, y, x, z;
  for (y = 0; y < N; y++) {
    for (x = 0; x < N; x++) {
      if (! a[y][x]) continue;
      for (int dir = 0; dir < 4; dir++) {
	for (z = 1; z < K; z++) {
	  int y2 = y + dy[dir] * z;
	  int x2 = x + dx[dir] * z;
	  if (y2 < 0 || x2 < 0 || y2 >= N || x2 >= N || a[y][x] != a[y2][x2]) break;
	}
	if (z == K) { // it's winning
	  if (a[y][x] == 1) ret |= 1;
	  else ret |= 2;
	}
      }
    }
  }
  return ret;
}

void draw() {
  for (int y = 0; y < N; y++) {
    for (int x = 0; x < N; x++) {
      cout << a[y][x];
    }
    cout << endl;
  }
}

int main() {
  int cases;
  char c;

  cin >> cases;
  for (int q = 1; q <= cases; q++) {
    cin >> N >> K;
    for (int y = 0; y < N; y++) {
      for (int x = 0; x < N; x++) {
	cin >> c;
	if (c == '.') a[y][x] = 0;
	else if (c == 'R') a[y][x] = 1;
	else a[y][x] = 2;
      }
    }
    rotate();
    int ans = count_winning();
    printf("Case #%d: ", q);
    if (ans == 1) cout << "Red\n";
    else if (ans == 2) cout << "Blue\n";
    else if (ans == 0) cout << "Neither\n";
    else if (ans == 3) cout << "Both\n";
  }
  return 0;
}
