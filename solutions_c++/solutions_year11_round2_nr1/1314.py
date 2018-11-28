#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>

using namespace std;

#define FOR(i, a) for( (i)=0; i < (a); (i)++)
template<typename T> bool min(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool max(T& x, T y) { if (x >= y) return false; x = y; return true; }

void doTest() {
  int teams;
  scanf("%d", &teams);
  vector<double> owf(teams);
  vector<int> games(teams);
  vector<int> wins(teams);
  vector<double> oowf(teams);
  vector<double> wp(teams);
  vector<string> matches(teams);
  for (int i=0; i< teams; i++) {
    int won = 0, played = 0;
    while(matches[i].length() == 0) {
      cin >> matches[i];
    }
    for (int j = 0; j < matches[i].length(); j++) {
      if((matches[i])[j] != '.') {
	played++;
      }
      if((matches[i])[j] == '1') {
	won++;
      }
    }
    wins[i] = won;
    games[i] = played;
    wp[i] = ((double)won)/played;
    //  cout << i << " won " << wp[i] << " games" << endl;
  }
  
  for(int i=0; i < teams; i++) {
    double tot = 0.0d;
    int count = 0;

    for(int j=0; j < teams; j++) {
      if((matches[i])[j] != '.') {
	count++;
	int exceptThis = games[j] - 1;
	int won = wins[j];
	if((matches[i])[j] == '0') won--;
	tot += ((double)won)/exceptThis;
      }
    }
    owf[i] = tot/count;
  }

  for(int i=0; i < teams; i++) {
    double tot = 0.0d;
    int count = 0;
    for(int j=0; j < teams; j++) {
      if((matches[i])[j] != '.') {
	count++;
	tot += owf[j];
      }
    }
    oowf[i] = tot/count;
  }

  for(int i=0; i < teams; i++) {
    double res = 0.25 * wp[i] + 0.5 * owf[i] + 0.25 * oowf[i];
    cout << res << endl;
  }
  
}

int main(int argc, char ** argv) {
  // 
  freopen(argv[1], "r", stdin);

  int t;
  scanf("%d", &t);
  for(int i=0; i < t; i++) {
    cout << "Case #" << i+1 << ":" << endl;
    doTest();

  }
  return 0;
}
