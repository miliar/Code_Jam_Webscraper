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

#define TEST_NAME "A-large"

VI getmask(int r,int c,vector<string> &field,char chr1,char chr2) {
     VI res(r);
     REP(i,r)REP(j,c)if(field[i][j]==chr1||field[i][j]==chr2)res[i]|=(1<<j);
     return res;
}

bool stable(VI s,int r,int c) {
     VVI seen(r,VI(c));
     queue<PII> q;
     int cnt=0;
     PII d[4]={PII(1,0),PII(-1,0),PII(0,1),PII(0,-1)};
     REP(i,r)REP(j,c)
          if(!seen[i][j]&&(s[i]&(1<<j))) {
               ++cnt;
               seen[i][j]=true;
//                cerr<<"see "<<i<<" "<<j<<endl;
               q.push(PII(i,j));
               while(!q.empty()) {
                    int x=q.front().X,y=q.front().Y,x2,y2;q.pop();
                    REP(dir,4) {
                         x2=x+d[dir].X;
                         y2=y+d[dir].Y;
                         if(x2>=0&&x2<r&&y2>=0&&y2<c&&(s[x2]&(1<<y2))&&!seen[x2][y2]) {
//                               cerr<<" -> "<<x2<<" "<<y2<<endl;
                              seen[x2][y2]=true;
                              q.push(PII(x2,y2));
                         }
                    }
               }
          }
     return cnt<=1;
}
bool intersect(const VI &a,const VI &b) {
     REP(i,SZ(a))if(a[i]&b[i])return true;
     return false;
}
#define OK(a,i,j) ((a[i])&(1<<j))

set<VI> seen;
queue<pair<VI,int> > q;

VI bad;
bool fromstable;
int r,c;

inline void relax(const VI &from,int d) {
//      cout<<"->";REP(i,SZ(from))cout<<from[i]<<" ";cout<<endl;
     if((fromstable||stable(from,r,c))&&!intersect(from,bad)&&!seen.count(from)) {
          seen.insert(from);
          q.push(make_pair(from,d));
     }
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int n,test;
	
     for(cin>>n,test=1;test<=n;++test) {
          cin>>r>>c;
          vector<string> field(r);
          REP(i,r)cin>>field[i];
          VI from=getmask(r,c,field,'o','w');
          VI to=getmask(r,c,field,'x','w');
          bad=getmask(r,c,field,'#','#');
          
          seen.clear();
          q=queue<pair<VI,int> >();
          
          seen.insert(from);
          q.push(make_pair(from,0));
          int res=-1;
          
          while(!q.empty()) {
               from=q.front().X;
               int d=q.front().Y;
               q.pop();

//                REP(i,SZ(from))cout<<from[i]<<" ";cout<<endl;
               
               fromstable=stable(from,r,c);
//                cout<<"stable="<<fromstable<<endl;
//                return 0;
               if(from==to) {
                    res=d;
                    break;
               }
               REP(i,r) 
                    FOR(j,1,c-1)if(!OK(from,i,j-1)&&OK(from,i,j)&&!OK(from,i,j+1)&&
                                   !OK(bad,i,j-1)&&               !OK(bad,i,j+1)) {
                    from[i]&=~(1<<j);
                    
                    from[i]|=(1<<j-1);
                    relax(from,d+1);
                    from[i]&=~(1<<j-1);

                    from[i]|=(1<<j+1);
                    relax(from,d+1);
                    from[i]&=~(1<<j+1);

                    from[i]|=(1<<j);
               }
               FOR(i,1,r-1)
                    REP(j,c)if(!OK(from,i-1,j)&&OK(from,i,j)&&!OK(from,i+1,j)&&
                                   !OK(bad,i-1,j)&&               !OK(bad,i+1,j)) {
                    from[i]&=~(1<<j);
                    
                    from[i-1]|=(1<<j); 
                    relax(from,d+1);
                    from[i-1]&=~(1<<j);

                    from[i+1]|=(1<<j);
                    relax(from,d+1);
                    from[i+1]&=~(1<<j);

                    from[i]|=(1<<j);
               }                    
          }
          printf("Case #%d: %d\n",test,res);
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
