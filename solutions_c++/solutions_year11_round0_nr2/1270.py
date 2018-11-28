#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<char> answer();
void print(const vector<char>& s);

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": ";
    print(answer());
    cout<<'\n';
  }
}

void invoke(char invoked,vector<char>& summoned,map<char,vector<pair<char,char> > >& combine,map<char,int>& remove);
map<char,vector<pair<char,char> > > read_combine();
map<char,int> read_remove();

vector<char> answer(){
  map<char,vector<pair<char,char> > > combine=read_combine();
  map<char,int> remove=read_remove();
  int n;
  cin>>n;
  vector<char> summoned;
  for(int i=0;i<n;i++){
    char invoked;
    cin>>invoked;
    invoke(invoked,summoned,combine,remove);
  }
  return summoned;
}

void invoke(char invoked,vector<char>& summoned,map<char,vector<pair<char,char> > >& combine,map<char,int>& remove){
  summoned.push_back(invoked);
  if(summoned.size()<2)
    return;
  vector<pair<char,char> >& v=combine[invoked];
  for(int i=0;i<v.size();i++)
    if(summoned[summoned.size()-2]==v[i].first){
      summoned.pop_back();
      summoned.back()=v[i].second;
      return;
    }
  int bad=remove[invoked];
  for(int i=0;i<summoned.size();i++)
    if(bad&(1<<(summoned[i]-'A'))){
      summoned.clear();
      return;
    }
}

map<char,vector<pair<char,char> > > read_combine(){
  int n;
  cin>>n;
  map<char,vector<pair<char,char> > > ret;
  for(int i=0;i<n;i++){
    char b,bb,result;
    cin>>b>>bb>>result;
    ret[b].push_back(make_pair(bb,result));
    ret[bb].push_back(make_pair(b,result));
  }
  return ret;
}

map<char,int> read_remove(){
  int n;
  cin>>n;
  map<char,int> ret;
  for(int i=0;i<n;i++){
    char b,bb;
    cin>>b>>bb;
    ret[b]|=1<<(bb-'A');
    ret[bb]|=1<<(b-'A');
  }
  return ret;
}

void print(const vector<char>& v){
  cout<<'[';
  for(int i=0;i<v.size();i++){
    if(i)
      cout<<", ";
    cout<<v[i];
  }
  cout<<']';
}
