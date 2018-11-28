
#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

#define REP(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases){
    map<string, char> combine;
    map<char, set<char> > oppose;
    
    oppose['Q'] = set<char>();
    oppose['W'] = set<char>();
    oppose['E'] = set<char>();
    oppose['R'] = set<char>();
    oppose['A'] = set<char>();
    oppose['S'] = set<char>();
    oppose['D'] = set<char>();
    oppose['F'] = set<char>();
    
    
    int nCombine;
    cin >> nCombine;
    REP(i, nCombine){
      string s;
      cin >> s;
      if(s[0] > s[1])
	swap(s[0], s[1]);
      string key = "AB";
      key[0] = s[0];
      key[1] = s[1];
      combine[key] = s[2];
    }

    int nOppose;
    cin >> nOppose;
    REP(i, nOppose){
      string s;
      cin >> s;
      oppose[s[0]].insert(s[1]);
      oppose[s[1]].insert(s[0]);
    }
    
    int len;
    string input;
    vector<char> ans;
    cin >> len >> input;
    REP(i, len){
      char ch = input[i];
      if(i > 0){
	// cmb
	string s = "AB";
	s[0] = ans.back();
	s[1] = ch;
	if(s[0] > s[1])
	  swap(s[0], s[1]);
	if(combine.count(s)){
	  ans.pop_back();
	  ans.push_back(combine[s]);
	  goto NEXT;
	}

	// opp
	REP(j, ans.size()){
	  if(oppose[ch].count(ans[j])){
	    ans.clear();
	    goto NEXT;
	  }
	}
      }
      
	ans.push_back(ch);
    NEXT:
	;//
    }
    
    cout << "Case #" << (iCase+1) << ": [";
    REP(i, ans.size()){
      if(i > 0){
	cout << ", ";
      }
      cout << ans[i];
    }
    cout << "]" << endl;
  }
  return 0;
}
