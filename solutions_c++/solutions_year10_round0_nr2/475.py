#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

bool small(const string& s1, const string& s2) {
  if (s1.length() != s2.length())
    return s1.length() < s2.length();
  return s1 < s2;
}

void trim_lead(string& s1) {
  if (s1[0] == '0') {
    int i = 0;
    while (i < s1.length()-1 && s1[i] == '0') ++i;
    s1 = s1.substr(i);
  }
}

string myminus(string s1, const string& s2) {
  if (s1 == s2) return "0";
  int k = 0;
  int i = s1.length() - 1;
  for (int j = s2.length()-1; j >= 0; --j) {
    k = k + s1[i] - s2[j];
    if (k < 0) {
      s1[i] = '0' + 10 + k;
      k = -1;
    } else {
      s1[i] = '0' + k;
      k = 0;
    }
    --i;
  }
  while (k != 0) {
    if (s1[i] == '0')
      s1[i] = '9';
    else {
      --s1[i];
      k = 0;
    }
    --i;
  }
  trim_lead(s1);
  return s1;
}

string mod(const string& s1, const string& s2) {
  if (small(s1, s2)) return s1;
  int n = s2.length();
  int r = s1.length() - n;
  string sub1 = s1.substr(0, n);
  while (1) {
    while (!small(sub1, s2)) {
      sub1 = myminus(sub1, s2);
    }
    if (r == 0) break;
    sub1 += s1[s1.length()-r];
    trim_lead(sub1);
    --r;
  }
  return sub1;
}

string gcd(const string& s1, const string& s2) {
  if (s2 == "0") return s1;
  if (s1 == "0") return s2;
  return gcd(s2, mod(s1, s2));
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
          int n;
          string a[1000];
          fin >> n;
          for (int i = 0; i < n; ++i) fin >> a[i];
          for (int i = 0; i < n; ++i)
            for (int j = i+1; j < n; ++j)
              if (small(a[j], a[i]))
                swap(a[i], a[j]);
          string d = myminus(a[n-1], a[n-2]);
          for (int i = n-3; i >= 0; --i) {
            string d1 = myminus(a[i+1], a[i]);
            d = gcd(d1, d);
          }
          string ans = mod(a[0], d);
          if (ans != "0") ans = myminus(d, ans);
          fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
