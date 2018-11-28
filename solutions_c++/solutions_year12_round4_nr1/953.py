#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <sstream>
using namespace std;

int vines;
int lengths[10000];
int dist[10000];
int tried[10000];
int final_dist;

bool Go(int at, int arc) {

  if (tried[at] >= arc) {
    return false;
  }
  tried[at] = arc;

  if (dist[at] + arc >= final_dist) {
    return true;
  }

  int longest = -1;
  for (int idx = at + 1; idx < vines; ++idx) {
    if (dist[idx] - dist[at] > arc) {
      break;
    }
    longest = idx;
  }

  if (longest < 0) {
    return false;
  }

  for (int idx = longest; idx > at; --idx) {
    int new_arc = dist[idx] - dist[at];
    if (new_arc > lengths[idx]) {
      new_arc = lengths[idx];
    }
    if (Go(idx, new_arc)) {
      return true;
    }
  }

  return false;
}

int main(int argc, char **argv) {

  int ncases;
  cin >> ncases;
  for (int ccc = 1; ccc <= ncases; ++ccc) {
    cout << "Case #" << ccc << ": ";

    cin >> vines;
    for (int idx = 0; idx < vines; ++idx) {
      cin >> dist[idx] >> lengths[idx];
      tried[idx] = -1;
    }
    cin >> final_dist;
    cout << (Go(0, dist[0]) ? "YES" : "NO");
    cout << endl;
  }

  return 0;
}
