#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;


map<string,string> combs() {
  map<string,string> m;
  int n;
  cin>>n;
  for (int i=0;i<n;i++) {
    string s;
    cin>>s;
    m[(string() + s[0]) + s[1]] = string() + s[2];
    m[(string() + s[1]) + s[0]] = string() + s[2];
  }
  return m;
}
set<string> opps() {
  set<string> m;
  int n;
  cin>>n;
  for (int i=0;i<n;i++) {
    string s;
    cin>>s;
    m.insert(s);
    m.insert(string() + s[1] + s[0]);
  }
  return m;  
}
int main() {
  int Q;
  cin >> Q;
  for (int q=1;q<=Q;q++) {
    map<string,string> combine = combs();
    set<string> opposed = opps();
    int p;
    cin>>p;
    string cmd;
    cin >> cmd;
    vector<string> r;
    for (int i=0;i<cmd.size();i++) {
      if (r.size() == 0) r.push_back(string() + cmd[i]);
      else {
	string comb = string() + r[r.size() - 1] + cmd[i];
	if (combine.find(comb) != combine.end()) {
	  r[r.size() - 1] = combine[comb];
	} else {
	  for (int j=0;j<r.size();j++) {
	    if (opposed.find(r[j]+cmd[i]) != opposed.end()) {
	      r.clear();
	      goto nxt;
	    }
	  }
	  r.push_back(string()+cmd[i]);
	}
      }
    nxt:;
    }
    cout << "Case #" << q << ": [";
    for (int i=0;i<r.size();i++) {
      if (i != 0) cout << ", ";
      cout << r[i];
    }
    cout << "]"<<endl;
  }
}
