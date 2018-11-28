
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstring>

using namespace std;

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, s) for(__typeof((s).begin() i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) (s).begin(), (s).end()

#define WELCOME "welcome to code jam"

int size = strlen(WELCOME);
int memo[510][30];
string line;

int solve(int texti, int pati) {
  int& res = memo[texti][pati];
  if(res < 0){
    if(pati == size){
      res = 1;
    }else if(texti == (int)line.size()){
      res = 0;
    }else{
      res = solve(texti + 1, pati) % 10000;
      if(WELCOME[pati] == line[texti]){
	res = (res + solve(texti + 1, pati + 1)) % 10000;
      }
    }
  }
  return res;
}


int main(void) {
  int nCases;
  scanf("%d ", &nCases);
  REP(iCase, nCases){
    getline(cin, line);
    REP(i, 510) REP(j, 31)
      memo[i][j] = -1;
    printf("Case #%d: %04d\n", iCase+1, solve(0, 0));
    
  }
  return 0;
}
