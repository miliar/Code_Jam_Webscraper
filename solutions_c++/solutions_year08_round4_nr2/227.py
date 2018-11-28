#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define LET(i,c) typeof(c) i = (c)
#define MP make_pair
#define PB push_back
#define SORT(x) sort((x).begin(),(x).end())
#define ALL(x) (x).begin(),(x).end()
#define UNIQUE(x) remove(unique((x).begin(),(x).end()),(x).end())
#define CLEAR(x,v) memset((x),(v),sizeof((x)))
#define FORS(i,x) for(int i=0;i<(int)(x).size();i++)
#define X first
#define Y second
typedef long long ent;

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 int n,m,a;
 cin>>n>>m>>a;
 int v=0;
 for(int x1=-n;x1<=n;x1++)for(int y1=-m;y1<=m;y1++){
  for(int x2=-n;x2<=n;x2++)for(int y2=-m;y2<=m;y2++){
   if(abs(x1*y2 - x2*y1) == a){
    if(max(max(x1,x2),0)-min(min(x1,x2),0)<=n && max(max(y1,y2),0)-min(min(y1,y2),0)<=m){
     int ox = min(min(x1,x2),0);
     int oy = min(min(y1,y2),0);
     cout<<"Case #"<<ic++<<": "<<-ox<<" "<<-oy<<" "<<x1-ox<<" "<<y1-oy<<" "<<x2-ox<<" "<<y2-oy<<endl;
     v=1;
     goto done;
    }
   }
  }
 }
 done:
 if(!v)cout<<"Case #"<<ic++<<": IMPOSSIBLE"<<endl;
}
return 0;
}
