#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;

pair<int,int> solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    pair<int,int> p=solve();
    cout<<"Case #"<<i+1<<": "<<p.first<<' '<<p.second<<'\n';
  }
}

const int infinity=999999999;

enum event{ a_arrive,a_leave, b_arrive, b_leave};

int read_time(){
  int hour,minute;
  char c;
  cin>>hour>>c>>minute;
  return hour*60+minute;
}

pair<int,int> solve(){
  int turn_around,a,b,ret_a=0,ret_b=0,a_ready=0,b_ready=0;
  cin>>turn_around>>a>>b;
  set<pair<pair<int,int>,pair<int,int> > > q;
  for(int i=0;i<a;i++){
    int start=read_time();
    int end=read_time();
    q.insert(make_pair(make_pair(start,a_leave),make_pair(end,i)));
  }
  for(int i=0;i<b;i++){
    int start=read_time();
    int end=read_time();
    q.insert(make_pair(make_pair(start,b_leave),make_pair(end,a+i)));
  }

  while(q.size()){
    int time=q.begin()->first.first;
    event type=static_cast<event>(q.begin()->first.second);
    int end_time=q.begin()->second.first;
    int id=q.begin()->second.second;
    q.erase(q.begin());
    if(type==a_leave){
      if(a_ready==0) ret_a++;
      else a_ready--;
      q.insert(make_pair(make_pair(end_time+turn_around,b_arrive),make_pair(0,id)));
    }else if(type==b_leave){
      if(b_ready==0) ret_b++;
      else b_ready--;
      q.insert(make_pair(make_pair(end_time+turn_around,a_arrive),make_pair(0,id)));
    }else if(type==a_arrive){
      a_ready++;
    }else if(type==b_arrive){
      b_ready++;
    }
  }
  return make_pair(ret_a,ret_b);
}
