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
    cout << "Case #" << ++temp << ": ";
    int w,h,a;
    cin >> w >> h >> a;
    int x1, y1, x2, y2;
    bool found = false;
    for(int x=0;x<=w;x++){
      for(int y=0;y<=h;y++){
	for(int xx=0;xx<=w;xx++){
	  for(int yy=0;yy<=h;yy++){
	    int area = xx*y-yy*x;
	    if(abs(area) == a){
	      found = true;
	      x1 = x;
	      y1 = y;
	      x2 = xx;
	      y2 = yy;
	      goto END;
	    }
	  }
	}
      }
    }
  END:
    if(found){
      cout << 0 << " " << 0 << " " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
