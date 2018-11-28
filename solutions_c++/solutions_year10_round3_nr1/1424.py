// don't solve problems at the party !!!!!!
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <iterator>
#include <sstream>

#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>
#include <boost/algorithm/string/join.hpp>

using namespace std;
using boost::algorithm::is_any_of;
using boost::algorithm::split;
using boost::algorithm::join;

ostream& operator<<(ostream& os, const vector<string>& vec)
{
  ostream_iterator<string> iter(os, ", ");
  copy(vec.begin(), vec.end(), iter);
  return os;
}

ostream& operator<<(ostream& os, const vector<size_t>& vec)
{
  ostream_iterator<size_t> iter(os, ", ");
  copy(vec.begin(), vec.end(), iter);
  return os;
}

ostream& operator<<(ostream& os, const pair<size_t, size_t>& p)
{
  os << "(" << p.first << ", " << p.second << ")";
  return os;
}

bool intersect(const pair<size_t, size_t>& lhs, const pair<size_t, size_t>& rhs)
{
  if (lhs == rhs)
    return false;

  pair<size_t, size_t> A = max(lhs, rhs);
  pair<size_t, size_t> B = min(lhs, rhs);

  if (A.first == A.second && B.first == B.second && A.first != B.first)
    return false;

  if (A.first < B.first) {
    if (A.second < B.second) {
      return false;
    } else {
      return true;
    }
  }

  if (A.first > B.first) {
    if (A.second < B.second) {
      return true;
    } else {
      return false;
    }
  }
}

int main()
{
  size_t NCASES;

  cin >> NCASES;

  for (size_t CASE = 0; CASE < NCASES; CASE++) {
    size_t NWIRES;
    cin >> NWIRES;
    
    set<pair<size_t, size_t> > WIRES;

    for (size_t w = 0; w < NWIRES; w++) {
      size_t A, B;
      cin >> A >> B;

      pair<size_t, size_t> p(A, B);
      WIRES.insert(p);
    }

    size_t intersections = 0;
    set<pair<size_t, size_t> >::iterator k, m;
    for (k = WIRES.begin(); k != WIRES.end(); ++k) {
      for (m = WIRES.begin(); m != WIRES.end(); ++m) {
        if (*k == *m)
          continue;        
        if (intersect(*k, *m)) {
          //cout << "checking if " << (*k) << " and " << (*m) << " intersect" << endl;
          //cout << "THEY DO!" << endl;
          intersections++;
        }
      }
    }
    cout << "Case #" << (CASE + 1) << ": " << intersections/2 << endl;
  }
}
