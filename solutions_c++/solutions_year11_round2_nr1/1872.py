#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>

using namespace std;

int main(void) {
  int T;
  string scores[100];
  double wp[100];
  double owp[100][100];
  double ave_owp[100];
  int total_games[100];
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N;
    cin >> N;
    memset(total_games, 0, sizeof(total_games));
    
    for (int n = 0; n < N; n++)
      cin >> scores[n];
    for (int i = 0; i < N; i++) {
      int total_wins = 0;
      for (int j = 0; j < N; j++) {
        if (scores[i][j] != '.') {
          total_games[i]++;
          if (scores[i][j] == '1')
            total_wins ++;
        }
      }
      for (int j = 0; j < N; j++) {
        if (scores[i][j] == '0')
          owp[i][j] = total_wins * 1.0 / (total_games[i] - 1);
        else if (scores[i][j] == '1')
          owp[i][j] = (total_wins - 1) * 1.0 / (total_games[i] - 1); 
      }
      wp[i] = total_wins * 1.0 / total_games[i];
      //cout << wp[i] << endl;
    }
    for (int i = 0; i < N; i++) {
      double owp_sum = 0;
      for (int j = 0; j < N; j++) {
        if (scores[i][j] != '.')
          owp_sum += owp[j][i];
      }
      ave_owp[i] = owp_sum / total_games[i];
      //cout << ave_owp[i] << endl;
    }
    cout << "Case #" << t + 1 << ":" << endl;
    for (int n = 0; n < N; n++) {
      double rpi = 0.25 * wp[n] + 0.5 * ave_owp[n];
      double oowp = 0;
      for (int i = 0; i < N; i++) {
        if (scores[n][i] != '.')
          oowp += ave_owp[i];
      }
      rpi += 0.25 * oowp / total_games[n];
      printf("%.12f\n", rpi);
    }
  }  
  
  return 0;
}
