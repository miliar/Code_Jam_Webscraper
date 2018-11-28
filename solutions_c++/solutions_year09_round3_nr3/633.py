#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

uint one(uint P, uint C, set<uint> already, uint n) {
  uint c = 0;
  for (uint i = n + 1; i <= P; i++) {
    if (already.find(i) == already.end()) {
      c++;
    } else {
      break;
    }
  }
  for (uint i = n - 1; i > 0; i--) {
    if (already.find(i) == already.end()) {
      c++;
    } else {
      break;
    }
  }
  return C + c;
}

uint Ks(uint P, uint C, set<uint> already, set<uint> yetto) {
  if (yetto.size() == 0) return C;
  if (yetto.size() == 1) {
    return one(P, C, already, *yetto.begin());
  } else {
     set<uint>::iterator it;
     uint min_c = 1000000000;
     set<uint> min_already;
     set<uint> min_yetto;

     for (it = yetto.begin(); it != yetto.end(); it++) {
       uint c = 0;
       set<uint> new_already = already;
       set<uint> new_yetto = yetto;
       new_yetto.erase(new_yetto.find(*it));
       new_already.insert(*it);
       c = one(P, C, already, *it) + Ks(P, 0, new_already, new_yetto);

       if (c < min_c) {
	 min_c = c;
	 min_already = new_already;
	 min_yetto = new_yetto;
       }
     }

     return C + min_c;
  }

}


int main()
{
  ios_base::sync_with_stdio(0);

  uint N;
  cin >> N;

  for (uint i = 1; i < N + 1; i++) {
    uint P, Q;
    cin >> P;
    cin >> Q;

    set<uint> yetto;
    
    for (uint j = 0; j < Q; j++) {
      uint p;
      cin >> p;
      yetto.insert(p);
    }

    cout << "Case #" << i << ": " << Ks(P, 0, set<uint>(), yetto) << endl;
  }

  return 0;
}
