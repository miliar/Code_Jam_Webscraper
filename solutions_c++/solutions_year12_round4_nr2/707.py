#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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

int W,L;

bool canplace(vector<pair<int, pair<float,float> > > &cord, vector<pair<int,int> > &stu, float x, float y, int r) {
  if(x<0 || x > W || y < 0 || y > L)
    return false;
  for(int i=0;i<cord.size();i++) {
    float x2=cord[i].second.first,y2=cord[i].second.second;
    int r2=stu[cord[i].first].first;
    if(abs(x2-x)+abs(y2-y) > r + r2)
      continue;
    if(sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2)) < r + r2)
      return false;
  }
  
  return true;
}

int main() {
	int T;
	cin >> T;
	for(int c=1;c<=T;c++) {
    int N,r;
    cin >> N >> W >> L;
    vector<pair<int,int> > stu(N);
    vector<pair<int, pair<float,float> > > cord;
    for(int i=0;i<N;i++) {
      cin >> r;
      stu[i] = make_pair(r,i);
    }
    int mxl,mxs,mnl;
    if(W>L) {
      mxs=1;
      mxl=W;
      mnl=L;
    }
    else {
      mxs=2;
      mxl=L;
      mnl=W;
    }

    float mx,mn;
    sort(stu.begin(),stu.end());
    
    vector<bool> placed(N,false);
    placed[N-1]=true;
    cord.push_back(make_pair(N-1,make_pair(0,0)));
    mn=stu[N-1].first;
    int v=0;
    if(N>1) {
      if(mxs==1)
        cord.push_back(make_pair(N-2,make_pair(mxl,0)));
      else
        cord.push_back(make_pair(N-2,make_pair(0,mxl)));
      mx=mxl-stu[N-2].first;
      int j;
      for(j=N-3;j>=0;j--) {
        if(mn+2*stu[j].first > mx)
          break;
        if(mxs==1)
          cord.push_back(make_pair(j,make_pair(mn+stu[j].first,0)));
        else
          cord.push_back(make_pair(j,make_pair(0,mn+stu[j].first)));
        mn += 2*stu[j].first;
      }
      
      if(j>0) {
        int to=j;
        mn=-stu[0].first;
        for(j=0;j<=to;j++) {
          if(mxs==1) {
            while(!canplace(cord,stu,mn+stu[j].first,mnl,stu[j].first))
              mn+=stu[j].first;
            cord.push_back(make_pair(j,make_pair(mn+stu[j].first,mnl)));
            mn+=2*stu[j].first;
          }
          else {
            while(!canplace(cord,stu,mnl,mn+stu[j].first,stu[j].first))
              mn+=stu[j].first;
            cord.push_back(make_pair(j,make_pair(mnl,mn+stu[j].first)));
            mn+=2*stu[j].first;
          }
        }
      }
      
    }
      
    
		cout << "Case #" << c << ":";
    cout.setf(ios::fixed);
    for(int i=0;i<N;i++) {
      for(int j=0;j<N;j++) {
        if(stu[cord[j].first].second == i) 
          cout << " " << setprecision(1) << cord[j].second.first << ' ' << setprecision(1) << cord[j].second.second;
      }
    }
    cout << endl;
  }
	return 0;
}
