#include <iostream>
#include <vector>

using namespace std;

const int unseen=-1,bad=-2;

int solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<solve()<<'\n';
}

const int dirs=2;
const int dx[dirs]={1,2};
const int dy[dirs]={2,1};

const int MOD=10007;

int add(int a,int b){
  return (a+b)%MOD;
}

int memo(vector<vector<int> >& v,int x,int y){
  if(v[x][y]==bad) return 0;
  if(v[x][y]!=unseen) return v[x][y];
  int& ret=v[x][y]=0;
  if(x+1==v.size() && y+1==v[x].size())
    return ret=1;
  for(int i=0;i<dirs;i++){
    int nx=x+dx[i],ny=y+dy[i];
    if(nx<v.size() && ny<v[x].size())
      ret=add(ret,memo(v,nx,ny));
  }
  return ret;
}

int solve(){
  int X,Y,r;
  cin>>X>>Y>>r;
  vector<vector<int> > v(X+1,vector<int>(Y+1,unseen));
  for(int i=0;i<r;i++){
    int x,y;
    cin>>x>>y;
    v[x][y]=bad;
  }
  return memo(v,1,1);
}
