
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <unordered_map>



using namespace std;

vector<int> d;
vector<int> l;

int f;

std::map<int, int> x;

bool calc(int pos, int rope)
{
  int ropeat = d[rope];
  int ropemax = ropeat + (ropeat - pos);

  x.erase(rope);

  //cerr << "pos: " << pos << ", rope: " << rope << ", ropemax: " << ropemax << endl;
  if (ropemax >= f) return true;

  bool b = false;
  int i = rope + 1;
  while (d[i] <= ropemax)
  {
    //catch rope
    int newpos = ropeat;
    if (d[i] - l[i] > newpos) newpos = d[i] - l[i];

    if (x.count(i))
    {
      int bu = x[i];
      if (newpos < bu) x[i] = newpos;
    }
    else
    {
      x[i] = newpos;
    }
    //b |= calc(newpos, i);

    ++i;
  }

  return b;
}

int main() {
	cout.precision(20);
	cerr.precision(20);

	int tn;
	cin >> tn;

	for (int ti = 0; ti < tn; ti++) {

    cerr << ti << endl;

    int n;
    cin >> n;
    d.clear();
    l.clear();
    x.clear();
    d.resize(n);
    l.resize(n);
    for (int i = 0; i < n; ++i)
    {
      cin >> d[i];
      cin >> l[i];
    }
    cin >> f;

    bool b = false;
    x[0] = 0;
    while (x.size() && !b)
    {
      //cerr << x << endl;

      int rope = x.begin()->first;
      int pos = x.begin()->second;

      b = calc(pos, rope);
    }


		cout << "Case #" << ti+1 << ": " << (b?"YES":"NO") << endl;
		cerr << "Case #" << ti+1 << ": " << (b?"YES":"NO") << endl;
	}
}
