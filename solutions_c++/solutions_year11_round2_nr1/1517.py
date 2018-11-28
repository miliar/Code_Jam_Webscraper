#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long



int main() {
  // Declare members
  uint32_t num_case;
  cin >> num_case;

  uint32_t num_team;
  vector<double> wp;
  vector<double> owp;
  vector<double> oowp;
  vector<int> num_games;
  vector<int> num_won;

  string line;

  for (int j = 1; j <= num_case; j++) {
    // Init members
    wp.clear();
    owp.clear();
    oowp.clear();
    num_games.clear();
    num_won.clear();
    cin >> num_team;
    
    int games[num_team][num_team];

    wp.resize(num_team, 0);
    owp.resize(num_team, 0);
    oowp.resize(num_team, 0);
    num_games.resize(num_team, 0);
    num_won.resize(num_team, 0);
    for (int i = 0; i < num_team; i++) {
      cin >> line;
      for (int k = 0; k < num_team; k++) {
	if (line[k] == '1') {
	  games[i][k]=1;
	  num_games[i]++;
	  num_won[i]++;
	} else if ( line[k] == '0'){
	  num_games[i]++;
	  games[i][k]=-1;
	} else {
	  games[i][k]=0;
	}
      }
      wp[i] = (num_won[i]==0)?0:(double)num_won[i]/num_games[i];
    }

    for (int i = 0; i < num_team; ++i) {
      double avg = 0;
      int g = 0;
      for (int k = 0; k < num_team; ++k) {
	if (i == k) continue;

	if (games[k][i] == 1) {
	  avg += (num_won[k] == 1)?0:(double)(num_won[k]-1)/(num_games[k]-1);
	  g++;
	} else if (games[k][i] == 0) {
	  //avg += wp[k];
	} else {
	  avg += (double)num_won[k]/(num_games[k]-1);
	  g++;
	}
      }
      if (g != 0) owp[i] = avg/g;
    }

    // Print output for case j
    cout << "Case #" << j << ":" << endl;

    for (int i = 0; i < num_team; i++) {
      double avg = 0;
      int g = 0;
      for (int k = 0; k < num_team; k++) {
	if (i == k || games[i][k] == 0) continue;

	avg += owp[k];
	g++;
      }
      if (g != 0) avg /= g;
      cout << 0.25*wp[i] + 0.5*owp[i] + 0.25*avg << endl;
    }

  }


  return 0;
}
