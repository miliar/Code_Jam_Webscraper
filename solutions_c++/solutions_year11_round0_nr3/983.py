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
  cin.ignore();
  vector<unsigned long> values;
  values.reserve(1000);
  while (cin >> N) {
    cin.ignore();
    ncase++;
    int i;
    values.clear();
    unsigned long sumfake = 0, sumreal = 0;
    unsigned long min = ULONG_MAX;
    for (i = 0; i < N; i++) {
      unsigned long val;
      cin >> val;
      values.push_back(val);
      sumfake = sumfake ^ val;
      sumreal += val;
      if (val < min)
        min = val;
    }

    printf("Case #%d: ", ncase);
    if (sumfake)
      printf("NO\n");
    else
      printf("%lu\n", sumreal - min);
       
  }
}