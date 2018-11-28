#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream in("knight.in");
ofstream out("knight.out");

int N,R,H,W;

bool inbounds(int r, int c) {
  if (r >= 1 && r <= H && c >= 1 && c <= W) {
    return 1;
  }
  return 0;
}

int main() {
  in >> N;

  for (int casenum = 1; casenum <= N; casenum++) {
    in >> H >> W >> R;
    vector< vector<int> > v(H+1, vector<int>(W+1,0));
    vector< vector<bool> > rock(H+1, vector<bool>(W+1,0));
    v[1][1] = 1;
    for (int i = 0; i < R; i++) {
      int r,c;
      in >> r >> c;
      rock[r][c] = 1;
    }
    for (int r = 1; r <= H; r++) {
      for (int c = 1; c <= W; c++) {
	if (!rock[r][c]) {
	  if (inbounds(r+1,c+2)) {
	    v[r+1][c+2] += v[r][c];
	    v[r+1][c+2] %= 10007;
	  }
	  if (inbounds(r+2,c+1)) {
	    v[r+2][c+1] += v[r][c];
	    v[r+2][c+1] %= 10007;
	  }
	}
      }
    }
    out << "Case #" << casenum << ": " << v[H][W]%10007 << endl;
  }
  return 0;
}
