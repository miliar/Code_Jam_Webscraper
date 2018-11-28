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

map<char, char> d;

void solve(vector<string>& ss)
{
    d['a'] = 'y';
    d['b'] = 'h';
    d['c'] = 'e';
    d['d'] = 's';
    d['e'] = 'o';
    d['f'] = 'c';
    d['g'] = 'v';
    d['h'] = 'x';
    d['i'] = 'd';
    d['j'] = 'u';
    d['k'] = 'i';
    d['l'] = 'g';
    d['m'] = 'l';
    d['n'] = 'b';
    d['o'] = 'k';
    d['p'] = 'r';
    d['q'] = 'z';
    d['r'] = 't';
    d['s'] = 'n';
    d['t'] = 'w';
    d['u'] = 'j';
    d['v'] = 'p';
    d['w'] = 'f';
    d['x'] = 'm';
    d['y'] = 'a';
    d['z'] = 'q';
    d[' '] = ' ';

    for (vector<string>::iterator i = ss.begin(); i < ss.end(); ++i) {
        for (string::iterator j = (*i).begin(); j < (*i).end(); ++j) {
            *j = d[*j];
        }
    }
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    string s;
    getline(cin, s);
    vector<string> ss;
    for (int i = 0; i < t; i++) {
        getline(cin, s);
        ss.push_back(s);
    }
    solve(ss);
    for (int i = 0; i < t; i++) {
        cout << "Case #" << (i+1) << ": " << ss[i] << endl;
    }
    return 0;
} 
