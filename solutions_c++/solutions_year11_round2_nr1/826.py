#include <iostream>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

#define MAX 100

using namespace std;

int won[MAX];
int games[MAX];
int played[MAX][MAX];

double wp[MAX];
double owp[MAX];
double oowp[MAX];

int n;
string str;

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t<=tt; t++) {
    memset(won, 0, sizeof(won));
    memset(games, 0, sizeof(games));
    memset(played, 0, sizeof(played));
    memset(wp, 0, sizeof(wp));
    memset(owp, 0, sizeof(owp));
    memset(oowp, 0, sizeof(oowp));

    cin >> n;
    for (int i = 0; i<n; i++) {
      cin >> str;
      for (int j=0; j<n; j++) {
	if (str[j] != '.') {
	  games[i]++;
	  played[i][j] = (str[j]=='1'?1:2);
	}
	if (str[j] == '1')
	  won[i]++;
      }

      wp[i] = ((double)won[i])/games[i];
    }

    for (int i = 0; i<n; i++) {
      double sum = 0;
      for (int j = 0; j<n; j++) {
	if (played[i][j]) {
	  if (played[i][j] == 1) 
	    sum += (double)(won[j])/(games[j]-1);
	  else
	    sum += ((double)(won[j]-1))/(games[j]-1);
	}
      }
      owp[i] = sum/games[i];
    }

    for (int i = 0; i<n; i++) {
      double sum = 0;
      for (int j = 0; j<n; j++) {
	if (played[i][j])
	  sum += owp[j];
      }
      oowp[i] = sum/games[i];
    }

    cout << "Case #" << t << ":" << endl;
    for (int i = 0; i<n; i++)
      printf("%.8lf\n", wp[i]/4+owp[i]/2+oowp[i]/4);

  }
  return 0;
}
