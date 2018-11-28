#include <algorithm>
#include <cmath>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int t(0);
  input >> t;
  for(int i(0); i != t; ++i) {
    cout << "Case #" << i+1 << ": ";
    int n;
    input >> n;
    vector<int> r;
    vector<int> p;
    vector<vector<int > > pp;
    pp.push_back(vector<int>());
    pp.push_back(vector<int>());
    for(int j(0); j != n; ++j) {
      char temp_char;
      input >> temp_char;
      r.push_back(temp_char == 'O' ? 0 : 1);
      int temp_int;
      input >> temp_int;
      p.push_back(temp_int);
      pp[r[j]].push_back(temp_int);
    }
    vector<int> pos;
    pos.push_back(1);
    pos.push_back(1);
    vector<int> next_pp;
    next_pp.push_back(0);
    next_pp.push_back(0);
    int y(0);
    for(size_t j(0); j != r.size(); ++j) {
      int steps = abs(pos[r[j]] - p[j]) + 1;
      y += steps;
      pos[r[j]] = p[j];
      next_pp[r[j]] += 1;
      if(next_pp[1-r[j]] < pp[1-r[j]].size()) {
	int dist = abs(pos[1-r[j]] - pp[1-r[j]][next_pp[1-r[j]]]);
	if(dist <= steps) {
	  pos[1-r[j]] = pp[1-r[j]][next_pp[1-r[j]]];
	} else {
	  if(pos[1-r[j]] > pp[1-r[j]][next_pp[1-r[j]]]){
	    pos[1-r[j]] -= steps;
	  } else {
	    pos[1-r[j]] += steps;
	  }
	}
      }
    }
    cout << y << endl;
  }
  input.close();
  return 0;
}
