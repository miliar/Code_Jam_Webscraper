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
 int k;cin>>k;
 string s;
 cin>>s;
 vector<int> p;
 for(int i=0;i<k;i++)p.PB(i);
 int best=1<<30;
 do{
  string ss=s;
  for(int i=0;i<s.size();i++){
   ss[i] = s[(i/k)*k + p[i%k]];
  }
  int dif=0;
  int ch = '&';
  FORS(i,s){
   if(ch!=ss[i]){
    ch=ss[i];dif++;
   }
  }
  best<?=dif;
 }while(next_permutation(ALL(p)));
 cout<<"Case #"<<ic++<<": "<<best<<endl;
}
return 0;
}
