// Technique: Simple Simulation
//
// Find the next O and next B
// at each step, march toward the next
// O or next B.
// If you are there, stop marching.
#include <iostream>


#include <vector>
#include <cmath>
using namespace std;

int next_B(vector<pair<char,int> > & x, int cur) {
  if (cur==-1) {
    for (int i=0;i<x.size();i++) {
      if (x[i].first=='B') return i;
    }
    return -1;
  } else {
    for (int i=cur+1;i<x.size();i++) {
      if (x[i].first=='B') return i;
    }
    return -1;
  }
}
int next_O(vector<pair<char,int> > & x, int cur) {
  if (cur==-1) {
    for (int i=0;i<x.size();i++) {
      if (x[i].first=='O') return i;
    }
    return -1;
  } else {
    for (int i=cur+1;i<x.size();i++) {
      if (x[i].first=='O') return i;
    }
    return -1;
  }
}


int main() {

  int T;

  cin >> T;

  for (int x1=0;x1<T;x1++) {
    int N;
    cin >> N;
    vector<pair<char,int> > buts;
    for (int x2=0;x2<N;x2++) {
      char C;
      int P;
      cin >> C;
      cin >> P;
      //      cout << "C=" << C << " " << P << endl;

      buts.push_back(make_pair(C,P));

    }
    int oi,bi;
    oi = 1;
    bi = 1;
    int t=0;
    int no,nb=0;
    int io,ib = -1;
    io=-1;
    io=next_O(buts,io);
    ib=next_B(buts,ib);
    int to,tb;
    if (io!=-1) {
    }
    if (ib!=-1) {
      tb=buts[ib].second;
    }
    t = 0;
    while ((io!=-1)||(ib!=-1)) {
      bool advanceo=false;;
      bool advanceb=false;
      if (io!=-1) {
	to = buts[io].second;
	if (to==oi) { // At the target
	  // Push button
	  // Find the next target
	  if ((io<ib)||(ib==-1)) {
	    advanceo=true;
	  }
	} else {
	  if (to > oi) {
	    oi++;
	  } else {
	    oi--;
	  }
	}
      }
      if (ib!=-1) {
	tb = buts[ib].second;
	if (tb==bi) { // At the target
	  // Push button
	  // Find the next target
	  if ((ib<io)||(io==-1)) {
	    advanceb=true;
	  }
	} else {
	  if (tb > bi) {
	    bi++;
	  } else {
	    bi--;
	  }
	}
      }
      if (advanceo) io = next_O(buts,io);
      if (advanceb) ib = next_B(buts,ib);
      t++;
      //cout << io << " " << ib << " " << t << " " << oi << " " << bi << endl;
    }
    int y = t;

    cout << "Case #"<<x1+1<<": " <<y<< endl;
  }
}
