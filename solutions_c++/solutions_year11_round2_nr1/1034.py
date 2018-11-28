#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
#include <stdio.h>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<string> mat;
    for (int i = 0; i < N; i++) {
      string tmp;
      cin >> tmp;
      mat.push_back(tmp);
    }
    vector<double> WP(N, 0);
    vector<int> sum(N, 0);
    for (int i = 0; i < N; i++) {
      int w = 0;
      for (int j = 0; j < N; j++) {
	if (mat[i][j] == '0') {
	  sum[i]++;
	} else if (mat[i][j] == '1') {
	  sum[i]++;
	  w++;
	}
      }
      WP[i] = w / (double)sum[i];
    }
    vector<double> OWP(N, 0);
    for (int i = 0; i < N; i++) {
      double tmp = 0;
      int total = 0;
      for (int j = 0; j < N; j++)
	if (mat[i][j] != '.') {// has match
	  total++;
	  tmp += (WP[j] * sum[j] - (mat[j][i] - '0')) / (double) (sum[j] - 1);
	}
      OWP[i] = tmp / (double) total;
      //cout << OWP[i] << total << endl;

    }

    cout << "Case #" << t << ": " << endl;

    for (int i = 0; i < N; i++) {
      double OOWP = 0;
      int total = 0;
      for (int j = 0; j < N; j++) 
	if (mat[i][j] != '.') {
	  total ++;
	  OOWP += OWP[j];
	}
      OOWP /= (double)total;
      double RPI = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP;
      printf("%.9f\n", RPI);
    }

    //cout << endl;
  }
  return 0;
}
