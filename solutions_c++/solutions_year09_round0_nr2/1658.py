#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

typedef vector<pair<int,int> > nlist_t;

bool pcmp(pair<int,int> &a, pair<int,int> &b) {
  if (a.second == b.second) return (a.first < b.first);
  else return (a.second < b.second);
}

char get_sink(int H, int W, int x, vector<int> &my_map, vector<char> &sink, char &label) {
  nlist_t res;
  if (sink[x] != ' ') return sink[x];
  if (x >= W) res.push_back(make_pair(x - W, my_map[x - W]));
  if ((x % W) > 0) res.push_back(make_pair(x - 1, my_map[x - 1]));
  if ((x % W) < (W - 1)) res.push_back(make_pair(x + 1, my_map[x + 1]));
  if ((x / W) < (H - 1)) res.push_back(make_pair(x + W, my_map[x + W]));
  nlist_t::iterator it = min_element(res.begin(), res.end(), pcmp);
  if (it->second < my_map[x]) sink[x] = get_sink(H, W, it->first, my_map, sink, label);
  else sink[x] = label++;
  return sink[x];
}

void solve_it() {
  int H, W;
  cin >> H >> W;
  vector<int> my_map;
  for (int i=0; i<H*W; i++) {
    int h;
    cin >> h;
    my_map.push_back(h);
  }
  if ((H == 1) && (W == 1)) {
    cout << 'a' << endl;
    return;
  }
  vector<char> sink(H*W, ' ');
  char label = 'a';
  for (int i=0; i<H*W; i++) {
    cout << get_sink(H, W, i, my_map, sink, label);
    if ((i % W) == (W - 1)) cout << endl;
    else cout << " ";
  }
}

int main() {
  int cases;
  cin >> cases;
  for (int i=1; i<=cases; i++) {
    cout << "Case #" << i << ":" << endl;
    solve_it();
  }
}
