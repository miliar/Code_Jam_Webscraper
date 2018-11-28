#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

int solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<solve()<<'\n';
}

const int infinity=999999999;

int solve(){
  int engines;
  string line;
  cin>>engines; getline(cin,line);
  vector<string> engine(engines);
  map<string,int> index;
  for(int i=0;i<engines;i++){
    getline(cin,engine[i]);
    index[engine[i]]=i+1;
  }
  vector<int> best(engines);
  int queries;
  cin>>queries; getline(cin,line);
  for(int i=0;i<queries;i++){
    getline(cin,line);
    int now=index[line];
    assert(now!=0);
    best[now-1]=infinity;
    int switcher= *min_element(best.begin(),best.end())+1;
    best[now-1]=switcher;
  }
  return *min_element(best.begin(),best.end());
}
