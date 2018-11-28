#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef pair<int, int>       pint;
typedef vector<int>          vint;
typedef vector<unsigned int> vuint;
typedef vector<vint>         vvint;
typedef vector<vuint>        vvuint;
typedef vector<pint>         vpint;


#define ALL(c)     (c).begin(), (c).end()
#define SORT(c)    sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c)  SORT(c), (c).resize( unique(ALL(c)) - (c).begin() )

unsigned int count_intersections(const vpint& wires) {
  unsigned int count = 0;
  for(int i = 0; i < wires.size(); ++i) {
    for(int j = i+1; j < wires.size(); ++j) {
      if(i == j) continue;
      if ((wires[i].first <= wires[j].first && 
	  wires[i].second >= wires[j].second) ||
	  (wires[i].first >= wires[j].first &&
	   wires[i].second <= wires[j].second ))
	count++;
    }
  }
  return count;
}

int main() 
{
  unsigned int T = 0;
  cin >> T;
  for(unsigned t = 1; t <= T; ++t) {
    // INPUT
    unsigned N;
    cin >> N;

    vpint wires;
    for(unsigned n = 0; n < N; ++n) {
      int A, B;
      cin >> A >> B;
      wires.push_back( pint(A,B) );
    }


    // OUTPUT
    cout << "Case #" << t << ": ";
    cout << count_intersections(wires);
    cout << endl;
  }

  return 0;
}
