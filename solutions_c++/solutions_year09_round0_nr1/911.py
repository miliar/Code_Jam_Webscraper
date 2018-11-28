
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, s) for(__typeof((s).begin() i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) (s).begin(), (s).end()

char dictionary[5010][20];

int main(void) {
  int length;
  int nDicts;
  int nCases;
  scanf("%d %d %d ", &length, &nDicts, &nCases);
  
  REP(iDict, nDicts){
    scanf("%s", dictionary[iDict]);
  }
  
  REP(iCase, nCases){
    int res = 0;
    string pattern;
    cin >> pattern;

    vector<vector<bool> > table(length, vector<bool>(26, false));
    int pos = 0;
    REP(iChar, length){
      if(pattern[pos] == '('){
	++pos;
	while(pattern[pos] != ')'){
	  table[iChar][pattern[pos++]-'a'] = true;
	}
	++pos;
      }else{
	table[iChar][pattern[pos++]-'a'] = true;
      }
    }

    REP(iDict, nDicts){
      bool ok = true;
      REP(iChar, length){
	if(table[iChar][dictionary[iDict][iChar]-'a'] == false){
	  ok = false;
	  break;
	}
      }
      if(ok)
	res++;
    }

    printf("Case #%d: %d\n", iCase+1, res);
  }
  
  
  return 0;
}
