#include <iostream>

using namespace std;

int answer();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<answer()<<'\n';
}

void move(pair<int,int>& robot,int target,int& time);

int answer(){
  int buttons;
  cin>>buttons;
  pair<int,int> blue(1,0),orange(1,0);
  int time=0;
  for(int i=0;i<buttons;i++){
    char r;
    int target;
    cin>>r>>target;
    pair<int,int>& robot=r=='B'?blue:orange;
    move(robot,target,time);
  }
  return time;
}

void move(pair<int,int>& robot,int target,int& time){
  int arrive=robot.second+abs(target-robot.first);
  robot.first=target;
  time=max(arrive+1,time+1);
  robot.second=time;
}
