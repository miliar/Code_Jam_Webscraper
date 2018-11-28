#include <iostream>
#include <vector>
#include <utility>

using namespace std;

void f(int C) {
  int N;
  cin >> N;
  char t[100][100];
  vector<pair<int, int> > wp;

  for(int i = 0; i < N; ++i) {
    int w = 0;
    int g = 0;
    for(int j = 0; j < N; ++j) {
      cin >> t[i][j];
      if(t[i][j] == '1') ++w;
      if(t[i][j] != '.') ++g;      
    }
    wp.push_back(make_pair(w,g));
  }
  vector<double> owp;
  for(int i = 0; i < N; ++i) {
    int n = 0;
    double s = 0.0;
    for(int j = 0; j < N; ++j) {
      if(t[i][j] != '.') {
        pair<int, int> p = wp[j];
        //        if(p.second > 1) {
          double r = p.first;
          if(t[i][j] == '0') r -= 1.0;
          s += r/(p.second-1.0);
          //}
        ++n;
      }
    }
    owp.push_back(s/n);
  }

  vector<double> oowp;
  for(int i = 0; i < N; ++i) {
    int n = 0;
    double s = 0.0;
    for(int j = 0; j < N; ++j) {
      if(t[i][j] != '.') {
        s += owp[j];
        ++n;
      }
    }
    oowp.push_back(s/n);
  }

  cout << "Case #"<< C << ":\n";
  cout.precision(18);
  for(int i = 0; i < N; ++i) {
    pair<int, int> p = wp[i];
    double rpi = (0.25*wp[i].first)/wp[i].second;
    rpi += 0.5*owp[i] + 0.25*oowp[i];
    cout << rpi << "\n";
  }
}

int main() {
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    f(i);
  }
}
