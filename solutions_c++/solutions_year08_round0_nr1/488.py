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

string names[101];
vector<int> qq;
map<string,int> mp;
 int s,q;
int t[1010][101];
int calc(int p, int se){
 int &ret = t[p][se];
 if(ret!=-1)return ret;
 if(qq.size()==p)return 0;
 ret=1<<30;
 REP(i,s){
  if(qq[p]!=i){
   ret<?=(i!=se)+calc(p+1,i);
  }
 }
 return ret;
}
int main(){
int nc;
cin>>nc;
int ic=1;
while(nc--){
 cin>>s;
 string ss;
 getline(cin,ss);
 mp.clear();
 REP(i,s){getline(cin,ss);names[i]=ss;mp[names[i]] = i;}
 cin>>q;
 getline(cin,ss);
 qq.clear();
 REP(i,q){
  getline(cin,ss);
  qq.PB(mp[ss]);
 }
 int ret=1<<30;
 CLEAR(t,-1);
 REP(i,s)ret<?=calc(0,i);
 cout<<"Case #"<<ic++<<": "<<ret<<endl;
}
}
