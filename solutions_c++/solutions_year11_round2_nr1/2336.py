#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)
       return a;
    else
       return gcd(b, a % b);
}

double WP(char table[][110], int n, int row, int &wins, int &total) {
  wins = 0; total = 0;
  for (int col = 0; col < n; col++) {
    if (table[row][col] != '.')
      total++;
    if (table[row][col] == '1') {
      wins++;
    }
  }
  return (double)wins/total;
}

double OWP(char table[][110], int n, int row) {
  double scr = 0.0; int tt = 0;
  for (int col = 0; col < n; col++) {
    if (table[row][col] == '0') {
      int wins, total;
      WP(table, n, col, wins, total);
      assert(total > 1);
      assert(wins >= 1);
      //cout << "row: " << col << " wins: " << wins << " total: " << total << endl;
      scr += ((double)(wins-1)/(total-1));
      tt++;
    } else if (table[row][col] == '1') {
      int wins, total;
      WP(table, n, col, wins, total);
      //cout << "row: " << col << " wins: " << wins << " total: " << total << endl;
      if (wins != 0) {
        assert(total > 1);
        assert(wins >= 0);
        scr += ((double)(wins)/(total-1));
        
      }
      tt++;
    }
    //cout << "scr: " << scr << endl;
  }
  
  //cout << "tt: " << tt << endl;
  return scr/tt;
}

double OOWP(char table[][110], int n, int row) {
  double total = 0.0;
  int opp = 0;
  for (int col = 0; col < n; col++) {
    if (table[row][col] != '.') {
      total += OWP(table, n, col);
      opp++;
    }
  }
  
  return total/opp;
}

int main() {
  freopen("data.txt", "r", stdin);
  freopen("outp1.txt", "w", stdout);
  cout << setprecision(10);
  long long T, n; char c; double wp, owp, oowp;
  char table[110][110];
  cin >> T;
  for (int p = 0; p < T; p++) {
    cin >> n;
    cin.get();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        table[i][j] = cin.get();
      }
      cin.get();
    }
    cout << "Case #" << p+1 << ": " << endl;
    for (int row = 0; row < n; row++) {
      int wins, total;
      wp = WP(table, n, row, wins, total);
      //cout << "WP of row " << row << " = " << wp << endl;
      owp = OWP(table, n, row);
      //cout << "OWP of row " << row << " = " << owp << endl;
      oowp = OOWP(table, n, row);
      //cout << "OOWP of row " << row << " = " << oowp << endl;
      double rate = 0.25*wp+0.5*owp+0.25*oowp;
      cout << rate << endl;
    }
  }
}