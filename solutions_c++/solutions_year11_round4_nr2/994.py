#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int w[500][500];
int xs[501][501];
int xc[501][501];
int ys[501][501];
int yc[501][501];

int main() {
  int T; fin >> T;
  for (int tid = 0; tid < T; ++tid) {
    int R; fin >> R;
    int C; fin >> C;
    int D; fin >> D;
    for (int i = 0; i < R; ++i) {
      string s; fin >> s;
      for (int j = 0; j < C; ++j) {
        w[i][j] = s[j] - '0';
        xs[i][j] = xc[i][j] = ys[i][j] = yc[i][j] = 0;
      }
    }
    memset(xs, 0, sizeof(xs));
    memset(ys, 0, sizeof(xs));
    memset(xc, 0, sizeof(xs));
    memset(yc, 0, sizeof(xs));
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        xs[i+1][j+1] = xs[i][j+1] + xs[i+1][j] - xs[i][j] + w[i][j];
        ys[i+1][j+1] = ys[i][j+1] + ys[i+1][j] - ys[i][j] + i;
        xc[i+1][j+1] = xc[i][j+1] + xc[i+1][j] - xc[i][j] + j * w[i][j];
        yc[i+1][j+1] = yc[i][j+1] + yc[i+1][j] - yc[i][j] + i * w[i][j];
        //cout << xs[i+1][j+1] << " ";
      }
      //cout << endl;
    }
    int K = 0;
    for (int i = 0; i < R; ++i) {
      for (int j = 0; j < C; ++j) {
        for (int ii = i; ii < R; ++ii) {
          for (int jj = j; jj < C; ++jj) {
            int xs_ = xs[ii + 1][jj + 1] - xs[ii + 1][j] - xs[i][jj + 1] + xs[i][j];
            xs_ -= w[ii][jj] + w[ii][j] + w[i][jj] + w[i][j];
            int xc_ = xc[ii + 1][jj + 1] - xc[ii + 1][j] - xc[i][jj + 1] + xc[i][j];
            xc_ -= w[ii][jj] *jj + w[ii][j]*j + w[i][jj]*jj + w[i][j]*j;
            int yc_ = yc[ii + 1][jj + 1] - yc[ii + 1][j] - yc[i][jj + 1] + yc[i][j];
            yc_ -= w[ii][jj] *ii + w[ii][j]*ii + w[i][jj]*i + w[i][j]*i;
            //cout << (i + ii) / 2.0 << " " << yc_ / (double)xs_ << " ";
            //cout << (j + jj) / 2.0 << " " << xc_ / (double)xs_ << endl;
            if ((i + ii) * xs_ == 2 * yc_ && (j + jj) * xs_ == 2 * xc_ ) {
              if (ii - i + 1 == jj - j + 1 && ii - i + 1 >= K) {
                //cout << ii - i + 1 << endl;
                K = ii - i + 1;
              }
            }
          }
        }
      }
    }
    if (K >= 3)
    fout << "Case #" << tid + 1<< ": " << K << endl;
    else
      fout << "Case #" << tid + 1<< ": " << "IMPOSSIBLE" << endl;
  }
}