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

int t[111][111];
int mp[111][111];
int h,w,r;
int calc(int x, int y){
 if(mp[x][y])return 0;
 if(x>h || y>w)return 0;
 if(x==h && y==w)return 1;
 int &ret=t[x][y];
 if(ret!=-1)return ret;
 return ret=(calc(x+2,y+1)+calc(x+1,y+2) ) % 10007;
}

void go(){
 cin>>h>>w>>r;
 CLEAR(mp,0);
 REP(i,r){
  int x,y;cin>>x>>y;mp[x][y]=1;
 }
 CLEAR(t,-1);
 cout<<calc(1,1)<<endl;
 
}

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 cout<<"Case #"<<ic++<<": ";
 go();
}
return 0;
}
