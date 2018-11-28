#include <iostream>
#include <cstring>
#include <map>

using namespace std;

int H, W;
int m[105][105];
int p[105][105];
int r[105][105];
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};
map<int, char> mapping;


int findSink(int x) {
  int r = x / W;
  int c = x % W;

  if (p[r][c] != x) {
    p[r][c] = findSink(p[r][c]);
  } 

  return p[r][c];
}

void solve() {
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      int min = m[i][j];
      p[i][j] = W * i + j;
      
      for(int k = 0; k < 4; k++) {
	int r = dr[k] + i;
	int c = dc[k] + j;

	if (r >= 0 && r < H && c >= 0 && c < W) {
	    if (m[r][c] < min) {
	      min = m[r][c];
	      p[i][j] = W * r + c;
	    }
	}
      }
    }
  }

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	p[i][j] = findSink(p[i][j]);
      }
    }    
}

int main() {
  int n, t = 1, c;

  cin >> n;

  while(n) {
    cin >> H >> W;
    c = 0;
    mapping.clear();

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	cin >> m[i][j];
      }
    }

    solve();

    cout << "Case #" << t++ << ":\n";
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	if (mapping[p[i][j]] == 0) {
	  mapping[p[i][j]] = c + 'a';
	  c++;
	}
	cout << mapping[p[i][j]] << " ";
      }      
      cout << endl;
    }
    n--;
  }

  return EXIT_SUCCESS;
}
