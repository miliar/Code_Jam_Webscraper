#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
  string line;
  stringstream ss;
  int T = 0;
  getline(cin, line);
  ss << line;
  ss >> T;
  ss.clear();

  for (int t=1;t<=T;t++) {
    getline(cin, line);
    ss << line;
    long long A=0, B=0;
    ss >> A >> B;
    ss.clear();
    vector<long double> p;
    getline(cin, line);
    ss << line;
    long double prob;
    for (long long i=0;i<A;i++) {
      ss >> prob;
      p.push_back(prob);
    }
    ss.clear();
    long long k = 0;
    vector<long double> s;
    while (k <= A) {
      long double skeys = 0;
      long double prod = 1;
      long double keys = A-k;
      for (long long i=0;i<k;i++) {
        prod *= p[i];
      }
      for (long long i=k;i<B;i++) {
        keys++;
      }
      keys++;
      skeys = (prod * keys) + ((1-prod) * (keys+B+1));
      // cout << prod << " * " << keys << " + " << (1-prod) << " * " << (keys+B+1) << " = " << skeys << endl;
      s.push_back(skeys);
      k++;
    }
    s.push_back(B+2);
    // cout << "stop: " << (B+2) << endl;
    long double min=3*B;
    for (long long i=0;i<s.size();i++) {
      if (min > s[i])
        min = s[i];
    }
    // cout << "Case #" << t << ": " << min << endl;
    printf("Case #%d: %Lf\n", t, min);
  }

  return 0;
}

