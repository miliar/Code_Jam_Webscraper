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

#define TEST_NAME "B-small-attempt1"

struct pqel {
     int r,c1,c2,d;
     pqel(int r=0,int c1=0,int c2=0,int d=0):r(r),c1(c1),c2(c2),d(d) {}
     bool operator<(const pqel &q)const {return d>q.d;}
};

int dist[55][55][55];

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int n,test;
	
     for(cin>>n,test=1;test<=n;++test) {
          int r,c,f;
          cin>>r>>c>>f;
          vector<string> field(r);
          REP(i,r)cin>>field[i];
          REVERSE(field);
          REP(i,r)REP(c1,c)FOR(c2,c1,c)dist[i][c1][c2]=INF;
          priority_queue<pqel> pq;
          dist[r-1][0][c-1]=0;
          int ri,c1,c2,d;
          c1=0;c2=0;ri=r-1;d=0;
          while(c2+1<c&&field[ri][c2+1]=='.'&&(ri==0||field[ri-1][c2+1]=='#'))++c2;
          dist[ri][c1][c2]=0;
          pq.push(pqel(ri,c1,c2,0));
          int ans=INF;
          int rri,cc1,cc2,dd;
//           FORD(i,r-1,0)cerr<<field[i]<<endl;
          while(!pq.empty()) {
               ri=pq.top().r;c1=pq.top().c1;c2=pq.top().c2;d=pq.top().d;pq.pop();
               if(d!=dist[ri][c1][c2])continue;
//                printf("ri=%d c1=%d c2=%d d=%d\n",ri,c1,c2,d);
               if(ri==0) {ans=d;break;}
               int beg=c1,end=c2;
               if(field[ri-1][beg]=='.')++beg;
               if(field[ri-1][end]=='.')--end;
               for(int x=max(0,beg-1);x<=min(c-1,end+1);++x) {
                    if((field[ri][x]=='.'||x>=c1&&x<=c2)&&!(x==beg&&end==beg)) {
                         for(rri=ri-1;rri>0&&field[rri-1][x]=='.';--rri);
//                          cout<<"->"<<x<<" ri="<<ri<<" rri="<<rri<<endl;                         
                         if(ri-rri<=f) {
                              cc1=x;cc2=x;dd=d;
                              if(field[ri-1][x]=='#')dd++;
                              while(cc1>0&&field[rri][cc1-1]=='.'&&(rri==0||field[rri-1][cc1-1]=='#'))--cc1;
                              while(cc2+1<c&&field[rri][cc2+1]=='.'&&(rri==0||field[rri-1][cc2+1]=='#'))++cc2;
//                               printf("field[%d][%d]=%c\n",rri-1,x,field[rri-1][x]);
//                               printf("->rri=%d cc1=%d cc2=%d dd=%d\n",rri,cc1,cc2,dd);               
                              if(dist[rri][cc1][cc2]>dd) {
                                   dist[rri][cc1][cc2]=dd;
                                   pq.push(pqel(rri,cc1,cc2,dd));
                              }
                         }
                    }
               }
               FOR(x,beg,end+1) {
                    cc1=x;dd=d;
                    FOR(y,x,end+1) {
                         if(x==beg&&y==end)continue;
                         rri=ri-1;cc1=x;cc2=y;
                         if(field[ri-1][y]=='#')++dd;
                         while(cc1>0&&field[rri][cc1-1]=='.'&&(rri==0||field[rri-1][cc1-1]=='#'))--cc1;
                         while(cc2+1<c&&field[rri][cc2+1]=='.'&&(rri==0||field[rri-1][cc2+1]=='#'))++cc2;
                         if(x+1>=y&&ri>=2&&field[ri-2][x]=='.'&&field[ri-2][y]=='.') {
                         }
                         else {
                              if(dist[rri][cc1][cc2]>dd) {
//                                    printf("->rri=%d cc1=%d cc2=%d dd=%d\n",rri,cc1,cc2,dd);                             
                                   dist[rri][cc1][cc2]=dd;
                                   pq.push(pqel(rri,cc1,cc2,dd));
                              }
                         }
                         if(ri>=2&&field[ri-2][y]!='#'&&y==x)continue;
                         if(ri>=2&&field[ri-2][y]!='#')break;
                    }
               }
          }

          printf("Case #%d: ",test);
          if(ans==INF)printf("No\n");
          else printf("Yes %d\n",ans);          
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
