#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define rep(i,n) REP(i,0,n)
#define FOR(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ALLOF(c) (c).begin(), (c).end()
typedef long long ll;

map<string,string> cstr;
vector<string> dstr;
string str;

string solve(){
  string now = "";
  rep(i,str.length()){
    now += str[i];
    //cout << "now: " << now << endl;
    string pr = "";
    if(now.length()>=2){ pr += now[now.length()-1]; pr += now[now.length()-2]; }
    if(pr!="" && cstr.count(pr)>0){
      now = now.substr(0, now.length()-2) + cstr[pr];
    }else{
      rep(i,dstr.size()){
        char a = dstr[i][0], b = dstr[i][1], c = '*';
        if(now[now.length()-1]==a) c = b;
        else if(now[now.length()-1]==b) c = a;
        if(c!='*'){
          int idx = 0;
          while(idx<now.length()-1 && now[idx]!=c) idx++;
          if(idx==now.length()-1) continue;
          //now = now.substr(0,idx);
          now = "";
        }
      }
    }
  }
  stringstream ss("");
  ss << "[";
  rep(i,now.length()){
    ss << now[i];
    if(i!=now.length()-1) ss << ", ";
  }
  ss << "]";
  return ss.str();
}

int main(){
  int T;
  cin >> T;
  rep(t,T){
    cstr.clear();
    dstr.clear();
    int c, d, n;
    cin >> c;
    rep(i,c){
      string cc;
      cin >> cc;
      string a1 = "", a2 = "", a3 = "";
      a1 += cc[0]; a1 += cc[1];
      a2 += cc[1]; a2 += cc[0];
      a3 += cc[2];
      cstr[a1] = a3;
      cstr[a2] = a3;
    }
    cin >> d;
    rep(i,d){
      string dd;
      cin >> dd;
      dstr.push_back(dd);
    }
    cin >> n;
    cin >> str;

    cout << "Case #" << t+1 << ": " << solve() << endl;
  }
  return 0;
}
