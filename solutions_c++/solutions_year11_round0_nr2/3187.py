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

#if 1
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

enum {
    O = 1,
    B
};

typedef vector<string> vs;

string revstr(const string& xs)
{
    string ys;
    for (string::const_reverse_iterator i = xs.rbegin();
         i < xs.rend();
         ++i) {
        ys += *i;
    }
    return ys;
}

bool combine(const vector<string>& cs, string & xs)
{
    string ys = xs.substr(0, 2);
    for (vs::const_iterator csi = cs.begin();
         csi < cs.end();
         ++csi) {
        string c = (*csi).substr(0, 2);
        for (int i = 0; i < 2; i++) {
            if (c == ys) {
                xs.replace(0, 2, 1, (*csi)[2]);
                cdebug << "COMBINE" << endl;
                return true;
            }
            char t = c[0];
            c[0] = c[1];
            c[1] = t;
        }
    }
    return false;
}

bool oppose(const vector<string>& cs, string & xs)
{
    for (vs::const_iterator csi = cs.begin();
         csi < cs.end();
         ++csi) {
        for (int i = 0; i < 2; i++) {
            const char a = (*csi)[i];
            const char b = (*csi)[1-i];
            size_t p = xs.find(a);
            if (p != string::npos) {// && (p != xs.size() - 1)) {
                string ys = xs.substr(p);
                size_t q = ys.find(b);
                if (q != string::npos) {
                    q += p+1;
                    xs.clear();
                    cdebug << "OPPOSE(" << p << ", " << q << "): " <<  xs << endl;
                    return true;
                }
            }
        }
    }
    return false;
}


string solve(const vector<string>& cs, const vector<string>& ds, string & xs)
{
    cdebug << "cs: " << cs << endl;
    cdebug << "ds: " << ds << endl;
    string ys, zs;
    while (!xs.empty()) {
        ys += xs[0]; xs.erase(0, 1);
        cdebug << "ys: " << ys << ", xs: " << xs << endl;
        if (ys.size() >= 2) {
            zs = revstr(ys);
            if (combine(cs, zs)) {
                ys = revstr(zs);
            } else {
                if (oppose(ds, zs)) {
                    ys = revstr(zs);
                }
            }
        }
    }
    zs = "[";
    if (!ys.empty()) {
        string::iterator it = ys.begin();
        zs += *it++;
        for (; it < ys.end(); ++it) {
            zs += ", ";
            zs += *it;
        }
    }
    zs += "]";
    return zs;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int ncs, nds, nxs;
        string xs;
        cin >> ncs;
//        cdebug << "ncs: " << ncs << endl;
        vector<string> cs(ncs);
        for (int j = 0; j < ncs; j++) {
            cin >> cs[j];
        }
        cin >> nds;
//        cdebug << "nds: " << nds << endl;
        vector<string> ds(nds);
        for (int j = 0; j < nds; j++) {
            cin >> ds[j];
        }
//        cdebug << "ds: " << ds << endl;
        cin >> nxs;
//        cdebug << "nxs: " << nxs << endl;
        cin >> xs;
        string r = solve(cs, ds, xs);
        cout << "Case #" << (i+1) << ": " << r << endl;
    }
    return 0;
} 
