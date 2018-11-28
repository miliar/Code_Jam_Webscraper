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
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

int n;
Vi rightMost; // rightMost[r]=Rightmost one at row r
int main() {
  int nCases;
  cin >> nCases;
  forUp(cnr,nCases) {
    cin >> n;
    string s;
    getline(cin,s);
    rightMost=Vi(n);
    forUp(i,n) {
      getline(cin,s);
      for(int j=0; j<n; j++)
        if (s[j]=='1')
          rightMost[i]=j;
    }

//     disp(rightMost);

    int mn=1000000000;
    Vi p(n);
    forUp(i,n) p[i]=i;
    do {
      bool ok=true;
      forUp(i,n) if (rightMost[p[i]] > i) {
        ok=false;
        break;
      }
      if (ok) {
        int cnt=0;
        forUp(i,n) forUp(j,i)
          if (p[j]>p[i]) cnt++;
        mn=min(mn,cnt);
      }
    } while (next_permutation(p.begin(), p.end()));

    int res=mn;
    cout << "Case #" << cnr+1 << ": " << res << endl;
  }
  
  return 0;
}






