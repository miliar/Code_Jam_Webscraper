#include <iostream>
#include <vector>
#include <map>

using namespace std;

int answer();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<answer()<<'\n';
}

int move(map<int,int>& m);

int answer(){
  int corners;
  cin>>corners;
  map<int,int> dogs;
  for(int i=0;i<corners;i++){
    int place,count;
    cin>>place>>count;
    dogs[place]=count;
  }
  int ret=0;
  do{
    int now=move(dogs);
    if(now==0) return ret;
    ret+=now;
  }while(true);
}

int move(map<int,int>& m){
  int ret=0;
  map<int,int> next;
  for(map<int,int>::iterator i=m.begin();i!=m.end();i++)
    if(i->second){
      int moves=i->second/2;
      int stays=i->second&1;
      if(moves){
        next[i->first-1]+=moves;
        next[i->first+1]+=moves;
        ret+=moves;
      }
      if(stays)
        next[i->first]++;
    }
  m=next;
  return ret;
}
