
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <list>
#include <unordered_map>
#include <stdexcept>

#define FIRST_DONE 100000000


using namespace std;

struct circle
{
	int id;
	double r;
  char lane;

  int x;
  int y;

	bool operator<(const circle &o) const
	{
    if (r == o.r) return id < o.id;
		return r > o.r;
	}
};

int main() {
	cout.precision(20);
	cerr.precision(20);

	int tn;
	cin >> tn;

	for (int ti = 0; ti < tn; ti++) {

		int n; int w; int l;
		cin >> n >> w >> l;

    cerr << "w: " << w << ", l: " <<l<<endl;

    vector<circle> c;
    c.resize(n);
    for (int i = 0; i < n; ++i)
    {
      c[i].id = i;
      cin >> c[i].r;
    }

    sort(c.begin(), c.end());

    int x = 0;
    int y = 0;
    int xnext = 0;
    int ynext = c[0].r;
    for (int i = 0; i < n; ++i)
    {
      x = xnext;
      circle &cc = c[i];
//      cerr << i << "id: " << cc.id << " r:" << cc.r << endl;

      if (x)
      {
        cc.x = x + cc.r;
      }
      else
      {
        cc.x = 0;
      }
      xnext = cc.x + cc.r;

      if (cc.x > w) {
        x = 0;
        y = ynext;
        ynext = y+2*cc.r;

        cc.x = 0;
        xnext = cc.r;
      }

      cc.y = (y?y+cc.r:0);

      if (cc.x > w) throw std::runtime_error("hiba");
      if (cc.y > l) throw std::runtime_error("tulsok");
    }
    
    vector<circle> c2;
    c2.resize(n);
    for (int i = 0; i < n; ++i)
    {
      c2[c[i].id] = c[i];
    }

    cout << "Case #" << ti+1 << ": ";
		cerr << "Case #" << ti+1 << ": ";
    for (int i = 0; i < n; ++i)
    {
      cout << c2[i].x << " " << c2[i].y << " ";
     // cerr << c2[i].x << " " << c2[i].y << " ";
    }
    cout << endl;
		cerr << endl;
	}
}

