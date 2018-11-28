#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<utility>

using namespace std;

struct comp_pair {
  bool operator() (const pair<char, char>& v1, const pair<char, char>& v2) const {
    char v1_1 = v1.first, v1_2 = v1.second;
    if (v1_1 > v1_2)
      swap(v1_1, v1_2);

    char v2_1 = v2.first, v2_2 = v2.second;
    if (v2_1 > v2_2)
      swap(v2_1, v2_2);
  
    return v1_1 < v2_1 ? true :
           v1_1 > v2_1 ? false :
           v1_2 < v2_2 ? true :
                         false;
  }
};

typedef map<pair<char, char>, char, comp_pair> map_type;
typedef set<pair<char, char>, comp_pair> set_type;

vector<char> solve(const vector<char>& elems,
                   const map_type& combine,
                   const set_type& oppose) {

  vector<char> ret;

  for (vector<char>::const_iterator it = elems.begin();
       it != elems.end();
       ++it) {
    ret.push_back(*it);
    int size =ret.size();
    if (size < 2) continue;

    char c1 = ret[size-2];
    char c2 = ret[size-1];
    map_type::const_iterator combined_it = combine.find(make_pair(c1, c2));

    if (combined_it != combine.end()) {
      ret.pop_back(), ret.pop_back();
      ret.push_back(combined_it->second);
    }
    else {
      for (vector<char>::const_iterator jt = ret.begin();
           jt != ret.end();
           ++jt) {
        set_type::const_iterator opposed_it = oppose.find(make_pair(*jt, c2));
        if (opposed_it != oppose.end()) {
          ret.clear();
          break;
        }
      }
    }
  }

  return ret;
}

int main() {
  int t;
  cin >> t;
  for (int s = 1; s <= t; ++s) {
    int c;
    map_type combine;

    cin >> c;
    for (int i = 0; i < c; ++i) {
      char c1, c2, c3;
      cin >> c1 >> c2 >> c3;
      combine.insert(make_pair(make_pair(c1, c2), c3));
    }

    int d;
    set_type oppose;

    cin >> d;
    for (int i = 0; i < d; ++i) {
      char c1, c2;
      cin >> c1 >> c2;
      oppose.insert(make_pair(c1, c2));
    }

    int n;
    vector<char> elems;

    cin >> n;
    for (int i = 0; i < n; ++i) {
      char c;
      cin >> c;
      elems.push_back(c);
    }

    vector<char> ret = solve(elems, combine, oppose);

    cout << "Case #" << s << ": [";
    if (ret.size() > 0) {
      cout << ret[0];
      for (vector<char>::iterator it = ret.begin() + 1;
           it != ret.end();
           ++it) {
        cout << ", " << *it;
      }
    }
    cout << "]" << endl;
  }
}
