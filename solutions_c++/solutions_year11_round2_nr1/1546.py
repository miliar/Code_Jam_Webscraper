#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <list>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <tr1/unordered_map>
using namespace std;
using namespace std::tr1;

int main() {
  int ncases;
  scanf("%d\n", &ncases);
  for (int j = 0; j < ncases; ++j) {
    printf("Case #%d:\n", j + 1);
    int n_teams;
    scanf("%d\n", &n_teams);
    unordered_map<int, unordered_map<int, int> > scores;
    unordered_map<int, int>::iterator it;
    vector<int> wins(n_teams, 0);
    vector<int> n_games(n_teams, 0);
    vector<double> WP(n_teams, 0);
    vector<double> OWP(n_teams, 0);
    vector<double> OOWP(n_teams, 0);
    char oi[150];

    for (int i = 0; i < n_teams; ++i) {
      scanf("%s\n", oi);
      for (int k = 0; k < n_teams; ++k) {
        if (k == i) continue;
        switch(oi[k]) {
          case '.':
          break;
          case '0':
            n_games[i]++;
            scores[i][k] = 0;
          break;
          case '1':
            wins[i]++;
            n_games[i]++;
            scores[i][k] = 1;
          break;
        }
      }
      WP[i] = (double) wins[i]/n_games[i];
      //cout << "WINS: "<<n_games[i]<<endl;
      //cout << "WP["<<i<<"] = "<<WP[i]<<endl;
    }
    //OWP
    for (int i = 0; i < n_teams; ++i) {
      double avg_owp = 0;
      int number = 0;
      double owp;
      for (it = scores[i].begin(); it != scores[i].end(); ++it) {
        if (it->second == 0) {
          owp = ((double)wins[it->first] - 1)/ (n_games[it->first]-1);
        }
        else {
          owp = ((double)wins[it->first]/(n_games[it->first] - 1));
        }
        avg_owp+= owp;
        number++;
      }
      OWP[i] = avg_owp / number;
      //cout << "OWP["<<i<<"] = "<<OWP[i]<<endl;
    }
  //OOWP
    for (int i = 0; i < n_teams; ++i) {
      double avg_owp = 0;
      int number = 0;
      double owp;
      for (it = scores[i].begin(); it != scores[i].end(); ++it) {
        avg_owp+= OWP[it->first];
        number++;
      }
      OOWP[i] = avg_owp / number;
      //cout << "OOWP["<<i<<"] = "<<OOWP[i]<<endl;
    }
    for (int i = 0; i < n_teams; ++i) {
      printf("%.9lf\n", 0.25 * WP[i] + .5*OWP[i] + 0.25*OOWP[i]);
    }
  }
}
