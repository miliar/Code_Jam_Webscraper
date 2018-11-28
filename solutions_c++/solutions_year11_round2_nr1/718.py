#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int N;
int a[100][100];
double wp[100];
double wp_no_me[100][100];
double owp[100];
double oowp[100];

int main() {
  int T; fin >> T;

  for (int t = 0; t < T; ++t) {
    fout << "Case #" << t + 1 << ":\n";
    fin >> N;
    for (int i = 0; i < N; ++i) {
      wp[i] = 0;
      for (int j = 0; j < N; ++j) {
        char ch;
        fin >> ch;
        if (ch == '1') a[i][j] = 1;
        else if (ch == '0') a[i][j] = 0;
        else a[i][j] = -1;
      }
    }

    for (int i = 0; i < N; ++i) {
      int won = 0;
      int tot = 0;
      for (int j = 0; j < N; ++j) {
        if (a[i][j] == 1) {won++;tot++;}
        else if (a[i][j] == 0) {tot++;}
      }
      wp[i] = (double)won/tot;
      //cout << wp[i] << endl;
      for (int j = 0; j < N; ++j) {
        if (a[i][j] == 1)
          wp_no_me[j][i] = ((double)(won - 1))/(tot - 1);
        else if (a[i][j] == 0)
          wp_no_me[j][i] = ((double)won)/(tot - 1);
        else 
          wp_no_me[j][i] = ((double)won)/tot;
        //cout << wp_no_me[j][i] << " " << " " << won << " " << tot << " ";
      } 
      //cout << endl;
    }

    for (int i = 0; i < N; ++i) {
      double tot_wp_no_me = 0;
      int opps = 0;
      for (int j = 0; j < i; ++j) {
        if (a[i][j] != -1) {
          tot_wp_no_me += wp_no_me[i][j];
          opps++;
        }
      }
      for (int j = i + 1; j < N; ++j) {
        if (a[i][j] != -1) {
          tot_wp_no_me += wp_no_me[i][j];
          opps++;
        }
      }
      owp[i] = tot_wp_no_me / opps;
    }

    for (int i = 0; i < N; ++i) {
      double tot_owp_no_me = 0;
      int opps = 0;
      for (int j = 0; j < N; ++j) {
        if (a[i][j] != -1) {
          tot_owp_no_me += owp[j];
          opps++;
        }
      }
      oowp[i] = tot_owp_no_me / opps;
    }

    for (int i = 0; i < N; ++i) {
      fout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
    }
  }
  return 0;
}