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

int gcd(int a, int b)
{
    while (true) {
        a = a % b;
		if (a == 0) return b;
		b = b % a;
        if (b == 0) return a;
    }
}

int find_inc(int p)
{
    int l = gcd(100, p);
    if (l == 0) {
        l = p;
    } else {
        l = p / l;
    }
    return l;
}

const int max_r = 1000000;

bool solve(int n, int pd, int pg)
{
    if (pd == 0) {
        if (pg != 0) {
            return false;
        } else {
            return true;
        }
    }
    if (pg == 0 && pd != 0) {
        return false;
    }
    int lq = find_inc(pd);
    int lr = find_inc(pg);
    cdebug << "lq: " << lq << ", lr: " << lr << endl;
    for (int q = lq; q <= (n*pd/100); q+=lq) {
        for (int r = (q/lr+1)*lr; r <= (max_r*pg/100); r+=lr) {
            int d = 100*q/pd;
            int g = 100*r/pg;
#if 0
            cdebug << "\tg: " << g << ", d: " << d;
            cdebug << ", r: " << r << ", q: " << q << endl;
#endif
            if (r - q < 0) continue;
            if (g - d >= r - q) {
                cdebug << "g: " << g << ", d: " << d;
                cdebug << ", r: " << r << ", q: " << q << endl;
                return true;
            }
        }
    }
    return false;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    string s;
//    getline(cin, s);
    for (int i = 0; i < t; i++) {
        cdebug << "reading case #" << (i+1) << endl;
        int n, pd, pg;
        cin >> n >> pd >> pg;
        cdebug << "case #" << (i+1);
        cdebug << ", n: " << n;
        cdebug << ", pd: " << pd;
        cdebug << ", pg: " << pg;
        cdebug << endl;
        string s = solve(n, pd, pg) ? "Possible" : "Broken";
        cout << "Case #" << (i+1) << ": " << s << endl;
    }
    return 0;
} 
