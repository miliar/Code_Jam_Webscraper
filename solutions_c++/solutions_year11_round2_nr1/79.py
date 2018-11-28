#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

const int MAX_N = 105;
int n;

char grid[MAX_N][MAX_N];
double nGames[MAX_N];
double nWins[MAX_N];
double wp[MAX_N];
double owp[MAX_N];
double oowp[MAX_N];
double rpi[MAX_N];

void printGrid() {
  for (int y = 0; y < n; y++) {
    for (int x = 0; x < n; x++) {
      printf("%c", grid[y][x]);
    }
    printf("  %g  %g\n", nGames[y], nWins[y]);
  }
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d", &n);
    for (int y = 0; y < n; y++) {
      nGames[y] = 0;
      nWins[y] = 0;
      for (int x = 0; x < n; x++) {
        char c;
        scanf(" %c", &c);
        grid[y][x] = c;
        if (c != '.') nGames[y]++;
        if (c == '1') nWins[y]++;
      }
      assert(nGames[y] > 0);
      wp[y] = nWins[y] / nGames[y];
    }
    for (int i = 0; i < n; i++) {
      double sumWP = 0;
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '.') continue;
        double nWins2 = nWins[j] - (grid[j][i] == '1');
        double wp2 = nWins2 / (nGames[j] - 1);
        //cout << "i=" << i << " j=" << j << " wp2=" << wp2 << endl;
        sumWP += wp2;
      }
      owp[i] = sumWP / nGames[i];
      //cout << "owp_" << i << "=" << owp[i] << endl;
    }
    for (int i = 0; i < n; i++) {
      double sumOWP = 0;
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '.') continue;
        sumOWP += owp[j];
      }
      oowp[i] = sumOWP / nGames[i];
      //cout << "oowp_" << i << "=" << oowp[i] << endl;
      rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
    }
    printf("Case #%i:\n", iCase);
    for (int i = 0; i < n; i++) {
      printf("%.12f\n", rpi[i]);
    }
    //printGrid();
  }
  return 0;
}
