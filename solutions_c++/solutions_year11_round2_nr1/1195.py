#include <fstream>
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

double wp(int team, const vector<string>& schedule){
  const string& row = schedule[team];

  double total = 0.0, wins = 0.0;
  for(int i = 0, n = row.size(); i < n; ++i){
    if(row[i] != '.'){
      total++;

      if(row[i] == '1')
        wins++;
    }
  }

  return wins / total;
}

double owp(int team, const vector<string>& schedule){
  const string& row = schedule[team];

  int nopp = 0;
  double total_wp = 0.0;
  for(int i = 0, n = row.size(); i < n; ++i){
    if(row[i] != '.'){
      nopp++;

      const string& orow = schedule[i];
      double total = 0.0;
      double wins = 0.0;
      for(int j = 0, nj = orow.size(); j < nj; ++j){
        if(j == team)
          continue;

        if(orow[j] != '.'){
          total++;

          if(orow[j] == '1')
            wins++;
        }
      }

      total_wp += wins / total;
    }
  }

  return total_wp / nopp;
}

double oowp(int team, const vector<string>& schedule){
  const string& row = schedule[team];

  double total_owp = 0.0;
  int nopp = 0;
  for(int i = 0, n = row.size(); i < n; ++i){
    if(row[i] != '.'){
      nopp++;
      total_owp += owp(i, schedule);
    }
  }

  return total_owp / nopp;
}

void run(istream& input){
  int ncases;

  input >> ncases;

  for(int icase = 0; icase < ncases; ++icase){
    int nteams;
    input >> nteams;

    vector<string> schedule;
    for(int iteam = 0; iteam < nteams; ++iteam){

      string row;
      input >> row;
      schedule.push_back(row);

    }

    printf("Case #%d:\n", icase + 1);

    for(int iteam = 0; iteam < nteams; ++iteam){
      printf("%f\n",
        0.25 * wp(iteam, schedule)
        + 0.50 * owp(iteam, schedule)
        + 0.25 * oowp(iteam, schedule));
    }
  }

}

int main(int argc, char *argv[]){

  if(argc > 1)
    run(ifstream(argv[1]));
  else
    run(cin);

  return 0;
}