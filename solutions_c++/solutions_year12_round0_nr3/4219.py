#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;
int T, A, B;
int memo[1001];

string toString(int x) {
  stringstream ss;
  ss << x;
  return ss.str();
}
int getNums(string x) {
  int ret = 0;
  int m = x.size();
  for (int i = 1; i < m; i++) {
    string tmp;
    for (int j = 0; j < m; j++) {
      tmp += x[(i+j)%m];
    }
    stringstream ss;
    ss << tmp;
    int c;
    ss >> c;
    if (c >= A && c <= B) {
      ret++;
    }
  }
  return ret;
}
void printV(vector<int>& v) {
  for (int i = v.size()-1; i > -1; i--) {
    cout << v[i] << " ";
  }
  cout << endl;
}
int doSmall(int a, int b) {
  int ret = 0;
  set<pair<int, int> > totalSet;
  for (int k = a; k <= b; k++) {
    string x = toString(k);
    int m = x.size();
    for (int i = 1; i < m; i++) {
      string tmp;
      for (int j = 0; j < m; j++) {
        tmp += x[(i+j)%m];
      }
      stringstream ss;
      ss << tmp;
      int c;
      ss >> c;
      if (c <= b && c > k && tmp.size() == x.size()) {
        totalSet.insert(make_pair(k, c));
      }
    }  
  }
  return totalSet.size();
}
int main(int argc, char** argv) {
  string file = argv[1];
  ifstream inF(file.c_str());
  file += ".out";
  ofstream outF(file.c_str());
  inF >> T;
  for (int i = 0; i < T; i++) {
    inF >> A >> B;
    int ret = doSmall(A, B);
    outF << "Case #" << i+1 << ": " << ret << endl;
  }
  outF.close();
  inF.close();
  return 0;
};
