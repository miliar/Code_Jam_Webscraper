#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <sstream>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back

const int inf = 1000 * 1000 * 1000;

typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef vector<ll> vll;
typedef set<int> si;

template<typename T>
void readvector(int N, vector<T> &v, istringstream& iss = cin) {
  v.clear();
  v.resize(N);
  for (int i = 0 ; i < N ; i++)
    iss >> v[i];
}

int R,F,C;
vector<string> grid;

struct pos {
  int d;
  int r,c;
  int state_cur;
  int state_below;
  bool operator<(const pos& p) const {
    vector<int> a;
    vector<int> b;
    a.pb(r);
    a.pb(c);
    a.pb(state_cur);
    a.pb(state_below);
    b.pb(p.r);
    b.pb(p.c);
    b.pb(p.state_cur);
    b.pb(p.state_below);
    return a < b;
  }
};

set<pos> visited;

bool check(int c) {
  return c >= 0 && c < C;
}

void print(pos p) {
  cout << p.r << " " << p.c << endl;
  for (int k = 0 ; k < C ; k++) {
    if ((p.state_cur>>k)&1) cout << '#'; else cout << '.';
  }
  cout << endl;
  for (int k = 0 ; k < C ; k++) {
    if ((p.state_below>>k)&1) cout << '#'; else cout << '.';
  }
  cout << endl;
}

int go() {
  visited.clear();
  deque<pos> file;
  int state_cur = 0, state_below = 0;
  for (int c = 0 ; c < C ; c++) {
    if (grid[0][c] == '#')
      state_cur |= 1<<c;
    if (grid[1][c] == '#') 
      state_below |= 1<<c;
  }
  file.pb((pos){0, 0, 0, state_cur, state_below});
  while (!file.empty()) {
    pos cur = file.front();
    //    print(cur);
    file.pop_front();
    if (cur.r == R) continue;
    if (cur.r == R-1) {
      return cur.d;
    }
    if (visited.count(cur)) { 
      //cout << "visited"<< endl; 
      continue; }
    visited.insert(cur);
    int dd[] = {1,-1};
    for (int i = 0 ; i < 2 ; i++) {
      int nc = cur.c + dd[i];
      int nr = cur.r;
      if (!check(nc)) continue;
      if ((cur.state_cur >> nc)&1) { 
	//cout << "in wall " << endl; 
	continue; }
      // go:
      {
	int f = 0;
	pos np = cur;
	while (!((np.state_below>>nc)&1)) {
	  ++f;
	  ++nr;
	  np.state_cur = np.state_below;
	  np.state_below = 0;
	  for (int k = 0 ; k < C ; k++) {
	    if (grid[nr+1][k] == '#')
	      np.state_below |= 1<<k;
	  }
	}
	if (f > F) goto dig;
	np.c = nc;
	np.r = nr;
	//	cout << "go " << nr << " " << nc << endl;
	file.push_front(np);
      }
    dig:
      // dig:
      {
	pos np = cur;
	if ((np.state_below >> nc)&1) {
	  np.state_below ^= 1<<nc;
	  np.d++;
	  file.push_back(np);
	  //	  cout << "dig " << nr << " " << nc << endl;
	}
      }
    }
  }
  return inf;
}

int main() {
  int T; cin>>T; cin.ignore();
  for (int test = 1 ; test <= T ; test++) {
    grid.clear();
    visited.clear();
    cin>>R>>C>>F; cin.ignore();
    for (int r = 0 ; r < R ; r++) {
      string s;
      getline(cin, s);
      grid.pb(s);
    }
    string floor(C, '#');
    grid.pb(floor);
    grid.pb(floor);  
    
    int res = go();    
    cout << "Case #" << test << ": ";
    if (res < inf) {
      cout << "Yes "<< res << endl;
    } else {
      cout << "No" << endl;
    }
  }
}
