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

string pat="welcome to code jam";

int main() {
  int patn=pat.size();
  int n;
  cin >> n;
  string s;
  getline(cin,s);
  forUp(t,n) {
    getline(cin,s);
    int sn=s.size();
    Mi C(patn, Vi(sn)); // C[i][j] = Ways to fit up to char i of
                          // pat ending it j'th char of s.

    forUp(i,patn) forUp(j,sn) {
      if (pat[i]==s[j]) {
        if (i==0)
          C[i][j] = 1;
        else
          forUp(k,j) 
            C[i][j] = (C[i][j] + C[i-1][k])%1000;
      }
    }

    int tot=0;
    forUp(j,sn) tot=(tot+C[patn-1][j])%1000;

    printf("Case #%d: %04d\n", t+1, tot);
  }
  return 0;
}






