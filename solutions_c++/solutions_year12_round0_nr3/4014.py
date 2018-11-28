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

int ndigits(int y)
{
    int n = 0;
    while (y != 0) {
        y /= 10;
        n++;
    }
    return n;
}

int cycle(int x, int n)
{
    int s = x % 10;
    for (int i = 0; i < n-1; i++) {
        s *= 10;
    }
    return s + (x / 10);
}

int count(int n, int mx)
{
    int c = 0;
    int d = ndigits(n);
    int m = n;
    set<int> s;
    for (int i = 0; i < d-1; i++) {
        m = cycle(m, d);
        if (m > n && m <= mx) {
            set<int>::iterator it = s.find(m);
            if (it == s.end()) {
//                cerr << n << " " << m << endl;
                c++;
                s.insert(m);
            }
        }
    }
    return c;
}

int solve(int mn, int mx)
{
    int r = 0;
    for (int n = mn; n <= mx; n++) {
        r += count(n, mx);
    }
    return r;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    string s;
    getline(cin, s);
    for (int i = 0; i < t; i++) {
        int mn, mx;
        cin >> mn >> mx;
        int r = solve(mn, mx);
        cout << "Case #" << (i+1) << ": " << r << endl;
    }
    return 0;
} 
