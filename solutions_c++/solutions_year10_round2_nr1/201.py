#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cctype>
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define rep(var,n)  for(int var=0,lim=(n);var<lim;var++)
#define REP(var,ar)  for(int var=0,lim=(ar).size();var<lim;var++)
#define FOR(var,from,to) for(int var=(from),till=(to);var<=till;var++)
#define all(c)  (c).begin(),(c).end()

#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout.h"

vector<string> split(string str, int delim=' ')
{
  vector<string> result;

  const char *s = str.c_str();
  if (delim == ' ') {
    for (const char *p=s; *p; p++) {
      if (*p == delim) s++;
      else break;
    }
    if (!*s) return result;

    for (const char *p=s; *p; p++) {
      if (*p == delim) {
        if (s < p) {
          string a(s,p-s);
          result.push_back(a);
        }
        s = p + 1;
      }
    }
    if (*s) result.push_back(s);
  } else {
    for (const char *p=s; *p; p++) {
      if (*p == delim) {
        string a(s,p-s);
        result.push_back(a);
        s = p + 1;
        if (*s == '\0') result.push_back("");
      }
    }
    if (*s) result.push_back(s);
  }

  return result;
}

int main(){
  int T; cin >> T;
  rep(t,T){
    int N, M; cin >> N >> M;

    set<string> deja;
    
    rep(n,N){
      string name; cin >> name;
      vector<string> ns = split(name,'/');
      int nu=sz(ns)-1;
      for(int i=nu;i>=1;i--){
        string s="";
        rep(j,i){
          s += "/" + ns[1+j];
          deja.insert(s);
        }
      }
    }

    int ans = 0;
    rep(m,M){
      string name; cin >> name;
      vector<string> ns = split(name,'/');
      int nu=sz(ns)-1;
      for(int i=nu;i>=1;i--){
        string s="";
        rep(j,i){
          s += "/" + ns[1+j];
          if (found(deja,s)) {
            ;
          } else {
            ans++; deja.insert(s);
          }
        }
      }
    }
    printf("Case #%d: %d\n", t+1, ans);
  }
  return 0;
}
