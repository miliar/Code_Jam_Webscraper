#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

const int di[] = {-1, 0, 0, 1};
const int dj[] = {0, -1, 1, 0};

const int WIDTH = 256;
const int HEIGHT = 256;
const int AREA = HEIGHT * WIDTH;

int height, width;

int lev[HEIGHT][WIDTH];
int ind[HEIGHT][WIDTH];
int mark[AREA];
int next[AREA];

int basins;

int inside(int i, int j) {
  return i >= 0 && i < height &&
         j >= 0 && j < width;
}

int get_mark(int i) {
  if (mark[i] != '?') {
    return mark[i];
  }
  if (next[i] < 0) {
    mark[i] = basins++;
    return mark[i];
  }
  mark[i] = get_mark(next[i]);
  return mark[i];
}

int main() {
  ifstream input("test.in");
  ofstream output("test.out");

  int test_cases;
  input >> test_cases;
  for (int test_case = 1; test_case <= test_cases; test_case++) {

    input >> height >> width;
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        input >> lev[i][j];
      }
    }
   
    int index = 0;
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        ind[i][j] = index++;
      }
    }

    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        next[ind[i][j]] = -1;
        int low_lev = lev[i][j];
        for (int d = 0; d < 4; d++) {
          if (inside(i + di[d], j + dj[d])) {
            int next_i = i + di[d];
            int next_j = j + dj[d];
            if (lev[next_i][next_j] < low_lev) {
              low_lev = lev[next_i][next_j];
              next[ind[i][j]] = ind[next_i][next_j];
            }
          }
        }
      }
    }


    basins = 0;
    for (int i = 0; i < index; i++) {
      mark[i] = '?';
    }
    for (int i = 0; i < index; i++) {
      get_mark(i);
    }

    output << "Case #" << test_case << ":\n";
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        output << (char)(mark[ind[i][j]] + 'a');
        if (j + 1 < width) {
          output << ' ';
        }
      }
      output << endl;
    }
  }

  input.close();
  output.close();

  return 0;
}