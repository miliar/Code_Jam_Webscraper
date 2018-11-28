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
int a[30][30];
int cc[30];
int main() {
#ifdef DBG
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif
  int t;
  cin >> t;
  string s;
  getline (cin, s);
  for (int qq = 1; qq <= t; ++qq) {
    getline (cin, s);
    int l = 0;
    while (s[l] == ' ')
      ++l;
    int n = 0;
    vector <int> b[30];
    while (s[l] != ' ') {
      n = n * 10 + s[l] - '0';
      ++l;
    }
    for (int i = 0; i < 30; ++i) {
      for (int j = 0; j < 30; ++j) {
        a[i][j] = -1;
      }
      cc[i] = 0;
    }
    for (int j = 0; j < n; ++j) {
      while (s[l] == ' ')
        ++l;
      a[s[l] - 'A'][s[l + 1] - 'A'] = s[l + 2] - 'A';
      a[s[l + 1] - 'A'][s[l] - 'A'] = s[l + 2] - 'A';
      ++l;
      ++l;
      ++l;
    }
    n = 0;
    while (s[l] == ' ') {
      ++l;
    }
    while (s[l] != ' ') {
      n = n * 10 + s[l] - '0';
      ++l;
    }
    for (int i = 0; i < n; ++i) {
      while (s[l] == ' ') {
        ++l;
      } 
      b[s[l] - 'A'].push_back(s[l + 1] - 'A');
      b[s[l + 1] - 'A'].push_back(s[l] - 'A');
      ++l;
      ++l;
    }
    while (s[l] == ' ') {
      ++l;
    }
    n = 0;
    while (s[l] != ' ') {
      n = n * 10 + s[l] - '0';
      ++l;
    }
    while (s[l] == ' ')
      ++l;
    vector <int> q;
    q.push_back(s[l] - 'A');
    cc[s[l] - 'A']++;
    ++l;
    for (int i = 1; i < n; ++i) {
      q.push_back(s[l] - 'A');
      cc[s[l] - 'A']++;
      if (q.size() != 0) {
        while (q.size() > 1 && a[q[q.size() - 1]][q[q.size() - 2]] != -1) {
          int w = a[q[q.size() - 1]][q[q.size() - 2]];
          cc[q[q.size() - 1]]--;
          cc[q[q.size() - 2]]--;
          q.pop_back();
          q.pop_back();
          cc[w]++;
          q.push_back(w);
        }
      }
      int w = q[q.size() - 1];
      if (b[w].size() != 0) {
        for (int j = 0; j < b[w].size(); ++j) {
          if (cc[b[w][j]] != 0 || (b[w][j] == w && (cc[w] >= 2))) {
            while (q.size() != 0) {
              cc[q[q.size() - 1]]--;
              q.pop_back();
            }
            break;
          }
        }
      }
      ++l;
    }
    cout << "Case #" << qq << ": [";
    if (q.size() != 0) {
      for (int i = 0; i < q.size() - 1; ++i) {
        cout << (char)(q[i] + 'A') << ", ";  
      } 
      cout << (char)(q[q.size() - 1] + 'A');
    }
    cout << ']' << endl;
  }
  return 0;
}