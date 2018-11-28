#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <iomanip>


using namespace std;

//#define DBG

int main() {
#ifdef DBG
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif
  int t;
  cin >> t;
  string s;
  getline (cin, s);
  for (int i = 1; i <= t; ++i) {
    getline (cin, s);
    int n = 0;
    int l = 0;
    while (s[l] == ' ') {
      ++l;
    }
    while (s[l] != ' ') {
      n = n * 10 + s[l] - '0';
      ++l;
    }
    vector <pair <int, int> > a;
    vector <int> b[3];
    for (int j = 0; j < n; ++j) {
      while (s[l] == ' ') {
        ++l;
      }
      int p;
      if (s[l] == 'O')
        p = 1;
      else
        p = 2;
      ++l;
      while (s[l] == ' ')
        ++l;
      int q = 0;
      while (l < s.length() && s[l] >= '0' && s[l] <= '9') {
        q = q * 10 + s[l] - '0';
        ++l;
      }
      a.push_back(make_pair(p, q));
      b[p].push_back(q);
    }
    b[1].push_back(1000);
    b[2].push_back(1000);
    int l1 = 1;
    int r1 = 1;
    int l2 = 0;
    int r2 = 0;
    int ss = 0;
    int time = 0;
    while (ss < a.size()) {
      ++time;
      if (a[ss].first == 1) {
        if (l1 != b[1][l2]) {
          if (l1 < b[1][l2])
            ++l1;
          else
            --l1;
        } else {
          ++l2;
          ++ss;
        }
        int f = 0;
        if (!f) {
          if (r1 < b[2][r2]) {
            ++r1;
          } else
            if (r1 > b[2][r2]) {
              --r1;
            }
        }
      } else {
        if (r1 != b[2][r2]) {
          if (r1 < b[2][r2])
            ++r1;
          else
            --r1;
        } else {
          ++r2;
          ++ss;
        }
        int f = 0;
        if (!f) {
          if (l1 < b[1][l2]) {
            ++l1;
          } else {
            if (l1 > b[1][l2])
              --l1;
          }
        }
      }
    }
    cout << "Case #" << i << ": " << time << endl;
  }
  return 0;
}