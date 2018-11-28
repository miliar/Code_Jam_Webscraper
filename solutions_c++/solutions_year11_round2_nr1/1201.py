#include <iostream>
#include <cstdio>

using namespace std;

char sched[101][101];
int N;

double findwp(int team, int ignore) {
  int nplayed=0, nwon=0;
  for(int i = 0; i < N; i++) {
    if(i == ignore)
      continue;
    if(sched[team][i] != '.') {
      nplayed++;
    }
    if(sched[team][i] == '1') {
      nwon++;
    }
  }

  return double(nwon)/double(nplayed);
}

double findowp(int team) {
  double totWP = 0.0;
  int numOp = 0;
  for(int i = 0; i < N; i++) {
    if(sched[team][i] != '.') {
      numOp++;
      totWP += findwp(i, team);
    }
  }

  return totWP/numOp;
}

int main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; tc++) {
    cin >> N;

    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
	cin >> sched[i][j];
      }
    }

    printf("Case #%d:\n", tc);

    double OWPs[101];

    for(int team = 0; team < N; team++) {
      OWPs[team] = findowp(team);
    }

    for(int team = 0; team < N; team++) {
      double WP = findwp(team, team);
      double OWP = OWPs[team];
      
      double OOWP = 0.0;
      int numOp = 0;
      for(int i = 0; i < N; i++) {
	if(sched[team][i] != '.') {
	  numOp++;
	  OOWP += OWPs[i];
	}
      }
      OOWP /= numOp;

      double RPI = 0.25*WP + 0.5*OWP + 0.25*OOWP;

      printf("%0.8f\n", RPI);
    }

  }

  return 0;
}
