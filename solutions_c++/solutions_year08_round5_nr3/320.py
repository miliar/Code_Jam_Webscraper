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
int h,w;
vector<string> board;
int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    cin >> h >> w;
    board.resize(h);
    for(int i=0;i<h;i++){
      cin >> board[i];
    }
    vector<int> mask(1<<h, 0);
    for(int i=0;i<w;i++){
      vector<int> next_mask(1<<h, 0);
      for(int j=0;j<1<<h;j++){
	int cur = mask[j];
	for(int k=0;k<1<<h;k++){
	  int count = 0;
	  int next_idx = (1<<h)-1;
	  for(int p=0;p<h;p++){
	    if(!((1<<p)&k))continue;
	    if(!((1<<p)&j))continue;
	    if(board[p][i]=='x')continue;
	    count++;
	    if(p!=0){
	      next_idx &= ~(1<<(p-1));
	    }
	    next_idx &= ~(1<<p);
	    if(p!=h-1){
	      next_idx &= ~(1<<(p+1));
	    }
	  }
	  //cout << i << " " << j << " " << k << " " << count+cur << endl;
	  next_mask[next_idx] = max(next_mask[next_idx], count+cur);
	}
      }
      mask = next_mask;
    }
    int maximum = 0;
    for(int i=0;i<1<<h;i++){
      maximum = max(mask[i], maximum);
    }
    cout << maximum << endl;
  }
  return 0;
}
