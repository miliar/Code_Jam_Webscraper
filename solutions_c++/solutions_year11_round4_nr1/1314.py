#include <iostream>
#include <fstream>
#include <algorithm>
#include <utility>

using namespace std;

int main(int argc, char *argv[])
{
  if (argc < 2)
    return 1;
  ifstream in(argv[1]);
  int t;
  in >> t;
  cout.precision(12);
  for (int i = 0; i < t; ++i)
  {
    int x, s, r, t, n;
    in >> x >> s >> r >> t >> n;
    //int l[n + 1], w[n + 1];
    pair<int, int> lw[n + 1];
    for (int j = 0; j < n; ++j)
    {
      int b, e, w, l;
      in >> b >> e >> w;
      x -= (l = e - b);
      lw[j] = make_pair(l, w);
    }
    lw[n++] = make_pair(x, 0);
    sort(lw, lw + n, [](const pair<int, int>& a, const pair<int, int>& b) -> bool
      {
        return a.second < b.second;
      });

    int p = 0, d;
    double rt = t, tt = 0;
    auto f = [&](int add)
    {
      double dt = (double)d / (r + add);
      //cout << "dt=" << dt << ",rt=" << rt << ",tt=" << tt << endl;
      if (dt <= rt)
      {
        rt -= dt;
        tt += dt;
      } else
      {
        dt -= rt;
        tt += rt;
        dt *= (double)(r + add) / (s + add);
        //cout << "DT=" << dt << endl;
        tt += dt;
        rt = 0;
      }
      //cout << "tt=" << tt << endl;
    };
    for (int j = 0; j < n; ++j)
    {
      d = lw[j].first;
      if (d) f(lw[j].second);
/*
      d = b[j] - p;
      if (d) f();
      d = e[j] - b[j];
      f(w[j]);
      p = e[j];
*/
    }
//    d = x - p;
//    if (d) f();
    cout << "Case #" << 1 + i << ": " << tt << endl;
  }
  return 0;
}

