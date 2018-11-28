// -lm -lcrypt -O2 -pipe -DONLINE_JUDGE

#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <string>
#include <iostream>
#include <utility>
#include <ctype.h>

using namespace std;

#ifdef ONLINE_JUDGE
ostream cnull(0);
#define cdebug cnull
#else
#define cdebug cerr
#endif

template <typename T>
std::ostream& operator<< (std::ostream& out, const vector<T>& v)
{
  out << "[";
  for (typename vector<T>::const_iterator i = v.begin(); i != v.end(); i++) {
    if (i != v.begin()) {
      out << ", ";
    }
    out << *i;
  }
  out << "]";
  return out;
}

template <typename T, typename U>
std::ostream& operator<< (std::ostream& out, const pair<T, U>& v)
{
  out << "(" << v.first << ", " << v.second << ")";
  return out;
}

template <typename T, typename U>
std::ostream& operator<< (std::ostream& out, const map<T, U>& v)
{
  out << "{";
  for (typename map<T, U>::const_iterator i = v.begin(); i != v.end(); i++) {
    if (i != v.begin()) {
      out << ", ";
    }
    out << (*i).first << " -> " << (*i).second;
  }
  out << "}";
  return out;
}

template <typename T, typename U>
std::ostream& operator<< (std::ostream& out, const multimap<T, U>& v)
{
  for (typename map<T, U>::const_iterator i = v.begin(); i != v.end(); i++) {
    if (i != v.begin()) {
      out << ", ";
    }
    out << (*i).first << " -> " << (*i).second;
  }
  return out;
}

vector<double> solve(int n, const vector<string>& ss) 
{
    int w[n], g[n];
    double wp[n][n], owp[n], oowp[n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int w = count(ss[i].begin(), ss[i].end(), '1');
            if (ss[i][j] == '1') w -= 1;
            int g = w + count(ss[i].begin(), ss[i].end(), '0');
            if (ss[i][j] != '.' && ss[i][j] != '1') g -= 1;
            wp[i][j] = (double)w / (double)g;
        }
    }
    for (int i = 0; i < n; i++) {
        int g = 0;
        owp[i] = 0.0;
        for (int j = 0; j < n; j++) {
            if (ss[i][j] != '.') {
                owp[i] += wp[j][i];
                g++;
            }
        }
        owp[i] /= (double)g;
    }
    for (int i = 0; i < n; i++) {
        int g = 0;
        oowp[i] = 0.0;
        for (int j = 0; j < n; j++) {
            if (ss[i][j] != '.') {
                oowp[i] += owp[j];
                g++;
            }
        }
        oowp[i] /= (double)g;
    }
    vector<double> r(n);
    for (int i = 0; i < n; i++) {
        r[i] = 0.25*wp[i][i]+0.5*owp[i]+0.25*oowp[i];
    }
    return r;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    string s;
//    getline(cin, s);
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<string> ss(n);
        for (int j = 0; j < n; j++) {
            cin >> ss[j];
        }
        vector<double> r = solve(n, ss);
        cout << "Case #" << (i+1) << ":" << endl;
        for (int j = 0; j < n; j++) {
            printf("%.8lf\n", r[j]);
        }
    }
    return 0;
} 
