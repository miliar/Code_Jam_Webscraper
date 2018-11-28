#include <iostream>
#include <sstream>
#include <cstring>
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


void printregel(vi S, int w) {
  vi now;
  for(int i=0;i<20;i++) if(w&(1<<i)) now.pb(S[i]);
  for(int i=0;i<sz(now);i++)
    printf("%d%c",now[i],(i==sz(now)-1)?'\n':' ');
}


int main()
{
  int i,j,k,l; char buf[1000];
  int keeses; scanf("%d",&keeses);

  for(int kees=1;kees<=keeses;kees++) {
    int z; scanf("%d",&z);
    vi S(20);
    for(j=0;j<20;j++) scanf("%d",&S[j]);
    bool done=false;
    map<int, int> M;
    for(int s=1;s<(1<<20);s++) {
      int som=0;
      for(j=0;j<20;j++) if(s&(1<<j))
        som+=S[j];
      if(M.find(som)!=M.end()) {
        printf("Case #%d:\n",kees);
        printregel(S,s);
        printregel(S,M[som]);
//printf("[%d->%d]",s,som);
        done=true;
        break;
      } else M[som]=s;

    }
    if(!done) printf("Impossible\n");







  }



  return 0;
}
