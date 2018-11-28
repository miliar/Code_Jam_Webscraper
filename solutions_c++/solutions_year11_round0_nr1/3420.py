#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// MACROS
#define PRunsigned(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOR(i, a, b) for(unsigned i=(a); i<(b);++i)
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_B(T, I, S, E) for (I = S; I != E; ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)
#define PRunsigned_COLLECTION(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << " " << *it;

#define PRINT_MAPPING(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << it->first << " : " << it->second << endl; cout << endl;

#define LIM 100
int main() {
  
  
  unsigned T; cin >> T;
  FOR(i, 0, T) {
    int n, to = 0, tb = 0, po = 1, pb = 1, b, t = 0, d, td;  
    char r;
    cin >> n;
    //cout << i << " : " << n << " path -> ";
    FOR(j, 0, n) {
      cin >> r >> b;
      //cout << " [" << r << ", " << b << "]";
      int pc = (r == 'O' ? po : pb);
      int dc = (b < pc ? pc - b : b - pc) + 1; // t to get to button
      t = (to > tb ? to : tb);
      if (r == 'O') {
        // time diff
        td = (t - to);
        // calculate the distance i have to travel
        d = (b < po ? po - b : b - po);
        // check if i have already arrive at the destination
        if (d > td) {
          t += (d - td);
        }
        // press the button
        t += 1;
        po = b;
        to = t;
        
      } else {
        // time diff
        td = (t - tb);
        // calculate the distance i have to travel
        d = (b < pb ? pb - b : b - pb);
        // check if i have already arrive at the destination
        if (d > td) {
          t += (d - td);
        }
        // press the button
        t += 1;
        pb = b;
        tb = t;
      }
    }
    cout << "Case #" << i+1 << ": " << t << endl;
  }

}

