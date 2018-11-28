#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

#define CLEAR(X) memset(X,0,sizeof(X))
#define REP(i,n) for(int i=0;i<(n);i++) 
template <class T> vector<T>parse(string s,const char d=' '){
  vector<T> v; string p; s+=d; int i=0; 
  while(i<(int)s.size())
    if (s[i] == d){stringstream u; u<<p; T t; u>>t; v.push_back(t); p=""; while(i<(int)s.size() && s[i]==d)i++;} else p+=s[i++];   
  return v;
} 

typedef long long ll;
typedef long double ld;

char a[10][10];

bool won(char s) {
  REP(i,4) {
    bool all = true;
    REP(j,4)
      if (!(a[i][j] == s || a[i][j]=='T')) all = false;
    if (all)return true;
  }

  REP(i,4) {
    bool all = true;
    REP(j,4)
      if (!(a[j][i] == s || a[j][i]=='T')) all = false;
    if (all)return true;
  }
  bool all = true;
  REP(j,4)
    if (!(a[j][j] == s || a[j][j]=='T')) all = false;
  if (all)return true;

  all = true;
  REP(j,4)
    if (!(a[3-j][j] == s || a[3-j][j]=='T')) all = false;
  if (all)return true;
  return false;

}

int main(){
  int _cases; scanf("%d",&_cases);
  for(int _case=1;_case<=_cases;_case++){
    printf("Case #%d:",_case);
    REP(i,4)scanf("%s",a[i]);
    bool full = true;
    REP(i,4)REP(j,4)if(a[i][j]=='.')full=false;
    if (won('X')) printf(" X won");
    else if (won('O')) printf(" O won");
    else if(full) printf(" Draw");
    else printf(" Game has not completed");
    printf("\n");


  }
  return 0;
}
