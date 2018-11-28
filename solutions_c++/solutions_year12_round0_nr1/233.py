#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#include "cout.h"

const char* tr[4][2] = {
  {"y qee",
   "a zoo"},
  {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
   "our language is impossible to understand"},
  {"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
   "there are twenty six factorial possibilities"},
  {"de kr kd eoya kw aej tysr re ujdr lkgc jv",
   "so it is okay if you want to just give up"} };

int main(){
  map<char,char> mp;
  vector<bool> v(256,false);
  rep(i,4){
    int l=strlen(tr[i][0]);
    rep(j,l){
      char c2 = tr[i][0][j], c1 = tr[i][1][j];
      //if (c1 == ' ') continue;
      if (found(mp,c1)) {
        //if (mp[c1] != c2) printf("%d %d %c: %c != %c\n", i,j,c1, mp[c1],c2);
      } else {
        mp[c1] = c2;
        v[c2] = true;
      }
    }
  }
  char unk;
  rep(i,26) if(!v['a'+i]) unk='a'+i;// printf("(%c) not found.\n", 'a'+i);
  map<char,char> rev;
  for (char c='a'; c<='z'; c++) {
    if (found(mp,c)){
      if (found(rev,mp[c])) {
        printf("%c =>> %c,%c\n", mp[c],rev[mp[c]],c);
        rev[mp[c]] = c;
      } else {
        //printf("%c =>> %c\n", mp[c],c);
        rev[mp[c]] = c;
      }
    } else {
      //printf("%c => ??? => %c\n", c,unk);
      mp[c] = unk;
      rev[unk] = c;
    }
  }
  rev[' '] = ' ';

  //return 0;
  char buf[256];
  gets(buf);
  int _T = atoi(buf);
  rep(_t,_T){
    printf("Case #%d: ", 1+_t);

    gets(buf);
    int l=strlen(buf);
    rep(i,l) {
      char c=buf[i];
      if (found(rev,c)) putchar(rev[c]);
      else putchar('*'); //printf("(%c)", c);
    }
    putchar('\n');
  }
}
