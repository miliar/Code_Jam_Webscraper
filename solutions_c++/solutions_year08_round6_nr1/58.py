#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <set>
using namespace std;

int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ":" << endl;
    int n;
    cin >> n;
    vector<pair<int,int> > birds;
    vector<pair<int,int> > nbirds;
    for(int i=0;i<n;i++){
      int x,y;
      cin >> x >> y;      
      string s;
      cin >> s;
      if(s=="BIRD"){
	birds.push_back(make_pair(x,y));
      }else{
	string dummy;
	cin >> dummy;
	nbirds.push_back(make_pair(x,y));
      }
      
    }
    int bx_min = 10000000;
    int bx_max = 0;
    int by_min = 10000000;
    int by_max = 0;
    
    for(int i=0;i<(int)birds.size();i++){
      int x,y;
      x = birds[i].first;
      y = birds[i].second;
      bx_min =min(bx_min,x);
      by_min = min(by_min,y);
      bx_max = max(bx_max,x);
      by_max = max(by_max,y);
    }

    int m;
    cin >> m;

    if(birds.size() == 0){
      for(int i=0;i<m;i++){
	int x,y;
	cin >> x >> y;
	int ans = 0;
	for(int j=0;j<(int)nbirds.size();j++){
	  if(x==nbirds[j].first && y==nbirds[j].second){
	    ans = 1;
	  }
	}
	if(ans==-1)cout << "BIRD" << endl;
      else if(ans==0)cout << "UNKNOWN" << endl;
      else cout << "NOT BIRD" << endl;
	
      }
    } else {
    
    for(int i=0;i<m;i++){
      int x,y;
      cin >> x >> y;
      int ans = 0;
      if(x >= bx_min && x <= bx_max && y >= by_min && y<= by_max){
	ans = -1;
      }
      for(int i=0;i<(int)nbirds.size();i++){
	int xx,yy;
	xx = nbirds[i].first;
	yy = nbirds[i].second;
	if(xx >= bx_min && xx <= bx_max){
	  if(yy >= by_max){
	    if(y>=yy)ans=1;
	  }
	  if(yy <= by_min){
	    if(y<=yy)ans=1;
	  }
	}
	if(yy >= by_min && yy <= by_max){
	  if(xx >= bx_max){
	    if(x>=xx)ans=1;
	  }
	  if(xx <= bx_min){
	    if(x<=xx)ans=1;
	  }
	}
	if(yy < by_min && xx < bx_min){
	  if(y<=yy && x<=xx)ans = 1;
	}
	if(yy > by_max && xx < bx_min){
	  if(y>=yy && x<=xx)ans=1;
	}
	if(yy > by_max && xx > bx_max){
	  if(y>=yy && x>=xx)ans = 1;
	}
	if(yy < by_min && xx > bx_max){
	  if(y<=yy && x>=xx)ans= 1;
	}
       }
      if(ans==-1)cout << "BIRD" << endl;
      else if(ans==0)cout << "UNKNOWN" << endl;
      else cout << "NOT BIRD" << endl;
    }
    }
  }
  return 0;
}
