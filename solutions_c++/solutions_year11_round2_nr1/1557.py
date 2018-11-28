#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<string> matrix;
vector<double> wp;
vector<vector<double>> wpe;
vector<double> owp;
vector<double> oowp;
vector<double> rpi;

void Go() {
  wp.clear();
  wp.resize(matrix.size(), 0.0);
  wpe.clear();
  wpe.resize(matrix.size(), vector<double>(matrix.size(), 0.0));
  owp.clear();
  owp.resize(matrix.size(), 0.0);
  oowp.clear();
  oowp.resize(matrix.size(), 0.0);
  rpi.clear();
  rpi.resize(matrix.size(), 0.0);

  for (int idx = 0; idx < matrix.size(); ++idx) {
    int num_games = 0;
    int num_wins = 0;
    for (int oth = 0; oth < matrix.size(); ++oth) {
      if (matrix[idx][oth] == '.') {
	continue;
      }
      ++num_games;
      if (matrix[idx][oth] == '1') {
	++num_wins;
      }
    }
    wp[idx] = double(num_wins) / num_games;

    for (int oth = 0; oth < matrix.size(); ++oth) {
      if (matrix[idx][oth] == '.') {
	wpe[idx][oth] = wp[idx];
      } else if (matrix[idx][oth] == '1') {
	wpe[idx][oth] = double(num_wins - 1) / double(num_games - 1);
      } else {
	wpe[idx][oth] = double(num_wins) / double(num_games - 1);
      }
    }
  }

  for (int idx = 0; idx < matrix.size(); ++idx) {
    int num_opps = 0;
    double opps_wp = 0.0;
    for (int oth = 0; oth < matrix.size(); ++oth) {
      if (matrix[idx][oth] == '.') {
	continue;
      }
      opps_wp += wpe[oth][idx];
      ++num_opps;
    }
    owp[idx] = opps_wp / num_opps;
  }

  for (int idx = 0; idx < matrix.size(); ++idx) {
    int num_opps = 0;
    double opps_owp = 0.0;
    for (int oth = 0; oth < matrix.size(); ++oth) {
      if (matrix[idx][oth] == '.') {
	continue;
      }
      opps_owp += owp[oth];
      ++num_opps;
    }
    oowp[idx] = opps_owp / num_opps;
  }

  for (int idx = 0; idx < matrix.size(); ++idx) {
    rpi[idx] = 0.25 * wp[idx] + 0.50 * owp[idx] + 0.25 * oowp[idx];
  }
}

int main(int argc, char **argv) {
  fstream fin("in");

  int cases;
  fin >> cases;

  for (int C = 0; C < cases; ++C) {
    int num_teams;
    fin >> num_teams;
    matrix.resize(num_teams);

    for (int N = 0; N < num_teams; ++N) {
      fin >> matrix[N];
    }

    Go();

    cout << "Case #" << (C + 1) << ":" << endl;
    for (int idx = 0; idx < num_teams; ++idx) {
      cout.precision(12);
      cout << rpi[idx] << endl;
    }
  }

  return 0;
}
