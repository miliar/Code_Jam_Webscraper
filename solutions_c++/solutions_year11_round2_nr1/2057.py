#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

typedef long long          ll;
typedef unsigned long long ull;

using namespace std;

double
compute_wp(ull N, ull C, char m[200][200], ull skip)
{
  double tg = 0;
  double tw = 0;

  for (ull i = 0; i < N; ++i)
  {
    if (skip == i)
      continue;

    if (m[C][i] != '.')
    {
      ++tg;

      if (m[C][i] == '1')
        ++tw;
    }
  }

  return tg != 0 ? tw / tg : 0;
}

void
run(unsigned casenb)
{
  ull N = 0;
  char m[200][200];

  cout.precision(12);
  cin >> N;

  vector<double> wp(N);
  vector<double> owp(N);
  vector<double> oowp(N);

  cout << endl;

  for (ull i = 0; i < N; ++i)
  {
    std::string scores;

    cin >> scores;
    for (ull j = 0; j < N; ++j)
      m[i][j] = scores[j];
  }

  for (ull i = 0; i < N; ++i)
    wp[i] = compute_wp(N, i, m, -1);

  for (ull i = 0; i < N; ++i)
  {
    double total = 0;
    double games = 0;

    for (ull j = 0; j < N; ++j)
    {
      if (m[i][j] != '.')
      {
        total += compute_wp(N, j, m, i);
        ++games;
      }
    }
    owp[i] = games != 0 ? (total / games) : 0;
  }

  for (ull i = 0; i < N; ++i)
  {
    double total = 0;
    double games = 0;

    for (ull j = 0; j < N; ++j)
      if (m[i][j] != '.')
      {
        total += owp[j];
        games++;
      }
    oowp[i] = games != 0 ? (total / games) : 0;
  }

  for (ull i = 0; i < N; ++i)
    cout << (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]) << endl;
}

int
main(int argc, char* argv[])
{
  ull T = 0;

  cin >> T;
  for (ull i = 1; i <= T; ++i)
  {
    cout << "Case #" << i << ":";
    run(i);
  }

  return 0;
}
