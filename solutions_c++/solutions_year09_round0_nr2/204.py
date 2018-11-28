#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int H, W;

void floodfill(const VVI &A, VVI &L, const VVI &DI, const VVI &DJ, int i, int j, int k) {
  queue<pair<int,int> > Q;
  Q.push(make_pair(i,j));

  while (!Q.empty()) {
    pair<int,int> p = Q.front();
    Q.pop();
    int I = p.first;
    int J = p.second;

    if (L[I][J] != -1) continue;
    L[I][J] = k;
  
    for (int di = -1; di <= 1; di++) {
      for (int dj = -1; dj <= 1; dj++) {
	if (di != 0 && dj != 0) continue;
	if (di == 0 && dj == 0) continue;
	if (I+di < 0 || J+dj < 0 || I+di >= H || J+dj >= W) continue;
	
	if (DI[I+di][J+dj] == I && DJ[I+di][J+dj] == J) Q.push(make_pair(I+di,J+dj));
      }
    }
    if (DI[I][J] != 0 || DJ[I][J] != 0) {
      Q.push(make_pair(DI[I][J], DJ[I][J]));
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> H >> W;
    VVI A(H, VI(W));
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++)
	cin >> A[i][j];
    }

    VVI DI(H, VI(W, -1));
    VVI DJ(H, VI(W, -1));
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	int bi = i, bj = j;
	for (int di = -1; di <= 1; di++) {
	  for (int dj = -1; dj <= 1; dj++) {
	    if (di != 0 && dj != 0) continue;
	    if (di == 0 && dj == 0) continue;
	    if (i+di < 0 || j+dj < 0 || i+di >= H || j+dj >= W) continue;
	    if (A[i+di][j+dj] < A[bi][bj]) { bi = i+di; bj = j+dj; }
	  }
	}
	DI[i][j] = bi;
	DJ[i][j] = bj;
      }
    }

    VVI L(H, VI(W, -1));

    int k = 0;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	if (L[i][j] == -1) {
	  floodfill(A, L, DI, DJ, i, j, k++);
	}
      }
    }

    cout << "Case #" << t+1 << ":" << endl;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
	cout << (char)(L[i][j] + 'a') << ' ';
      }
      cout << endl;
    }
  }
}
