#include <cstdio>
#include <map>
#include <string>
#include <vector>

using namespace std;

map <string,int> engineMap;
vector <int> queries;
  int numOfEngines;
  int numOfQueries;
  int numOfSwitches;

void read() {
  int actualEngine;
  char actualEngineName[200];
  string actualEngineNameString;
  engineMap.clear();
  
  scanf("%d\n",&numOfEngines);
  for (int actualEngine = 1; actualEngine <= numOfEngines; actualEngine++) {
    for (int c = 0; c < 200; c++){
      actualEngineName[c] = 0;
    }
    fgets(actualEngineName,200,stdin);
    actualEngineNameString = actualEngineName;
    engineMap[actualEngineNameString] = actualEngine;
  }
  scanf("%d\n",&numOfQueries);
  queries.clear();
  for (int c = 0; c < numOfQueries; c++) {
    for (int d = 0; d < 200; d++){
      actualEngineName[d] = 0;
    }
    fgets(actualEngineName,200,stdin);
    actualEngineNameString = actualEngineName;
    queries.push_back(engineMap[actualEngineNameString]);
  }
  
}

int solve() {
  int appeared[500];
  int numOfAppeared = 0;
  numOfSwitches = 0;
  for (int d = 1; d <= numOfEngines; d++) {
    appeared[d] = 0;
  }
  for (int c = 0; c < numOfQueries; c++) {
    if (appeared[queries[c]] == 0) {
      appeared[queries[c]] = 1;
      numOfAppeared++;
    }
    if (numOfAppeared == numOfEngines) {
      numOfAppeared = 0;
      numOfSwitches ++;
      c--;
      for (int d = 1; d <=numOfEngines; d++) {
        appeared[d] = 0;
      }
    }
    
  }
}

int main() {
  int numOfTests;
  scanf("%d",&numOfTests);
  for (int c = 1; c <= numOfTests; c++) {
    read();
    solve();
    printf("Case #%d: %d\n",c,numOfSwitches);
  }
}
