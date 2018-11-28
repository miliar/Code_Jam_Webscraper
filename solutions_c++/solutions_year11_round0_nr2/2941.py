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
    cout << "Case #" << i+1 << ": [";
    int c;
    input >> c;
    vector<string> combinations;
    for(int j(0); j != c; ++j) {
      string temp;
      input >> temp;
      combinations.push_back(temp);
    }
    int d;
    input >> d;
    vector<string> opposed;
    for(int j(0); j != d; ++j) {
      string temp;
      input >> temp;
      opposed.push_back(temp);
    }
    int n;
    input >> n;
    string invocations;
    input >> invocations;
    string result("");
    for(int j(0); j != n; ++j) {
      char next = invocations[j];
      if(result.size() != 0) {
	char previous = result[result.size()-1];
	for(int k(0); k != combinations.size(); ++k) {
	  if (next == combinations[k][0] && previous == combinations[k][1]){
	    result.erase(result.size() - 1);
	    next = combinations[k][2];
	    break;
	  }
	  if (next == combinations[k][1] && previous == combinations[k][0]){
	    result.erase(result.size() - 1);
	    next = combinations[k][2];
	    break;
	  }
	}
      }
      result.push_back(next);
      for(int k(0); k != opposed.size(); ++k) {
	if(result.find(opposed[k][0]) != result.npos && result.find(opposed[k][1]) != result.npos) {
	  result.clear();
	  break;
	}
      }
    }
    for(int j(0); j != result.size(); ++j) {
      cout << result[j];
      if(j != result.size() - 1) {
	cout << ", ";
      }
    }
    cout << "]" << endl;
  }
  input.close();
  return 0;
}
