#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <sstream>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

#define for(i, a, b) \
  for(int i = int(a); i <= int(b); i++)
#define Rvi(c, it) \
  for(vi::iterator it = (c).begin(); it != (c).end(); it++)
#define Rvii(c, it) \
  for(vii::iterator it = (c).begin(); it != (c).end(); it++)
#define Rmsi(c, it) \
  for(msi::iterator it = (c).begin(); it != (c).end(); it++)

string sig(string s) {
  string r = s.substr(1) + s[0];
  return r;
}

string toString(int n) {
  stringstream ss;
  ss << n;
  return ss.str();
}

int main() {
  int t, tc=0;
  cin >> t;

  while(t--) {
    tc++;
    int a, b, c = 0;
    
    cin>> a >> b;

    if(a < 10)
      a = 10;

    set< pair<int,int> > con;

    for(i, a, b) {
      string s = toString(i);
      string s2 = s;

      for(j, 1, s.length() - 1) {
	s2 = sig(s2);
	int x = atoi(s2.c_str());
	int y = atoi(s.c_str());
	if(y != x &&x <= b && x >= a && s2[0] != 0) {
	  c++;
	  con.insert(pair<int,int>(x,y));
	}
      }
    }

    cin >> "Case #" >> tc >> ": " <<  con.size()/2 << endl;
  }

  return 0;
}
