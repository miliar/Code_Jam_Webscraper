

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {

  ifstream in("input");
  ofstream out("output");

  int T;
  in >> T;
  for(int i = 0; i < T; i++){

    int numb_of_teams;
    in >> numb_of_teams;

    vector<string> schedule(numb_of_teams);
    vector<double> team_WP(numb_of_teams), team_OWP(numb_of_teams), team_OOWP(numb_of_teams);

    vector<vector<double> > team_WP_without_team;
    team_WP_without_team.resize(numb_of_teams);
    for(int i = 0; i < numb_of_teams; i++){
      team_WP_without_team[i].resize(numb_of_teams,0);
    }

    for(int i = 0; i < numb_of_teams; i++){
      // read team results
      in >> schedule[i];

      // count wins and games
      int numb_of_games = 0;
      int numb_of_wins = 0;
      for(int j = 0; j < numb_of_teams; j++){
        switch(schedule[i][j]){
          case '.':
            break;
          case '1':
            numb_of_games++;
            numb_of_wins++;
            break;
          case '0':
            numb_of_games++;
            break;
        }
      }

      // team_WP
      team_WP[i] = double(numb_of_wins)/numb_of_games;

      // team_WP_without_team
      for(int j = 0; j < numb_of_teams; j++){
        switch(schedule[i][j]){
          case '.':
            team_WP_without_team[i][j] = team_WP[i];
            break;
          case '0':
            team_WP_without_team[i][j] = double(numb_of_wins)/(numb_of_games-1);
            break;
          case '1':
            team_WP_without_team[i][j] = double(numb_of_wins-1)/(numb_of_games-1);
        }
      }
    }

    // team_OWP
    for(int i = 0; i < numb_of_teams; i++){
      double sum_of_WP_opponents = 0;
      int numb_of_opponents = 0;
      for(int j = 0; j < numb_of_teams; j++){
        if(schedule[i][j] != '.'){
          sum_of_WP_opponents += team_WP_without_team[j][i];
          numb_of_opponents++;
        }
      }
      team_OWP[i] = sum_of_WP_opponents/numb_of_opponents;
    }

    // team_OOWP
    for(int i = 0; i < numb_of_teams; i++){
      double sum_of_OWP_opponents = 0;
      int numb_of_opponents = 0;
      for(int j = 0; j < numb_of_teams; j++){
        if(schedule[i][j] != '.'){
          sum_of_OWP_opponents += team_OWP[j];
          numb_of_opponents++;
        }
      }
      team_OOWP[i] = sum_of_OWP_opponents/numb_of_opponents;
    }



    // OUTPUT
    vector<double> team_RPI(numb_of_teams);
    out << "Case #" << i+1 << ": " << "\n";
    for(int i = 0; i < numb_of_teams; i++){
      team_RPI[i] = 0.25*team_WP[i] + 0.50*team_OWP[i] + 0.25*team_OOWP[i];
      out << team_RPI[i] << "\n";
    }


  }


  return 0;
}



