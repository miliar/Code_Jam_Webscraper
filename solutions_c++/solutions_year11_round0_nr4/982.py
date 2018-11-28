#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <climits>
#include <string>
#include <cctype>
#include <cstring>
#include <queue>
#include <stack>

using namespace std;

int main(int argc, char *argv[]) {
  int T; // num test cases
  int N; // size of case problem
  int ncase = 0; // current case number

  cin >> T;
  vector<unsigned long> values, sorted;
  values.reserve(1000);
  sorted.reserve(1000);
  while (cin >> N) {
    ncase++;
    int i;
    values.clear();
    for (i = 0; i < N; i++) {
      unsigned long val;
      cin >> val;
      values.push_back(val);
    }
    sorted = values;
    sort(sorted.begin(), sorted.end());
    vector<unsigned long>::iterator it1, it2;
    // ignore already in place
    for (it1 = values.begin(), it2 = sorted.begin(); it1 != values.end();) {
      if (*it1 == *it2) {
        it1 = values.erase(it1);
        it2 = sorted.erase(it2);
      }
      else
        it1++, it2++;
    }
    double avgtime = values.size();

    printf("Case #%d: %.7f\n", ncase, avgtime);
       
  }
}