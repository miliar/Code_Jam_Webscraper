#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

int debug = 0;

main() {
  int T;
  cin >> T;
  for (int t=0; t<T; ++t) {
    cout << "Case #" << t+1 <<": ";

    int C;
    cin >> C;
    char combine[36][4];
    char dust[28][3];

    for (int i=0;i<C;++i) {
      cin >> combine[i];
      if (debug)
	cerr<<"Combine ["<<combine[i]<<"]"<<endl;
    }

    int D;

    cin >> D;
    for (int i=0;i<D;++i) {
      cin >> dust[i];
      if (debug)
	cerr<<"dust ["<<dust[i]<<"]"<<endl;
    }
    
    int N;
    cin >> N;
    char input[101];
    cin >> input;
    if (debug) cerr<<"input ["<<input<<"]"<<endl;
    
    char deck[101];
    char *p=deck;
    int pc;
    for (pc=0;input[pc];pc++) {
      if (debug) {
	*p=0;
	cerr<<" ["<<deck<<"] -> ";
      }
      *p=input[pc];
      if (p>deck) {
	int i;
	for (i=0;i<C;++i) {
	  if ((combine[i][0]==p[0] && combine[i][1]==p[-1]) ||
	      (combine[i][1]==p[0] && combine[i][0]==p[-1])) {
	    p--;
	    *p=combine[i][2];
	    break;
	  }
	}

	if (i==C) {
	  for (char *q=deck;q<p;q++) {
	    for (int j=0;j<D;++j) {
	      if ((dust[j][0]==*q && dust[j][1]==*p)
		  || (dust[j][1]==*q && dust[j][0]==*p)) {
		p=deck-1;
		q=p;
		break;
	      }
	    }
	  }
	}
      }

      p++;
      if (debug) {
	*p=0;
	cerr<<"["<<deck<<"]"<<endl;
      }
    }
    
    cout <<"[";
    for (char *q=deck;q<p;q++) {
      if (q>deck) cout <<", ";
      cout<< *q;
    }
    cout << "]"<<endl;
  }
}
