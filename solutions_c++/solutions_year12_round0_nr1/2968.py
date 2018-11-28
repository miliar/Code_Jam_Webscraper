#include <iostream>
#include <string>
#include <vector>

using namespace std;


#include <iostream>
#include <sstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <cmath>
#include <set>

typedef long long LL;
typedef vector<string> Vs;
typedef vector<int> Vi;
typedef vector<bool> Vb;
typedef vector<long long> Vll;
typedef vector<double> Vd;
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)


map<char,char> trans;
map<char,char> inv;

void learn(string plain, string tongue) {
  forUp(i, plain.size()) {
    assert(trans[plain[i]] == 0 or trans[plain[i]] == tongue[i]);
    trans[plain[i]] = tongue[i];
    inv[tongue[i]] = plain[i];
  }
}

string invert(string tongue) {
  string s = tongue;
  forUp(i, tongue.size()) {
    s[i] = inv[tongue[i]];
    assert(s[i] != 0);
  }
  return s;
}

int main() {
  freopen("a.in","r",stdin);

  learn("q", "z");
  learn("a zoo", "y qee");

  learn("our language is impossible to understand",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi");
  
  learn("there are twenty six factorial possibilities",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  
  learn("so it is okay if you want to just give up",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv");

  int T;
  cin >> T;
  string s;
  getline(cin, s);
  
  forUp(t, T) {
    string tongue;
    getline(cin, tongue);
    cout << "Case #" << t+1 << ": " << invert(tongue) << endl;
  }

  return 0;
}






