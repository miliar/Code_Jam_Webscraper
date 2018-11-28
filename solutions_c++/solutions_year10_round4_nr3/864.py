#include <iostream>
#include <set>
#include <utility>

using namespace std;

int solve(set<pair<int,int> > *live) {
  int g = 0;

  while (live->size() > 0) {
    set<pair<int,int> > *newlive = new set<pair<int,int> >;
    // cerr << g << " " << live->size() << "\n";
    for (set<pair<int,int> >::const_iterator it = live->begin();
         it != live->end(); ++it) {
      int x = it->first;
      int y = it->second;
      if (live->count(make_pair(x-1, y)) || live->count(make_pair(x, y-1)))
        newlive->insert(*it);
      if (live->count(make_pair(x-1,y+1)))
        newlive->insert(make_pair(x,y+1));
      if (live->count(make_pair(x+1,y-1)))
        newlive->insert(make_pair(x+1,y));
    }
    set<pair<int,int> > *p = live;
    live = newlive;
    g++;
    delete p;
  }
  delete live;
  return g;
}

int main(void)
{
  int ncases;
  int casenr;
  set<pair<int,int> > *live;

  cin >> ncases;
  for (casenr = 1; casenr <= ncases; casenr++) {
    live = new set<pair<int,int> >;
    int nR;
    cin >> nR;
    for (int i = 0; i < nR; i++) {
      int x1, x2, y1, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for (int x = x1; x <= x2; x++) {
        for (int y = y1; y <= y2; y++) {
          live->insert(make_pair(x, y));
        }
      }
    }
    int s = solve(live);
    cout << "Case #" << casenr << ": " << s << "\n";
    cerr << "Case #" << casenr << ": " << s << "\n";
  }
}
