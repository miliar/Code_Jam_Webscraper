#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <cstdio>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {
    cout << "Case #" << t << ":" << endl;

    int N;
    cin >> N;

    vector<string> sc(N);
    for (int i = 0; i < N; ++i)
      cin >> sc[i];

    vector<double> WP(N);
    for (unsigned int i = 0; i < sc.size(); ++i) {
      double win = 0, vs = 0;
      for (unsigned int j = 0; j < sc[i].size(); ++j) {
	if (sc[i][j] != '.') {
	  ++vs;
	  if (sc[i][j] == '1')
	    ++win;
	}
      }
      if (vs != 0)
	WP[i] = win/vs;
      else
	WP[i] = 0;
    }

    vector<double> OP(N, 0.0);
    for (unsigned int i = 0; i < sc.size(); ++i) {
      double cnt = 0;
      for (unsigned int j = 0; j < sc.size(); ++j) {
	if (i == j || sc[j][i] == '.')
	  continue;
	double win = 0, vs = 0;
	for (unsigned int k = 0; k < sc[j].size(); ++k) {
	  if (k == i)
	    continue;
	  if (sc[j][k] != '.') {
	    ++vs;
	    if (sc[j][k] == '1')
	      ++win;
	  }
	}
	if (vs != 0)
	  OP[i] += win / vs;
	else
	  OP[i] = 0;
	++cnt;
      }
      if (cnt != 0)
	OP[i] /= cnt;
    }

    vector<double> OOP(N, 0.0);
    for (unsigned int i = 0; i < sc.size(); ++i) {
      double cnt = 0;
      for (unsigned int j = 0; j < sc.size(); ++j) {
	if (i == j || sc[j][i] == '.')
	  continue;
	OOP[i] += OP[j];
	++cnt;
      }
      if (cnt != 0)
	OOP[i] /= cnt;
    }

    for (int i = 0; i < N; ++i) {
      printf("%.12f\n", 0.25*WP[i] + 0.5*OP[i] + 0.25*OOP[i]);
    }

  }
  return 0;
}
