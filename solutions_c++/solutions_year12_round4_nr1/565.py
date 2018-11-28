#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int key=0;

bool solve(const vector<pair<int,int> >& vines,int length);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int n,length;
    cin>>n;
    vector<pair<int,int> > vines(n+1);
    for(int j=1;j<vines.size();j++)
      cin>>vines[j].first>>vines[j].second;
    cin>>length;
    key++;
    cout<<"Case #"<<i+1<<": "<<(solve(vines,length)?"YES":"NO")<<'\n';
  }
}

bool memo(const vector<pair<int,int> >& vines,int at,int next,const int length);

bool solve(const vector<pair<int,int> >& vines,const int length){
  return memo(vines,0,1,length);
}

const int N=1000;
bool cache[N][N];
int cached[N][N];

bool memo(const vector<pair<int,int> >& vines,int at,int next,const int length){
  bool& ret=cache[at][next];
  if(cached[at][next]==key)
    return ret;
  cached[at][next]=key;
  int gap=min(vines[next].first-vines[at].first,vines[next].second);
  const int reach=vines[next].first+gap;
  if(reach>=length)
    return ret=true;
  for(int later=next+1;later<vines.size() && reach>=vines[later].first;later++)
    if(memo(vines,next,later,length))
      return ret=true;
  return ret=false;
}
