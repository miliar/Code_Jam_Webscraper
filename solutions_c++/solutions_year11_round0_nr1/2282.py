#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <list>
#include <set>

#include <cstdio>
#include <cstring>
#include <climits>

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define MP make_pair
#define cerr if (0) cerr

using namespace std;

typedef pair<int, int> iipair;
#define Button first
#define Order  second

const iipair Sentinel(101, 101);

#define signum(v) (v > 0 ? +1 : (v < 0 ? -1 : 0))

int main()
{
  int T, N;
  
  cin >> T;

  REP(i, T) {
    cin >> N;
    
    queue<iipair> blue, orange; // command queues for each bot

    REP(j, N) {
      char col;
      int btn;
      cin >> col >> btn;
      if (col == 'O') orange.push( iipair(btn, j) );
      else            blue.push( iipair(btn, j) );
    }
    orange.push(Sentinel);
    blue.push(Sentinel);

    long long time = 0;
    int opos = 1; // pos of orange bot
    int bpos = 1; // pos of blue bot

    for (;; ++time) {
      //if (time > 10) break;
      const iipair ocmd = orange.front();
      const iipair bcmd = blue.front();

      if (ocmd == Sentinel && bcmd == Sentinel) break; // all commands finished

      if (ocmd != Sentinel) {
	if (opos == ocmd.Button) {
	  if (bcmd.Order > ocmd.Order) {
	    orange.pop();
	    cerr << "Orange: Push Button " << ocmd.Button << endl;
	  } else {
	    cerr << "Orange: Stay at " << ocmd.Button << endl;
	    // stay.
	  }
	} else {
	  opos += signum(ocmd.Button - opos);
	  cerr << "Orange: Move to " << opos << endl;
	}
      } else {
	cerr << "Orange: Stay at " << ocmd.Button << endl;
      }

      if (bcmd != Sentinel) {
	if (bpos == bcmd.Button) {
	  if (ocmd.Order > bcmd.Order) {
	    blue.pop();
	    cerr << "Blue: Push Button " << bcmd.Button << endl;
	  } else {
	    cerr << "Blue: Stay at " << bcmd.Button << endl;
	    // stay.
	  }
	} else {
	  bpos += signum(bcmd.Button - bpos);
	  cerr << "Blue: Move to " << bpos << endl;
	}
      } else {
	cerr << "Blue: Stay at " << bcmd.Button << endl;
      }
    }

    cout << "Case #" << i+1 << ": " << time << endl;
  }
  
  return 0;
}
