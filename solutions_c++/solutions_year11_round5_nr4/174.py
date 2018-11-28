#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

template<typename T> ostream& operator<<( ostream &os, const vector<T> &v ) { os << "{"; for ( typename vector<T>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " " << *vi; } os << " }"; return os; }
template<> ostream& operator<<( ostream &os, const vector<string> &v ) { os << "{"; for ( vector<string>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " \"" << *vi << "\""; } os << " }"; return os; }
template<typename T, typename U> ostream& operator<<( ostream &os, const pair<T, U> &P ) { return os << "(" << P.first << ", " << P.second << ")"; }
template<typename T> ostream& operator<<( ostream &os, const set<T> &S ) { return os << vector<T>( S.begin(), S.end() ); }
template<typename T, typename U> ostream& operator<<( ostream &os, const map<T, U> &M ) { for ( typename map<T, U>::const_iterator mi=M.begin(); mi!=M.end(); ++mi ) { os << mi->first << " => " << mi->second << endl; } return os; }

typedef long long int64;

int64 bsqrt(int64 x) {
  int64 hi = 1;
  while (hi*hi < x) hi *= 2;
  int64 lo = 0;
  while (lo < hi) {
    int64 mid = (lo+hi) / 2;
    int64 mid2 = mid*mid;
    if (mid2 == x) return mid;
    if (mid2 < x) lo = mid+1;
    if (mid2 > x) hi = mid-1;
  }
  return lo;
}

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    string str;
    cin >> str;

    int qm = 0;
    for (int i=0; i<(int)str.size(); ++i) {
      qm += str[i] == '?';
    }

    int64 num = 0;
    for (int mask=0; mask<(1<<qm); ++mask) {
      int bit_index = 0;
      num = 0;
      for (int i=0; i<(int)str.size(); ++i) {
        int bit;
        if (str[i] == '?') bit = (mask >> bit_index++) & 1;
        else bit = str[i]-'0';
        num = 2*num + bit;
      }

      int64 sq = bsqrt(num);
      if (sq*sq == num) {
        break;
      }
    }

    string outbin;
    if (num == 0) outbin = "0";
    while (num > 0) {
      outbin += '0' + num % 2;
      num /= 2;
    }
    reverse(outbin.begin(), outbin.end());
    cout << "Case #" << tt << ": " << outbin << endl;
  }

  return 0;
}
