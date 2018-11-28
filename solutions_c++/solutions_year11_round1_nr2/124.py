
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;



int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases) {
    vector<string> res;
    int nDict, nList;
    cin >> nDict >> nList;
    vector<string> dict;
    
    REP(i, nDict){
      string s;
      cin >> s;
      dict.push_back(s);
    }
    
    REP(iList, nList){
      char list[30];
      cin >> list;
      int id = 0;
      int maxi = 0;
      REP(iDict, nDict){
	string cur = dict[iDict];
	int len = cur.size();
	int point = 0;
	vector<string> cand;
	REP(i, nDict){
	  if((int)dict[i].size() == len){
	    cand.push_back(dict[i]);
	  }
	}
	
	REP(iList, 26){
	  assert(cand.size() > 0);
	  if(cand.size() == 1){
	    goto UPDATE;
	  }
	  char ch = list[iList];
	  bool contains = false;
	  REP(it, cand.size()){
	    REP(i, len){
	      if(cand[it][i] == ch){
		contains = true;
		goto LB1;
	      }
	    }
	  }
	LB1:
	  if(contains){
	    bool cost = true;
	    REP(i, len){
	      if(cur[i] == ch){
		cost = false;
		break;
	      }
	    }
	    
	    if(cost)
	      point++;
	    vector<string> nextcand;
	    REP(it, cand.size()){
	      bool ok = true;
	      REP(i, len){
		if((cand[it][i] == ch || cur[i] == ch) && cand[it][i] != cur[i]){
		  ok = false;
		  break;
		}
	      }
	      if(ok){
		nextcand.push_back(cand[it]);
// 		cerr << s << " ";
	      }
	    }
// 	    cerr << endl;
	    cand.swap(nextcand);
	  }
	}
	
      UPDATE:
	if(point > maxi){
	  maxi = point;
	  id = iDict;
	}
      }
      res.push_back(dict[id]);
    }
    
    cout << "Case #" << (iCase+1) << ":";
    REP(i, res.size())
      cout << " " << res[i];
    cout << endl;
  }
  
  return 0;
}
