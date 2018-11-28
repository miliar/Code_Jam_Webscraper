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

const int N = 50;
char s[N][N];

bool solve(int r, int c)
{
    for (int j = 0; j < r-1; j++) {
        for (int k = 0; k < c-1; k++) {
            if (s[j][k] == '#'
                && s[j][k+1] == '#'
                && s[j+1][k] == '#'
                && s[j+1][k+1] == '#') {
                s[j][k] = s[j+1][k+1] = '/';
                s[j+1][k] = s[j][k+1] = '\\';
            }
        }
    }
    for (int j = 0; j < r; j++) {
        for (int k = 0; k < c; k++) {
            if (s[j][k] == '#') return false;
        }
    }
    return true;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int r, c;
        cin >> r >> c;
        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                cin >> s[j][k];
            }
        }
        bool o = solve(r, c);
        cout << "Case #" << (i+1) << ":" << endl;
        if (o) {
            for (int j = 0; j < r; j++) {
                for (int k = 0; k < c; k++) {
                    cout << s[j][k];
                }
                cout << endl;
            }
        } else {
            cout << "Impossible" << endl;
        }
    }
    return 0;
} 
