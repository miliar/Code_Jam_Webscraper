#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

int main() {
  ifstream cin("A-large (2).in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<string> table(N, string(N, 0));
    vector<double> WP(N);
    vector<int> nums(N);
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        char c;
        cin >> c;
        if(c == '1')
          WP[i] += 1;
        table[i][j] = c;
      }
    }
    for(int i = 0; i < N; i++) {
      int num = 0;
      for(int j = 0; j < N; j++)
        if(table[i][j] != '.')
          num++;
      WP[i] /= num;
      nums[i] = num;
    }
    vector<double> OWP(N);
    for(int i = 0; i < N; i++) {
      int num = 0;
      double wp = 0;
      for(int j = 0; j < N; j++) {
        if(table[i][j] != '.') {
          num++;
          wp += (WP[j]*nums[j] - (table[i][j] == '0'))/(nums[j]-1);
        }
      }
      OWP[i] = wp/num;
    }
    vector<double> OOWP(N);
    for(int i = 0; i < N; i++) {
      int num = 0;
      double wp = 0;
      for(int j = 0; j < N; j++) {
        if(table[i][j] != '.') {
          num++;
          wp += OWP[j];
        }
      }
      OOWP[i] = wp/num;
    }
    cout << "Case #" << t << ":";
    //cout << " ";
    cout.precision(15);
    cout << endl;
    for(int i = 0; i < N; i++) {
      cout << 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i] << endl;
    }
    //cout << endl;
  }
}
