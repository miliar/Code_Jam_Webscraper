#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

int N;
int robot[100];
int button[100];

const bool debug=false;

main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cout << "Case #" << t+1 <<": ";

    cin >> N;
    
    for (int n=0; n<N; ++n) {
      char ch;
      cin >> ch;
      robot[n] = (ch=='B'); 
      cin >> button[n];
      if (debug)
	cerr<< " read "<< robot[n]<<" "<<button[n]<<endl;
    }

    int pc=0;

    struct Cpu {
      int pos;
      int target;

      bool update(int pc, int me) {
	if (robot[pc] == me && button[pc] == pos) {
	  if (debug)
	    cerr<<"robot "<<me<<" press button at "<<pos<<endl;
	  target=0;
	  return true; 
	}
	if (!target) {
	  for (;pc<N && robot[pc]!=me; pc++);
	  if (pc<N) {
	    target=button[pc];
	    if (debug)
	      cerr<<"robot "<<me<<" next target "<<target<<endl;
	  }
	}

	if (target) {
	  if (pos<target) 
	    pos++;
	  if (pos>target)
	    pos--;
	  if (debug)
	    cerr<<"robot "<<me<<" at position "<<pos<<endl;
	  return false;
	}
      }

      Cpu(): pos(1), target(0) {}
    };

    Cpu cpu[2];
    
    int time=0;
    for (pc=0; pc<N; time++) {
      if (debug)
	cerr<<"pc "<<pc<<endl;
      bool done0 = cpu[0].update(pc,0);
      bool done1 = cpu[1].update(pc,1);
      if (done0 || done1)
	pc++;
      if (debug) {
	cerr<<"time "<<time<<endl;
	if (time>10) return 1;
      }
    }
    
    cout << time << endl;
  }
  return 0;
}
