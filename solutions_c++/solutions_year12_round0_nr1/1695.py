#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>

using namespace std;
#define pb         push_back
#define all(a)     (a).begin(),(a).end()
#define sz(a)      (int)((a).size())
#define rep(i,n)   for(int i=0; i<n; ++i)
#define REP(i,j,k) for(int i=j; i<k; ++i)
typedef long long ll;
string c = "yhesocvxduiglbkrztnwjpfmaq";
int main () {
  int TC; scanf("%d", &TC);
  string s;
  getline(cin, s);
  rep (tc, TC) {
    getline(cin, s);
    if (s[sz(s)-1] < 'a') s.erase(sz(s)-1, 1);
    rep (i, sz(s)) if (s[i] != ' ') s[i] = c[s[i]-'a'];
    cout << "Case #" << tc+1 << ": " << s << endl;
  }
  return 0;
}
