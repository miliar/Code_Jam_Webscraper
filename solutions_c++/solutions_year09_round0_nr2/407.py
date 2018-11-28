#include <iostream>
#include <vector>

using namespace std;

void answer();

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    cout<<"Case #"<<i<<":\n";
    answer();
  }
}

const int unseen=-1;
const pair<int,int> no_sink(-1,-1);

int sinks;
int search(const vector<vector<int> >& v,int x,int y,vector<vector<int> >& sink);

void check(const vector<vector<int> >& v,const vector<vector<int> >& sink,const vector<char>& name);

void answer(){
  int x,y;
  cin>>x>>y;
  vector<vector<int> > v(x,vector<int>(y)),sink(x,vector<int>(y,unseen));
  for(int i=0;i<v.size();i++)
    for(int j=0;j<v[i].size();j++)
      cin>>v[i][j];
  sinks=0;
  for(int i=0;i<v.size();i++)
    for(int j=0;j<v[i].size();j++)
      search(v,i,j,sink);
  vector<pair<int,int> > location(sinks,no_sink);
  for(int i=0;i<v.size();i++)
    for(int j=0;j<v[i].size();j++)
      if(location[sink[i][j]]==no_sink)
        location[sink[i][j]]=make_pair(i,j);
  sort(location.begin(),location.end());
  vector<char> name(location.size());
  for(int i=0;i<location.size();i++){
    pair<int,int> p=location[i];
    name[sink[p.first][p.second]]='a'+i;
  }
  check(v,sink,name);
  for(int i=0;i<sink.size();i++){
    for(int j=0;j<sink[i].size();j++){
      if(j) cout<<' ';
      cout<<name[sink[i][j]];
    }
    cout<<'\n';
  }
}

const int dirs=4;
const int dx[dirs]={-1,0,0,1};
const int dy[dirs]={0,-1,1,0};

bool good(const vector<vector<int> >& v,int x,int y){
  return x>=0 && y>=0 && x<v.size() && y<v[x].size();
}

int direction(const vector<vector<int> >& v,int x,int y){
  int lowest=v[x][y],ret=unseen;
  for(int d=0;d<dirs;d++){
    int nx=x+dx[d],ny=y+dy[d];
    if(!good(v,nx,ny))
      continue;
    if(v[nx][ny]>=lowest)
      continue;
    lowest=v[nx][ny];
    ret=d;
  }
  return ret;
}

int search(const vector<vector<int> >& v,int x,int y,vector<vector<int> >& sink){
  if(sink[x][y]!=unseen)
    return sink[x][y];
  int dir=direction(v,x,y);
  if(dir==unseen)
    return sink[x][y]=sinks++;
  int nx=x+dx[dir],ny=y+dy[dir];
  return sink[x][y]=search(v,nx,ny,sink);
}

void check(const vector<vector<int> >& v,const vector<vector<int> >& sink,const vector<char>& name){
  char seen='a'-1;
  for(int i=0;i<v.size();i++)
    for(int j=0;j<v[i].size();j++){
      char now=name[sink[i][j]];
      if(now>seen+1)
        assert(!"bad order!");
      if(now==seen+1) seen++;
      int dir=direction(v,i,j);
      if(dir!=unseen){
        int nx=i+dx[dir],ny=j+dy[dir];
        assert(sink[i][j]==sink[nx][ny]);
      }
    }
}
