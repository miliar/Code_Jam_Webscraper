#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

#define INF 1000000000
int r,n;
main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    cin>>n;
    typedef pair<int,int> p2;
    set<p2> s;
    FOR(i,n){
      int x0,x1,y0,y1;
      cin>>x0>>y0>>x1>>y1;
      for(int x=x0;x<=x1;x++)for(int y=y0;y<=y1;y++)s.insert(p2(x,y));
    }
    r=0;
    while(s.size()){
      r++;
      set<p2> ss;
      FOREACH(iter,s){
        int x=iter->first,y=iter->second;
        if(s.count(p2(x-1,y))||s.count(p2(x,y-1)))ss.insert(p2(x,y));
        if(s.count(p2(x-1,y+1)))ss.insert(p2(x,y+1));
        if(s.count(p2(x+1,y-1)))ss.insert(p2(x+1,y));        
      }
      swap(s,ss);
    }
    cout<<"Case #"<<c<<": "<<r<<endl;
  }
}
