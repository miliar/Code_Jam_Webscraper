#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

int64 X, S, R, T, N;
int64 boost;
int64 noboost;

typedef map<int64, int64> DDMAP;
DDMAP smap;

void solve(int caseNum) {
  cin>>X>>S>>R>>T>>N;
  smap.clear();
  boost = R-S;

  noboost = X;
  REP(i, 0, N) {
    int64 start, end, w;
    cin>>start>>end>>w;

    int64 speed = w+S;
    int64 len = end-start;
    if (smap.count(speed)==0)
      smap[speed] = 0;
    smap[speed] += len;

    noboost -= len;
  }
  smap[S] = noboost;
  // for (DDMAP::iterator it=smap.begin(); it!=smap.end(); ++it) cout<<it->first<<" "<<it->second<<endl;

  double bo = T;
  double rslt = 0;

  for (DDMAP::iterator it=smap.begin(); it!=smap.end(); ++it) {
    double len = it->second;
    double spd = it->first;
    if (bo>0) {
      double boosted = spd + boost; // speed
      double costable = len / boosted; //time
      double cost;
      if (costable>bo) {
        cost = bo;
        bo = 0;
      } else {
        cost = costable;
        bo -= cost;
      }

      double bo_dist = boosted*cost;
      double walk_dist = double(len)-bo_dist;
      // cout<<boosted<<" "<<costable<<endl;

      // cout<<walk_dist<<endl;
      // cout<<costable;
      // cout<<len<<" "<<bo_dist<<endl;
      rslt += cost;
      rslt += (walk_dist/spd);
    } else {
      rslt += (len/spd);
    }
  }

  printf("Case #%i: %.9lf", caseNum, rslt);
  printf("\n");
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

