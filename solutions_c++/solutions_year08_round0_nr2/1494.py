#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef pair<int,int> event;

class myLess{
  public:
  myLess(){};
  bool operator()(event& lhs,event& rhs){
    if(lhs.first>rhs.first){return true;}
    else if(rhs.first>lhs.first){ return false;}
    else{ if(lhs.second>rhs.second) return true;
          else return false;
     }
  }
};

pair<int,int> simulate(priority_queue<event,vector<event>,myLess> q,int T){

  int availA=0;
  int availB=0;
  int reqA=0;
  int reqB=0;

  while(!q.empty()){
    event e=q.top();
    //printf("Simulating at time=%d\n",e.first);
    q.pop();
    switch(e.second){
      case 0:
        availA++; 
        break;
      case 1:
        availB++; 
        break;
      case 6:
        if(availA!=0){availA--;}
        else{reqA++;}
        break;
      case 7:
        if(availB!=0){availB--;}
        else{reqB++;}
        break;
      case 4:
        {event e2(e.first+T,0);
        q.push(e2);}
        break;
      case 5:
        {event e2(e.first+T,1);
        q.push(e2);}
        break;
    }
    if(availA<0 || availB<0) {printf("Error boss\n");}
  }
  pair<int,int> ans(reqA,reqB);
  //cout<<"Avail sum= "<<availA+availB<<" Req sum = "<<reqA+reqB<<"\n";
  return ans;
}

int main(){
  int N;
  scanf("%d",&N);

  for(int i=0;i<N;i++){
    int T;
    scanf("%d",&T);
    int NA,NB;
    scanf("%d %d",&NA,&NB);
    int hr,min;
    priority_queue<event,vector<event>,myLess> q;
    for(int j=0;j<NA;j++){
      scanf("%d:%d",&hr,&min);
      q.push(event(hr*60+min,6));
      //cout<<"Pushed "<<hr*60+min<<" Type "<< 2<<"\n";
      scanf("%d:%d",&hr,&min);
      q.push(event(hr*60+min,5));
      //cout<<"Pushed "<<hr*60+min<<" Type "<< 5<<"\n";
    }
    for(int j=0;j<NB;j++){
      scanf("%d:%d",&hr,&min);
      q.push(event(hr*60+min,7));
      //cout<<"Pushed "<<hr*60+min<<" Type "<< 3<<"\n";
      scanf("%d:%d",&hr,&min);
      q.push(event(hr*60+min,4));
      //cout<<"Pushed "<<hr*60+min<<" Type "<< 4<<"\n";
    }
    pair<int,int> ans=simulate(q,T);
    printf("Case #%d: %d %d\n",i+1,ans.first,ans.second);
  }

}
