#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

string ins[] = 
  {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
   "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

string outs[] = 
  {"our language is impossible to understand",
   "there are twenty six factorial possibilities",
   "so it is okay if you want to just give up"};

int main () {
  int test, T;

  int i,j;
  map<char, char> mapping;
  REP(i,3){
    string si=ins[i];
    string so=outs[i];
    int n=si.size();
    REP(j,n){
      mapping[si[j]] = so[j];
    }
  }
  mapping['z'] = 'q';
  mapping['q'] = 'z';

  cin >> T;
  string s;
  getline(cin, s);
  REP (test, T) {
    getline(cin, s);
    int n=s.size();
    REP(i,n){
      if(mapping[s[i]]){
        s[i]=mapping[s[i]];
      }else{
        //s[i]=s[i]-32;
        s[i]='?';
      }
    }
    gp(s);
  }
  return 0;
}

