#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "C-small-attempt0"

int field[501][501];

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int r;
          cin>>r;
          memset(field,0,sizeof(field));
          int X=0,Y=0;
          REP(i,r) {
               int x1,x2,y1,y2;
               cin>>x1>>y1>>x2>>y2;
               X=max(X,x2);
               Y=max(Y,y2);
               for(int x=x1;x<=x2;++x)
                    for(int y=y1;y<=y2;++y)
                         field[x][y]=1;
          }
          int res=0;
          bool done=false;
          while(!done) {
               done=true;
               for(int x=X+1;x>0;--x)
                    for(int y=Y+1;y>0;--y)
                         if(field[x-1][y]&&field[x][y-1]&&!field[x][y]) {
                              field[x][y]=1;
                              done=false;
                              X=max(x,X);Y=max(y,Y);
                         }
                         else if(!field[x-1][y]&&!field[x][y-1]&&field[x][y]) {
                              field[x][y]=0;
                              done=false;
                         }
               if(!done)++res;
          }
          cout<<"Case #"<<test<<": "<<res<<endl;
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
