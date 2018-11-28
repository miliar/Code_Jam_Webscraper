#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <cassert>

using namespace std;

void solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<":\n";
    solve();
  }
}

void solve(const vector<string> v,int x,int y);

void solve(){
  int x,y;
  cin>>x>>y;
  vector<string> v(x);
  for(int i=0;i<x;i++)
    cin>>v[i];
  for(int i='0';i<='9';i++)
    for(int j=0;j<v.size();j++)
      for(int k=0;k<v[j].size();k++)
        if(v[j][k]==i)
          solve(v,j,k);
}

const int dirs=3;
const int dx[dirs]={0,0,1};
const int dy[dirs]={1,-1,0};

set<pair<int,int> > traceable(const vector<string>& v,int sx,int sy){
  set<pair<int,int> > ret;
  int x=sx,y=sy;
  queue<pair<int,int> > q;
  ret.insert(make_pair(sx,sy));
  q.push(make_pair(sx,sy));
  while(q.size()){
    pair<int,int> current=q.front();
    q.pop();
    int x=current.first,y=current.second;
    for(int d=0;d<dirs;d++){
      int nx=x-dx[d],ny=y-dy[d];
      pair<int,int> next(nx,ny);
      if(v[nx][ny]!='#' && ret.find(next)==ret.end()){
        q.push(next);
        ret.insert(next);
      }
    }
  }
  return ret;
}

set<set<pair<int,int> > > seen; 

set<pair<int,int> > move(const vector<string>& v,int cx,set<pair<int,int> > possible,int d){
  set<pair<int,int> > next,bad;
  for(set<pair<int,int> >::iterator i=possible.begin();i!=possible.end();i++){
    pair<int,int> now=*i;
    pair<int,int> later(now.first+dx[d],now.second+dy[d]);
    if(v[later.first][later.second]=='#')
      later=now;
    if(later.first>cx)
      return bad;
    next.insert(later);
  }
  return next;
}

void print(const string& st,set<pair<int,int> > s){
  cout<<st<<": ";
  for(set<pair<int,int> >::iterator i=s.begin();i!=s.end();i++)
    cout<<i->first<<','<<i->second<<' ';
  cout<<'\n';
}

bool lucky(const vector<string>& v,int cx,int cy,set<pair<int,int> > possible){
  if(possible.size()==1 && possible.find(make_pair(cx,cy))!=possible.end())
      return true;
  if(seen.find(possible)!=seen.end())
    return false;
  seen.insert(possible);
  //print("checking set",possible);
  for(int d=0;d<dirs;d++){
    set<pair<int,int> > next=move(v,cx,possible,d);
    if(next.size()==0)
      continue;
    if(lucky(v,cx,cy,next))
      return true;
  }
  return false;
}

void solve(const vector<string> v,int cx,int cy){
  set<pair<int,int> > tr=traceable(v,cx,cy);
  seen.clear();
  cout<<v[cx][cy]<<": "<<tr.size()<<' '<<(lucky(v,cx,cy,tr)?"Lucky":"Unlucky")<<'\n';
}
