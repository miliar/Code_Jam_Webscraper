#include <iostream>
#include <vector>
#include <cassert>
#include <iomanip>
using namespace std;

const int MAX_N = 200;

int result[MAX_N][MAX_N];
double WP[MAX_N];
double OWP[MAX_N];
double OOWP[MAX_N];

double compute_wp(int N, int team, int excluding = -1) {
  double wins = 0;
  double games = 0;
  for(int i=0;i<N;i++) {
    if(i == excluding)
      continue;
    if(result[team][i]) {
      wins += (result[team][i] > 0);
      games += 1;
    }
  }
  if(games == 0)
    return 0;
  return wins / games;
}

int main()
{
  int T;
  cin >> T;
  for(int c=1;c<=T;c++) {
    int N;
    cin >> N;
    assert(N < 200);
    for(int i=0;i<N;i++) {
      string row;
      cin >> row;
      assert(row.size() == N);
      for(int j=0;j<N;j++) {
	char ch = row[j];
	if(ch == '1')
	  result[i][j] = 1;
	else if(ch == '0')
	  result[i][j] = -1;
	else if(ch == '.')
	  result[i][j] = 0;
	else
	  assert(false);
      }
    }

    for(int i=0;i<N;i++) {
      WP[i] = compute_wp(N, i);
      OWP[i] = 0;
      OOWP[i] = 0;
    }

    for(int i=0;i<N;i++) {
      double owp_sum = 0;
      double total = 0;
      for(int j=0;j<N;j++) {
	if(result[i][j]) {
	  owp_sum += compute_wp(N, j, i);
	  total += 1;
	}
      }
      if(total > 0)
	OWP[i] = owp_sum / total;
    }

    for(int i=0;i<N;i++) {
      double oowp_sum = 0;
      double total = 0;
      for(int j=0;j<N;j++) {
	if(result[i][j]) {
	  oowp_sum += OWP[j];
	  total += 1;
	}
      }
      if(total > 0)
	OOWP[i] = oowp_sum / total;
    }

    cout << "Case #" << c << ":\n";
    for(int i=0;i<N;i++) {
      double RPI = .25 * WP[i] + .5 * OWP[i] + .25 * OOWP[i];
      cout << setprecision(15) << RPI << "\n";
    }
  }

  return 0;
}
