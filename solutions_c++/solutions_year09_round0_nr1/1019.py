#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

int dict[5010][16];
int ptn[16];
int nLetters, nDicts, nCases;

int main(){
  cin >> nLetters >> nDicts >> nCases;
  REP(i, nDicts){
    REP(j, nLetters){
      char c;
      scanf("%1s", &c);
      dict[i][j] = 1 << (c-'a');
    }
  }
  REP(i, nCases){
    REP(j, nLetters){
      char c;
      scanf("%1s", &c);
      int code = 0;
      if(c == '('){
	while((c = getchar()) != ')'){
	  code |= 1 << (c-'a');
	}
      }else{
        code = 1 << (c-'a');
      }
      ptn[j] = code;
    }
    int res = 0;
    REP(j, nDicts){
      bool ok = true;
      REP(k, nLetters){
	if(ptn[k] & dict[j][k]) continue;
	ok = false;
	break;
      }
      if(ok){
	res++;
      }
    }
    cout << "Case #" << i+1 << ": " << res << endl;
  }
  return 0;
}

