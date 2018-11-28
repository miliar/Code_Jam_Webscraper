#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

void solve(){
  int N;
  // read number of teams
  scanf("%d", &N);

  map<int, map<int, char> > matches;
  map<int, int> total;
  map<int, double> wp;
  map<int, double> owp;
  map<int, double> rpi;
  map<int, double> oowp;

  FOR(team, 0, N){
    string line;
    cin >> line;
    total[team]=0;
    wp[team]=0;
    FOR(i, 0, line.size()){
      if (line[i] != '.'){
        matches[team][i] = line[i];
        total[team]++;
        if (line[i] == '1'){
          wp[team]++;
        }
      }
    }
  }

  FOR(team, 0, N){
    //OWP = opponents winning percentage
    map<int, char>::iterator it = matches[team].begin();
    owp[team] = 0;
    //for all oponents
    while(it != matches[team].end()){
      int opponent = (*it).first;
      double temp = 0;
      if (total[opponent] <= 1){
        temp = 0;
      }
      else if ((*it).second == '0'){
        temp = (wp[opponent] - 1)/(total[opponent] - 1);
      } else{
        temp = wp[opponent] / (total[opponent] - 1);
      }
      owp[team] += temp;
      it++;
    }
    owp[team] /= total[team];
  }

  FOR(team, 0, N){
    map<int, char>::iterator it = matches[team].begin();
    oowp[team] = 0;
    wp[team] /= total[team];
    //for all oponents
    while(it != matches[team].end()){
      int opponent = (*it).first;
      oowp[team] += owp[opponent];
      it++;
    }
    oowp[team] /= total[team];
    rpi[team] = 0.25*(wp[team] + oowp[team]) + 0.5*owp[team];  
    printf("%1.10f\n", rpi[team]);
  }

}

int main()
{
  int t;
  scanf("%d", &t);
  FOR(testcase, 0, t){
    printf("Case #%d:\n", testcase + 1);
    solve();
  }
  return 0;
}


