//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define LL long long
#define ST first
#define ND second
#define PII pair<int,int>
#define VI vector<int>
#define PCC pair<char,char>
using namespace std;
int t,n,cnum,onum,dlen;
char m[10];
char s[110];
map < pair<char,char>, char > comb;
map < char, char > opp;
vector <char> d;
int main() {
  scanf("%d",&t);
  for(int i = 1; i <= t; i++) {
    comb.clear(); opp.clear();  d.clear();
    scanf("%d",&cnum);
    for(int j = 1; j <= cnum; j++) {
      scanf("%s",m);
      comb[PCC(m[0],m[1])] = m[2];
      comb[PCC(m[1],m[0])] = m[2];
    }
    scanf("%d",&onum);
    for(int j = 1; j <= onum; j++) {
      scanf("%s",&m);
      opp[m[0]] = m[1];
      opp[m[1]] = m[0];
    }
    scanf("%d",&dlen);
    scanf("%s",s);
    d.push_back(s[0]);

    for(int j = 1; j < dlen; j++) {
      d.push_back(s[j]);
      int ok = 1;
      while(ok) {
	ok = 0;
	if(d.size() > 1 &&  comb.find(PCC(d[d.size()-1],d[d.size()-2])) != comb.end() ) {
	d[d.size()-2] = comb[PCC(d[d.size()-1],d[d.size() - 2])];
	d.pop_back();
	ok = 1;
      }
	else if(d.size() > 1 && comb.find(PCC(d[d.size()-2],d[d.size()-1])) != comb.end() ) {
	d[d.size() -2] = comb[PCC(d[d.size()-2],d[d.size()-1])];
	d.pop_back();
	ok = 1;
      }
      else {
	for(int k = 0; k < d.size(); k++) {
	  if(opp.find(d[k]) != opp.end() ) {
	    if(opp[d[k]] == d[d.size()-1]) d.clear();
	  }
	}
      }
      }
    }
    if(d.size() > 0) {
    printf("Case #%d: [",i);
    for(int k = 0; k < d.size() - 1; k++)
      printf("%c, ",d[k]);
    printf("%c]\n",d[d.size()-1]);
    }
    else printf("Case #%d: []\n",i);
  }
  


  return 0;
}
