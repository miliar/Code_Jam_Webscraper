#include <iostream>

using namespace std;

int main() {
  char schedule[100][100];
  double WP[100];
  double WPP[100][100];
  double OWP[100];
  double OOWP[100];
  int T;
  cin >> T;
  double games;
  double won;
  for(int t=1; t<=T; t++) {
    int N;
    cin >> N;
    for(int i = 0; i < N; i++) {
      games = 0;
      won = 0;
      for(int j = 0; j < N; j++) {
	cin >> schedule[i][j];
	if(schedule[i][j] != '.') {
	  games += 1;
	  if(schedule[i][j] == '1') {
	    won += 1;
	  }
	}
      }
      WP[i] = won / games;
      for(int j = 0; j < N; j++) {
	if(schedule[i][j] != '.') {
	  if(schedule[i][j] == '1') {
	    WPP[i][j] = (won - 1) / (games - 1);
	  } else {
	    WPP[i][j] = won / (games - 1);
	  }
	} else {
	  WPP[i][j] = WP[i];
	}
      }
    }
    double sum, count;
    for(int i = 0; i < N; i++) {
      sum = 0;
      count = 0;
      for(int j = 0; j < N; j++) {
	if(schedule[i][j] != '.') {
	  count += 1;
	  sum += WPP[j][i];
	}
      }
      OWP[i] = sum / count;
    }

    for(int i = 0; i < N; i++) {
      sum = 0;
      count = 0;
      for(int j = 0; j < N; j++) {
	if(schedule[i][j] != '.') {
	  count += 1;
	  sum += OWP[j];
	}
      }
      OOWP[i] = sum / count;
    }
    cout << "Case #" << t << ":" << endl;
    for(int i = 0; i < N; i++) {
      cout << (0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]) << endl;
    }
  }
}
