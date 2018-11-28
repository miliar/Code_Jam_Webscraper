#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <exception>

using namespace std;

//----- Start Includes -----
// END CUT HERE
typedef vector<int> Vi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)
#define ALL(x) (x).begin(), (x).end()
// BEGIN CUT HERE
// ----- End Includes -----

typedef pair<int, pair<int,int> > Event;
vector<Event> events;
int T;

int readTime() {
  int h,m;
  char ch;
  cin >> h >> ch >> m;
  return h*60+m;
}

void read(int from) {
  int t1=readTime();
  int t2=readTime();
  events.push_back(make_pair(t2+T,make_pair(-1,1-from)));
  events.push_back(make_pair(t1,make_pair(+1,from)));
}

int main() {
  std::set_terminate (__gnu_cxx::__verbose_terminate_handler);

  int nCases;
  cin >> nCases;
  forUp(caseNr,nCases) {
    events.clear();
    int na,nb;
    cin >> T >> na >> nb;
    forUp(i,na) read(0);
    forUp(i,nb) read(1);
    sort(ALL(events));

    Vi start(2);
    Vi curr(2);
    forEach(e,events) {
      int pos=e.second.second;
      curr[pos] -= e.second.first;
      if (curr[pos]<0) {
        curr[pos]++;
        start[pos]++;
      }
    }
    cout << "Case #" << caseNr+1 << ": " << start[0] << " " << start[1] << endl;
  }
  return 0;
}

// ----- Code Ends -----
