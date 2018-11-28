#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

long long answer();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<answer()<<'\n';
}

pair<int,long long> ride(int seats,const vector<int>& groups,int g); 
vector<pair<int,long long> > twice(const vector<pair<int,long long> >& transition);

long long answer(){
  int rides,seats,groups;
  cin>>rides>>seats>>groups;
  vector<int> group(groups);
  for(int i=0;i<group.size();i++)
    cin>>group[i];
  long long total=accumulate(group.begin(),group.end(),0LL);
  if(total<=seats)
    return rides*total;
  vector<pair<int,long long> > transition(groups);
  for(int i=0;i<groups;i++)
    transition[i]=ride(seats,group,i);
  int step=1,next=0;
  long long ret=0;
  while(rides){
    if(rides&step){
      ret+=transition[next].second;
      next=transition[next].first;
      rides&=~step;
    }
    step*=2;
    transition=twice(transition);
  }
  return ret;
}

vector<pair<int,long long> > twice(const vector<pair<int,long long> >& transition){
  vector<pair<int,long long> > ret=transition;
  for(int i=0;i<ret.size();i++){
    int middle=ret[i].first;
    ret[i].first=transition[middle].first;
    ret[i].second+=transition[middle].second;
  }
  return ret;
}

pair<int,long long> ride(int seats,const vector<int>& groups,int g){
  int next=g,seated=0;
  while(seated+groups[next]<=seats){
    seated+=groups[next];
    next=(next+1)%groups.size();
  }
  return make_pair(next,static_cast<long long>(seated));
}
