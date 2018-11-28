#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

const int O = 0;
const int B = 1;

int solve(vector< pair<int, int> >& v,
		  vector<int> &o, vector<int> &b) {

  int op = 1;
  int bp = 1;

  int oi = 0;
  int bi = 0;

  int time = 0;

  o.push_back(0);
  b.push_back(0);
  for (size_t vi = 0; vi < v.size(); vi++) {
	int next_time = 0;
	if (v[vi].first == O) {
	  next_time = abs(o[oi] - op) + 1;
	  op = o[oi];
	  oi++;
	  if (next_time >= abs(b[bi] - bp)) {
		bp = b[bi];
	  } else {
		bp = bp + (abs(b[bi] - bp) / (b[bi] - bp)) * next_time;
	  }
	    
	} else {
	  next_time = abs(b[bi] - bp) + 1;
	  bp = b[bi];
	  bi++;
	  if (next_time >= abs(o[oi] - op)) {
		op = o[oi];
	  } else {
		op = op + (abs(o[oi] - op) / (o[oi] - op)) * next_time;
	  }
	}
	time += next_time;
  }
  return time;
  /*
	for (size_t i = 0; i < v.size(); i++) {
	cout << v[i].first << v[i].second << endl;
	}*/
  return time;
}

int main() {

  int N;
  cin >> N;

  for (int i = 0; i < N; i++) {
	int M;
	cin >> M;
	vector< pair<int, int> > v;
	vector<int> o, b;
	for(int j = 0; j < M; j++) {
	  char c;
	  int t;
	  cin >> c >> t;
	  if (c == 'O') {
		o.push_back(t);
		v.push_back( make_pair(O, t) );
	  } else {
		b.push_back(t);
		v.push_back( make_pair(B, t) );
	  }
	}
	cout << "Case #" << i + 1 << ": " << solve(v, o, b) << endl;
  }
  return 0;
}
