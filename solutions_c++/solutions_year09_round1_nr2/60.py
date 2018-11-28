
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;
typedef double decimal;


struct K {
  int x;
  int y;
  integer t;
};

bool operator >(const K& a, const K& b) {
  return a.t > b.t;
}

struct Cross {
  int ns;
  int ew;
  int ini;
};

Cross field[20][20];

int main(void) {
  
  int nCases;
  cin >> nCases;
  
  REP(iCase, nCases) {
    int nRows;
    int nCols;
    cin >> nRows >> nCols;
    REP(i, nRows){
      REP(j, nCols){
	int ns, ew, t;
	cin >> ns >> ew >> t;
	int cycle = ns + ew;
	int ini = (cycle - t % cycle) % cycle;
	field[i][j] = (Cross){ns, ew, ini};
      }
    }
    
    int startx = 0;
    int starty = nRows*2-1;
    int goalx = nCols*2-1;
    int goaly = 0;

    vector<vector<integer> > dist(nRows*2, vector<integer>(nCols*2, (integer)-1));
    priority_queue<K, vector<K>, greater<K> > q;
    q.push((K){startx, starty, 0});
    while(!q.empty()){
      K cur = q.top();
      q.pop();
      if(dist[cur.y][cur.x] < 0){
	dist[cur.y][cur.x] = cur.t;
	if(cur.x == goalx && cur.y == goaly)
	  break;
	
	if(cur.x > 0){ // W
	  int cost;
	  if(cur.x % 2 == 1){ // cross
	    cost = 1;
	    const Cross& cross = field[cur.y/2][cur.x/2];
	    int cycle = cross.ns + cross.ew;
	    int curstate = (cross.ini + cur.t) % cycle;
	    if(curstate < cross.ns)
	      cost += cross.ns - curstate;
	  }else{
	    cost = 2;
	  }
	  K next = {cur.x-1, cur.y, cur.t + cost};
	  if(dist[next.y][next.x] < 0)
	    q.push(next);
	}

	if(cur.x < nCols*2-1){ // E
	  int cost;
	  if(cur.x % 2 == 0){ // cross
	    cost = 1;
	    const Cross& cross = field[cur.y/2][cur.x/2];
	    int cycle = cross.ns + cross.ew;
	    int curstate = (cross.ini + cur.t) % cycle;
	    if(curstate < cross.ns)
	      cost += cross.ns - curstate;
	  }else{
	    cost = 2;
	  }
	  K next = {cur.x+1, cur.y, cur.t + cost};
	  if(dist[next.y][next.x] < 0)
	    q.push(next);
	}

	if(cur.y > 0){ // N
	  int cost;
	  if(cur.y % 2 == 1){ // cross
	    cost = 1;
	    const Cross& cross = field[cur.y/2][cur.x/2];
	    int cycle = cross.ns + cross.ew;
	    int curstate = (cross.ini + cur.t) % cycle;
	    if(!(curstate < cross.ns))
	      cost += cycle - curstate;
	  }else{
	    cost = 2;
	  }
	  K next = {cur.x, cur.y-1, cur.t + cost};
	  if(dist[next.y][next.x] < 0)
	    q.push(next);
	}

	if(cur.y < nRows*2-1){ // S
	  int cost;
	  if(cur.y % 2 == 0){ // cross
	    cost = 1;
	    const Cross& cross = field[cur.y/2][cur.x/2];
	    int cycle = cross.ns + cross.ew;
	    int curstate = (cross.ini + cur.t) % cycle;
	    if(!(curstate < cross.ns))
	      cost += cycle - curstate;
	  }else{
	    cost = 2;
	  }
	  K next = {cur.x, cur.y+1, cur.t + cost};
	  if(dist[next.y][next.x] < 0)
	    q.push(next);
	}

      }
    }
    
    cout << "Case #" << (iCase + 1) << ": " << dist[goaly][goalx] << endl;
  }
  
  return 0;
}
