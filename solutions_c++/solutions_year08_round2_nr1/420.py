#include <fstream>
#include <iostream>

using namespace std;

long long A, B, C, D;
long long X, Y;
long long x0, y0;
long long M;

int n;

#define MAX 100008

int x[100008];
int y[100008];

long long cool1down[MAX][3][3];
long long cool2down[MAX][3][3];

int main()
{
  ifstream input("a.in");
  ofstream output("a.out");
  int test, tests;
  input >> tests;
  for (test = 0; test < tests; ++test) {
    input >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    X = x0;
    Y = y0;
    x[0] = x0;
    y[0] = y0;
    for (int i = 1; i < n; ++i) {
      x[i] = (A * X + B) % M;
      y[i] = (C * Y + D) % M;
      X = x[i];
      Y = y[i];
    }
    memset(cool1down, 0, sizeof(cool1down));
    memset(cool2down, 0, sizeof(cool2down));
    for (int i = 1; i < n; ++i) {
      cool1down[i][x[i - 1] % 3][y[i - 1] % 3] = 1;
      for (int j = 0; j < 3; ++j) {
	for (int k = 0; k < 3; ++k) {
	  cool1down[i][j][k] += cool1down[i - 1][j][k];
	}
      }
    }
    for (int i = 1; i < n; ++i) {
      for (int j = 0; j < 3; ++j) {
	for (int k = 0; k < 3; ++k) {
	  cool2down[i][(x[i - 1] + j) % 3][(y[i - 1] + k) % 3] = cool1down[i - 1][j][k];
	}
      }
      for (int j = 0; j < 3; ++j) {
	for (int k = 0; k < 3; ++k) {
	  cool2down[i][j][k] += cool2down[i - 1][j][k];
	}
      }
    }
    long long result = 0;
    for (int i = 0; i < n; ++i) {
      int j = x[i] % 3, k = y[i] % 3;
      j = (3 - j) % 3;
      k = (3 - k) % 3;
      result += cool2down[i][j][k];
    }
    /*    long long result0 = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
	for (int k = j + 1; k < n; ++k) {
	  result0 += ((x[i] + x[j] + x[k]) % 3 == 0) && ((y[i] + y[j] + y[k]) % 3 == 0);
	}
      }
      }*/
    output << "Case #" << test + 1 << ": " << result << endl;
  }
}
