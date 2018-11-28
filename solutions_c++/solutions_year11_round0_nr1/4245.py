#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;
int seq[101][2], n, no, nb;
map< vector<int>, int > M;
queue< vector<int> > Q;
inline void enqueue(vector<int> v, int d) {
  if ((!M.count(v) || M[v] > d) && v[2]>=1 && v[2]<=100 &&
      v[3]>=1 && v[3]<=100) {
    M[v] = d;
    Q.push(v);
  }
}
inline vector<int> mv(int a, int b, int c, int d) {
  vector<int> v  = vector<int>(4);
  v[0] = a, v[1] = b, v[2] = c, v[3] = d;
  return v;
}
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  for (int rr = 1; rr <= nocases; ++rr) {
    no = nb = 0;
    M.clear();
    cin >> n;
    Q = queue< vector<int> >();
    for (int i = 0; i < n; ++i) {
      char c;
      cin >> c >> seq[i][1];      
      seq[i][0] = (c == 'B');
      if (c == 'B')
	nb++;
      else
	no++;
    }
    enqueue(mv(0, 0, 1, 1), 0);
    while (Q.size()) {
      vector<int> v = Q.front(); Q.pop();
      int d = M[v];
      if (v[0] == nb && v[1] == no) {
	printf("Case #%d: %d\n", rr, d);
	break;
      }
      int at = v[0] + v[1];
      for (int dx = -1; dx <= 1; ++dx)
	for (int dy = -1; dy <= 1; ++dy)
	  for (int po = 0; po <= 1; ++po)
	    for (int pb = 0; pb <= 1; ++pb)
	      if (!(pb && po)) {
		if (!pb && !po)
		  enqueue(mv(v[0], v[1], v[2]+dx, v[3]+dy), d+1);
		else if (pb && !dx && v[0]<nb && seq[at][0]
			 && seq[at][1]==v[2])
		  enqueue(mv(v[0]+1, v[1], v[2], v[3]+dy), d+1);
		else if (po && !dy && v[1]<no && !seq[at][0]
			 && seq[at][1]==v[3])
		  enqueue(mv(v[0], v[1]+1, v[2]+dx, v[3]), d+1);
	      }
    }
  }
  return 0;
}
