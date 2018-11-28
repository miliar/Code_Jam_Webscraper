#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<string>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
bool check(vector<string> s, char c) {
  REP(i,4) {
    int ok=1;
    REP(j,4) if(s[i][j]!=c && s[i][j]!='T') ok =0;
    if(ok) return 1;
    ok=1;
    REP(j,4) if(s[j][i]!=c && s[j][i]!='T') ok =0;
    if(ok) return 1;
  }
  int a=1;
  REP(i,4) {
    if(s[i][i]!=c && s[i][i]!='T') a = 0;
  }
  if(a) return 1;
  a=1;
  REP(i,4) {
    if(s[i][3-i]!=c && s[i][3-i]!='T') a = 0;
  }
  return a;

}
string solve(vector<string> s) {
  int cnt=0;
  REP(i,4) REP(j,4) {
    cnt+=s[i][j]=='.';
  }
  if(check(s,'O')) return "O won";
  if(check(s,'X')) return "X won";

  
  
  if(cnt) {
    return "Game has not completed";
  } else {
    return "Draw";
  }


}
int main() {
int T;
cin>>T;
REP(tt,T) {
  vector<string> s(4);
  REP(i,4) cin>>s[i];
  cout<<"Case #"<<(tt+1)<<": "<<solve(s)<<endl;
}
}
// issue choosing small type
