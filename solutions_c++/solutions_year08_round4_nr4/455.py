#include<cstdio>
#include<string>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
#include<sstream>

using namespace std;

#define pf printf
#define sf scanf
#define co continue
#define re return
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

string change(string a, vector<int> v) {
  string s = "";
  int i;
  for(i=0;i<a.size();i++)
    s += a[ v[i] - 1];
  return s;
}

int per(string s) {
    int cnt = 1;
    int i;
    for(i=1;i<s.size();i++)
      if( s[i] != s[i-1] ) cnt++;
    re cnt;
}

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int t;
    int cases = 1;
    for( sf("%d", &t); t--;  ) {
      int k;
      char str[2000];
      sf("%d", &k);
      sf("%s", str);
      string s = str;
      vector<int> v; v.clear();
      int i;
      for(i=1;i<=k;i++) {
        v.pb(i);
      }
      int res = 1000000000;
      do
      {
       string ss = s;
       string P = "";
       for(i=0;i<ss.size();i+=k) {
         P += change(ss.substr(i, k), v);
       }
       res <?= per(P);
      }while( next_permutation(v.begin(), v.end() ) );
      pf("Case #%d: %d\n", cases++, res);
    }
    return 0;
}

