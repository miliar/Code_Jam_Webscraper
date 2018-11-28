#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>

using namespace std;

int run_tc (int c) {
  string s;
  int nse = 0; // number of search engines.
  if(!getline(cin, s)) {
    cerr << "Error while reading the number of search engines." << endl;
    return -1;
  }
  stringstream ss(s);
  ss >> nse;

  vector<string> se;
  for (int i = 0; i < nse;) {
    if(!getline(cin, s)) {
      cerr << "Error while reading search engine." << endl;
      return -1;
    }
    if(s == "") continue;
    se.push_back(s);
    ++i;
  }


  int nq = 0; // number of queries
  if(!getline(cin, s)) {
    cerr << "Error while reading the number of queries." << endl;
    return -1;
  }
  stringstream ss2(s);
  ss2 >> nq;

  vector<string> q;
  for (int i = 0; i < nq;) {
    if(!getline(cin, s)) {
      cerr << "Error while reading query." << endl;
      return -1;
    }

    if(s == "") continue;
    q.push_back(s);
    ++i;
  }

  if(nse == 0 || nq == 0) {
    cout << "Case #" << c << ": 0" << endl;
    return 0;
  }

  int ns = -1; // number of switches
  int i = 0;
  int m = se.size();
  int n = q.size();

  while (i < n) {
    int mx = INT_MIN;
    for (int j = 0; j < m; ++j) {
      int k = i;
      string t = se[j];
      for (; k < n; ++k) {
        if (q[k] == t) {
          break;
        }
      }

      if((k-i) > mx) {
        mx = (k-i);
      }
    }
    if (mx <= 0) {
      cerr << "*** FATAL *** No progress made in search. I's value is " << i << endl;
      exit(1);
    }
    ++ns;
    i += mx;
  }
  if(ns < 0)
    ns = 0;
  cout << "Case #" << c << ": " << ns << endl;
  return 0;
}


int main(int argc, const char* argv[]) {
  int ntc = 0; // number of test cases
  string s;
  if(!getline(cin, s)) {
    cerr << "Error while reading the number of test cases." << endl;
    return -1;
  }

  stringstream ss(s);
  ss>>ntc;

  for (int i = 1; i <= ntc; ++i) {
    run_tc (i);
  }
}

