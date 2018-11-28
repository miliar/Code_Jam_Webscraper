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
int readhour(){
 string s;
 cin>>s;
 int h=s[0]*10+s[1];
 int m=s[3]*10+s[4];
 return h*60+m;
}

int st[2][1001],end[2][1001];
int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 int T,na,nb;
 cin>>T>>na>>nb;
 priority_queue<pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > q;
 int reta=0,retb=0;
 int acta=0,actb=0;
 REP(i,na){
  st[0][i]=readhour();
  end[0][i]=readhour();
  q.push(MP(st[0][i],3));
  q.push(MP(end[0][i]+T,1));
 }
 REP(i,nb){
  st[1][i]=readhour();
  end[1][i]=readhour();
  q.push(MP(st[1][i],4));
  q.push(MP(end[1][i]+T,2));
 }
 while(!q.empty()){
  pair<int,int> p = q.top();q.pop();
  switch(p.Y){
   case 2:
    acta++;
    break;
   case 1:
    actb++;
    break;
   case 3:
    acta--;
    reta>?=-acta;
    break;
   case 4:
    actb--;
    retb>?=-actb;
    break;
  }
 }
 cout<<"Case #"<<ic++<<": "<<reta<<" "<<retb<<endl;
}
}
