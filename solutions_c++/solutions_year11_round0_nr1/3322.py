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

enum {
    O = 1,
    B
};


int solve(int n, char ob[], int p[])
{
    int s = 0;
    int os = 0, bs = 0;
    int op = 1, bp = 1;
    int oq[n], bq[n];
    memset(oq, 1, sizeof(oq));
    memset(bq, 1, sizeof(bq));
    int oi = 0, bi = 0;
    for (int j = 0; j < n; j++) {
        cerr << ob[j] << p[j] << ", ";
        if (ob[j] == 'O') {
            oq[oi++] = j;
        } else {
            bq[bi++] = j;
        }
    }
    cerr << endl;
    int i = 0;
    const int on = oi, bn = bi;
    bi = oi = 0;
    while (bi < bn || oi < on || os != 0 || bs != 0) {
        if (os == 0 && oi < on) {
            int np = p[oq[oi]];
            os = abs(np - op) + 1;
            op = np;
        }
        if (bs == 0 && bi < bn) {
            int np = p[bq[bi]];
            bs = abs(np - bp) + 1;
            bp = np;
        }
        if (os == 1 && oq[oi] > 0 && ob[oq[oi]-1] != 0) {
            // wait
        } else if (os) os--;
        if (bs == 1 && bq[bi] > 0 && ob[bq[bi]-1] != 0) {
            // wait
        } else if (bs) bs--;
        if (os == 0 && oi < on) {
            cerr << " O! ";
            ob[oq[oi]] = 0;
            oi++;
        }
        if (bs == 0 && bi < bn) {
            cerr << " B! ";
            ob[bq[bi]] = 0;
            bi++;
        }
        if (bs != 0 && os != 0) {
            cerr << "    ";
        }
        ++s;
        cerr << s << ": Os: " << os << ", Op: " << op << ", Bs: " << bs << ", Bp: " << bp << endl;
    }
    return s;
}

int main(int argc, char* argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        char br[n];
        int p[n];
        for (int j = 0; j < n; j++) {
            cin >> br[j] >> p[j];
        }
        int r = solve(n, br, p);
        cout << "Case #" << (i+1) << ": " << r << endl;
    }
    return 0;
} 
