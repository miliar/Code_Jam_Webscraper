#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <iomanip>

using namespace std;

double getWP(char** array, int team, int N) {
  int played = 0, won = 0;
  for (int i = 0; i < N; i++) {
    if (array[team][i] == '0') {
      played++;
    }
    else if (array[team][i] == '1') {
      played++;
      won++;
    }
  }
  return ((double)won / (double)played);
}

double getOWP(char** array, int team, int N) {
  double average = 0;
  int teamsPlayed = 0;
  for (int i = 0; i < N; i++) {
    if (i == team) continue;

    //check if the team every plaed the team
    if (array[i][team] == '.') continue;
    teamsPlayed++;
    int played = 0, won = 0;
    for (int j = 0; j < N; j++) {
      if (j == team) continue;
      if (array[i][j] == '0') {
        played++;
      }
      else if (array[i][j] == '1') {
        played++;
        won++;
      }
    }
    average += ((double)won / (double)played);
  }
  return (average / (double)teamsPlayed);
}

double getOOWP(char** array, int team, int N) {
  double average = 0;
  int teamsPlayed = 0;
  for (int i = 0; i < N; i++) {
    if (i == team) continue;
    if (array[team][i] == '.') continue;
    teamsPlayed++;
    average += getOWP(array, i, N);
  }
  return average / (double)teamsPlayed;
}
int main() {
  cout.precision(12);
  ifstream fin ("A.in");
  ofstream fout ("A.out");

  int numTimes;
  fin >> numTimes;

  for (int turn = 1; turn <= numTimes; turn++) {
    int N;
    fin >> N;
    char** array = (char**)malloc(N * sizeof(char *));
    if (array == NULL) cout << "FUCK" << endl;
    for (int i = 0; i < N; i++) {
      string line;
      fin >> line;
      array[i] = (char*)malloc( N * sizeof(char *));
      if (array[i] == NULL) cout << "FUCK V2.0" << endl;
      for (int j = 0; j < N; j++) {
        array[i][j] = line[j];
      }
    }
    fout << "Case #" << turn << ":" << endl;
    for (int team = 0; team < N; team++) {
      double answer = (0.25 * getWP(array, team, N)) + (0.5 * getOWP(array, team, N)) + (0.25 * getOOWP(array, team, N));
      fout << answer << endl;
    }
  }
}
