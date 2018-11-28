#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int alt[100][100];
char label[100][100];
char cur;
int H, W;

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

bool valid(int i, int j) {
  return 0 <= i && i < H && 0 <= j && j < W;
}

char search(int i, int j) {
  if (label[i][j]) return label[i][j];
  int lowest = alt[i][j];;
  int min_i = i, min_j = j;
  for (int k = 0; k < 4; k++) {
    int new_i = i+di[k], new_j = j+dj[k];
    if (valid(new_i, new_j) && alt[new_i][new_j] < lowest) {
      lowest = alt[new_i][new_j];
      min_i = new_i; min_j = new_j;
    }
  }
  if (lowest < alt[i][j])
    label[i][j] = search(min_i, min_j);
  else
    label[i][j] = cur++;
  return label[i][j];
}

int main(void)
{
  int T; cin >> T;

  for (int c = 1; c <= T; c++) {
    cin >> H >> W;
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++) {
	cin >> alt[i][j];
	label[i][j] = 0;
      }
    printf("Case #%d:\n", c);
    cur = 'a';
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++)
	cout << search(i, j) << ' ';
      cout << endl;
    }
  }
  return 0;
}
