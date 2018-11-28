#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<cassert>
#include<climits>
using namespace std;

#define REP(i,n) for(int i=0, _e(n); i<_e; i++)
#define FOR(i,a,b) for(int i(a), _e(b); i<=_e; i++)
#define FORD(i,a,b) for(int i(a), _e(b); i>=_e; i--) 
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )

#define sz size()
#define pb push_back
#define VI vector<int>
#define VS vector<string>
#define x first
#define y second

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

#define D(x) if(1) cout << __LINE__ <<" "<< #x " = " << (x) << endl;
#define D2(x,y) if(1) cout << __LINE__ <<" "<< #x " = " << (x) \
   <<", " << #y " = " << (y) << endl;

char transf[255][255];
char destroy[255][255];

int main()
{
  int t;scanf("%d",&t);
  REP (__,t) {
    SET(transf,0);
    SET(destroy,0);
    int C; scanf("%d",&C);
    REP (i,C) {
      char str[10]; scanf("%s",str);
      transf[ str[0] ][ str[1] ] = str[2];
      transf[ str[1] ][ str[0] ] = str[2];
    }
    int D; scanf("%d",&D);
    REP (i,D) {
      char str[10]; scanf("%s",str);
      destroy[ str[0] ][ str[1] ] = 1;
      destroy[ str[1] ][ str[0] ] = 1;
    }

    int n; scanf("%d",&n);
    char str[1000]; scanf("%s", str);
    vector<char> out;
    for(int i=0;i<n;i++) {
      out.push_back(str[i]);

      if (i>0) {
        char tr = transf[ out[out.sz-1] ][out[out.sz-2]];
        if (tr) {
          out.pop_back();
          out.pop_back();
          out.push_back(tr);
          continue;
        }
      }

      REP (j,out.size()-1) {
        if (destroy[ out[j] ][ out[out.sz-1] ]) {
          out.resize(0);
          break;
        }
      }
    }

    printf("Case #%d: [", __+1);
    if(out.sz) {
      printf("%c", out[0]);
      FOR (i,1,int(out.size())-1) {
        printf(", %c", out[i]);
      }
    }
    printf("]\n");
  }
  
  return 0;
}

