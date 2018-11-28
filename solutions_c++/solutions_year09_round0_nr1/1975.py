#include <iostream>
#include <sstream>
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

using namespace std;

typedef long long LL;
typedef vector<string> Vs;
typedef vector<int> Vi;
typedef vector<bool> Vb;
typedef vector<long long> Vll;
typedef vector<double> Vd;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

int main() {
  int l,d,n;
  cin >> l >> d >> n;
  Vs dic(d);
  forUp(i,d)
    cin >> dic[i];
  forUp(i,n) {
    string s;
    cin >> s;
    vector<set<char> > toks(l);
    int t=0;
    bool var=false;
    forEach(c,s)
      if (c=='(') var=true; 
      else if (c==')') {t++; var=false;}
      else if (islower(c)) {
        toks[t].insert(c);
        if (!var) t++;
      }
    int cnt=0;
    forUp(j,d) {
      bool ok=true;
      forUp(t,l)
        if (!toks[t].count(dic[j][t])) ok=false;
      if (ok) cnt++;
    }
      
    cout << "Case #" << i+1 << ": " << cnt << endl;
  }
  return 0;
}






