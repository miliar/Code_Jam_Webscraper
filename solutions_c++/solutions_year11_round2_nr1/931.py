#include <map>
#include <iostream>
#include <iomanip>

using namespace std;

enum outcome {win, lose, none};

void doit () {
  int n;

  cin >> n;
  outcome outcomes [n][n];
  for(int i = 0; i < n; ++i) {
    for(int j= 0; j < n; ++j) {
      char c;
      cin >> c;
      if( c == '.') {
        outcomes[i][j] = none;
      } else if ( c == '1' ) {
        outcomes[i][j] = win;
      } else if ( c == '0') {
        outcomes[i][j] = lose;
      }
    }
  }

  int games_played[n];
  int games_won[n];
  float wp[n];
  float owp[n];
  float oowp[n];
  for(int i = 0; i < n; ++i) {
    games_played[i] = 0;
    games_won[i] = 0;
    for(int j = 0; j < n; ++j) {
      if (outcomes[i][j] != none) {
        games_played[i]++;
      }
      if (outcomes[i][j] == win) {
        games_won[i]++;
      }
    }
    wp[i] = ((float)games_won[i]) / ((float)games_played[i]);
  }

  for(int i = 0; i < n; ++i) {
    float total = 0;
    for(int j = 0; j < n; ++j) {
      if (outcomes[i][j] != none) {
        int won_against_not_i = games_won[j];
        if(outcomes[j][i] == win) {
          won_against_not_i--;
        }
        total += ((float)won_against_not_i) / ((float)(games_played[j] - 1));
      }
    }
    owp[i] = total / (float)games_played[i];
  }

  for (int i = 0; i < n; ++i) {
    float total = 0;
    for(int j = 0; j < n; ++j) {
      if (outcomes[i][j] != none) {
        total += owp[j];
      }
    }
    oowp[i] = total / ((float)games_played[i]);
    cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
  }
}

int main () {
  int t;
  cin >> t;
  cout << setprecision(10);
  for(int i = 0; i < t; ++i) {
    cout << "Case #:" << (i+1) << endl;
    doit();
  }

  return 0;
}
