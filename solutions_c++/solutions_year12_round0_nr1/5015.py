#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())



int main()
{
  int i,j,k=0; char buf[10000];

  string from = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string to = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

  string mapping(26,' ');
  for(j=0;j<sz(from);j++) if(from[j]!=' ') mapping[from[j]-'a']=to[j];
  mapping[16]='z';
  mapping[25]='q';

  gets(buf);
  sscanf(buf,"%d",&k);
  for(j=1;j<=k;j++) {
    printf("Case #%d: ",j);
    gets(buf);
    for(i=0;buf[i];i++) {
      char c=buf[i];
      if(c!=' ') c=mapping[c-'a'];
      printf("%c",c);
    }
    printf("\n");
  }

  return 0;
}
