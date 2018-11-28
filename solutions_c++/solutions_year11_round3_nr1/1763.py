#include <iostream>

using namespace std;

const int dw[3] = { 0, 1, 1};
const int dh[3] = { 1, 1, 0};
const char rep[3] = { '\\', '/', '\\'};

int main() {
  int T; cin >> T;
  for (int test_case = 1; test_case <= T; ++test_case) {
    int H, W; cin >> H >> W;
    char pic[50][50];		// [w][h]
    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
	cin >> pic[j][i];
      }
    }

    bool impossible = false;
    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
	if (pic[j][i] == '#') {
	  pic[j][i] = '/';
	  for (int k = 0; k < 3; ++k) {
	    int nw = j + dw[k]; int nh = i + dh[k];
	    if (0<=nw && nw<W && 0<=nh && nh<H) {
	      if (pic[nw][nh] == '#') {
		pic[nw][nh] = rep[k];
	      } else {
		impossible = true;
	      }
	    } else {
	      impossible = true;
	    }
	  }
	}
      }
    }
    cout << "Case #" << test_case << ":" << endl;
    if (impossible) cout << "Impossible" << endl;
    else {
      for (int i = 0; i < H; ++i) {
	for (int j = 0; j < W; ++j) {
	  cout << pic[j][i];
	}
	cout << endl;
      }
    }
  }

  return 0;
}
