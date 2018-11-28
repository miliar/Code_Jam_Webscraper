#include <vector>
#include <iostream>
#include <utility>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

void solve(const vector<string>&,const vector<string>&,string&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    vector<string> combine,opposed;
    string element;
    int num_combines;
    cin >> num_combines;
    for(int j = 0; j < num_combines; j++){
      string c;
      cin >> c;
      combine.push_back(c);
    }
    int num_opposed;
    cin >> num_opposed;
    for(int j = 0; j < num_opposed; j++){
      string o;
      cin >> o;
      opposed.push_back(o);
    }
    int num_element; // not used
    cin >> num_element >> element;
    solve(combine,opposed,element);
    cout << "Case #" << i+1 << ": [";
    if(element.size() == 0) {cout << "]" << endl;} 
    else {
      for(size_t j = 0; j < element.size() - 1; j++){
	cout << element[j] << ", ";
      }
      cout << element[element.size()-1] << "]" << endl;
    }
  }
}

string make_key(char c1, char c2){
  char ckey[3];
  if(c1 > c2){
    ckey[0] = c2;
    ckey[1] = c1;
  } else {
    ckey[0] = c1;
    ckey[1] = c2;
  }
  ckey[2] = '\0';
  return string(ckey);
}

void solve(const vector<string>& combinev,
	   const vector<string>& opposedv,
	   string& element){
  map<string,string> combine;
  set<string> opposed;
  for(size_t i = 0; i < combinev.size(); i++){
    string c = combinev[i];
    string ckey = make_key(c[0],c[1]);
    string rep(c,2,1);
    combine.insert(pair<string,string>(ckey,rep));
  }
  for(size_t i = 0; i < opposedv.size(); i++){
    string c = opposedv[i];
    string okey = make_key(c[0],c[1]);
    opposed.insert(okey);
  }
  if(element.size() < 2) return;
  for(size_t i = 1; i < element.size();){
    string ckey = make_key(element[i-1],element[i]);
    map<string,string>::iterator ci = combine.find(ckey);
    if(ci != combine.end()) {
      element.replace(i-1,2,(*ci).second);
      continue; 
    }
    bool isopposed = false;
    for(size_t j = 0; j < i; j++){
      string okey = make_key(element[j],element[i]);
      set<string>::iterator oi = opposed.find(okey);
      if(oi != opposed.end()){
	element.erase(0,i+1);
	i = 1;
	isopposed = true;
	break;
      }
    }
    if(isopposed) continue;
    i++;
  }
}
