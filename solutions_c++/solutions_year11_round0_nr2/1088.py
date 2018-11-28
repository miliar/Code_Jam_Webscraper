#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    cout << "Case #" << tcase << ": [";
    int c;
    cin >> c;
    map<pair<char, char>, char> comb;
    for(int i=0;i<c;i++){
      char c1, c2, c3;
      cin >> c1 >> c2 >> c3;
      comb[make_pair(c1, c2)] = c3;
      comb[make_pair(c2, c1)] = c3;
    }

    int d;
    cin >> d;
    set<pair<char, char> > opp;
    for(int i=0;i<d;i++){
      char c1, c2;
      cin >> c1 >> c2;
      opp.insert(make_pair(c1, c2));
      opp.insert(make_pair(c2, c1));
    }

    int n;
    string cur;
    cin >> n;
    
    for(int i=0;i<n;i++){
      char cc;
      cin >> cc;
      bool opposed = false;
      if(cur.size() && comb.count(make_pair(cur[cur.size()-1], cc)))
	cur[cur.size()-1] = comb[make_pair(cur[cur.size()-1], cc)];
      else {
	for(size_t i=0;i<cur.size();i++)
	  if(opp.count(make_pair(cur[i], cc))){
	    opposed = true;
	    cur.clear();
	    break;
	  }
	if(!opposed) cur.push_back(cc);
      }
    }


    for(size_t i=0;i<cur.size();++i)
      if(i) cout << ", " << cur[i];
      else cout << cur[i];
    cout << "]\n";
  }
}
