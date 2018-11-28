#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

inline int classify(const string& s, char c){
  int res = 0;
  for(int i=0, l=1;i<s.size();i++, (l<<=1))
    if(s[i] == c) res += l;

  return res;
}

map<string, int> dict;
string ord;

pair<int, string> recurse(const vector<string>& s, int l) {
  //std::cerr << "recurse({";for(int i=0;i<s.size();i++)cerr << s[i] << " ";cerr << "}, " << ord[l] << ")\n";
  if(l >= 26 || (s.size() == 1)) return make_pair(0, s[0]);
  if(!s.size()) cerr << "!!!!\n";

  map<int, vector<string> > m;

  for(vector<string>::const_iterator it=s.begin();it!=s.end();++it)
    m[classify(*it, ord[l])].push_back(*it);

  pair<int, string> opt(-1, "?");

  for(map<int, vector<string> >::const_iterator it=m.begin();it!=m.end();++it)
    if(it->first) {
      pair<int, string> cur = recurse(it->second, l+1);
      //std::cerr << "recurse({";for(int i=0;i<s.size();i++)cerr << s[i] << " ";cerr << "}, " << ord[l] << ")::::"
      //		<< "(" << cur.first << ", " << cur.second << ")>?(" << opt.first << ", " << opt.second << ")\n";
      if((cur.first > opt.first) || ((cur.first == opt.first) && (dict[cur.second] < dict[opt.second]))) opt = cur;
    } else {
      pair<int, string> cur = recurse(it->second, l+1);
      if(m.size() > 1) {
	//std::cerr << "++recurse({";for(int i=0;i<(it->second.size());i++) cerr << (it->second)[i] << " ";cerr << "}, " << ord[l] << ")\n";
	cur.first++;
      }
      //      std::cerr << "recurse({";for(int i=0;i<s.size();i++)cerr << s[i] << " ";cerr << "}, " << ord[l] << ")::::"
      //		<< "(" << cur.first << ", " << cur.second << ")>?(" << opt.first << ", " << opt.second << ")\n";
      if((cur.first > opt.first) || ((cur.first == opt.first) && (dict[cur.second] < dict[opt.second]))) opt = cur;
    }
  return opt;
}

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    int n, m;
    cin >> n >> m;
    vector<string> s[10];

    dict.clear();
    for(int i=0;i<n;i++){
      string cur;
      cin >> cur;
      dict[cur] = i;
      s[cur.length()-1].push_back(cur);
    }

    cout << "Case #" << tcase << ":";
    for(int i=0;i<m;i++) {
      cin >> ord;
      pair<int, string> opt(-1, "?");
      for(int j=0;j<10;j++)
	if(s[j].size()) {
	  pair<int, string> cur = recurse(s[j], 0);
	  //cerr << "(" << cur.first << ", " << cur.second << ")";
	  if((cur.first > opt.first) || ((cur.first == opt.first) && (dict[cur.second] < dict[opt.second]))) opt = cur;
	}
      cout << " " << opt.second;
      //cerr << "--";
    }
    //cerr << '\n';
    cout << '\n';
  }
}
