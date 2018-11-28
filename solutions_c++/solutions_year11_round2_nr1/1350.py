#include <iostream>
#include <algorithm>

#define MAX 120

using namespace std;

int T, N;
char mat[MAX][MAX];
double winCount[MAX], gameCount[MAX];
double WP[MAX];
double OWPscore[MAX];
double OWPcount[MAX];
double OWP[MAX];
double OOWPscore[MAX];
double OOWPcount[MAX];

void solve() {
  // fill wp
  for (int i = 0; i < N; i++) {
    WP[i] = (1.0*winCount[i])/gameCount[i];
  }
  
  // fill owp
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (mat[i][j] != '.') {
	double OWP = WP[j];
	// take out game against me
	OWP = OWP * gameCount[j] - 1*( mat[i][j] == '0' );
	OWP /= ( gameCount[j] - 1 );
	OWPscore[i] += OWP;
	OWPcount[i]++;
      }
    }
  }

  // fill oowp
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (mat[i][j] != '.') {
	double OOWP = OWPscore[j]/OWPcount[j];
	//OOWP = OOWP * gameCount[i] - ( mat[j][i] == '1' );
	//OOWP /= gameCount[i] - 1;
	OOWPscore[i] += OOWP;
	OOWPcount[i]++;
      }
    }
  }

  // fill rpi
  for (int i = 0; i < N; i++) {
    double score = 0.25 * WP[i] + 0.5 * OWPscore[i]/OWPcount[i] + 0.25 *  OOWPscore[i]/OOWPcount[i];
    cout << score << endl;
  }
}
  

int main() {
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> N;
    for (int i = 0; i < MAX; i++) {
      winCount[i] = 0;
      gameCount[i] = 0;
      OWPscore[i] = 0;
      OWPcount[i] = 0;
      OWP[i] = 0;
      OOWPscore[i] = 0;
      OOWPcount[i] = 0;
    }
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
	cin >> mat[j][k];
	if ( mat[j][k] == '1' )
	  winCount[j]++;
	if ( mat[j][k] != '.')
	  gameCount[j]++;
      }
    }
    printf("Case #%d:\n", t+1);
    solve();
  }    
  return 0;
}

