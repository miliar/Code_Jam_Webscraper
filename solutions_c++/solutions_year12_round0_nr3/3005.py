#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int pow_10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
void cycle(int a, int b, int x, set<pair<int, int> >& s) {
  int nd=0, t=x;
  while(t) {
    nd++;
    t = t/10;
  }
  t = x;
  for(int i=1; i<nd; ++i) {
    int r = x%10;
    if(r==0) continue;
    int y = (x - r)/10 + r*pow_10[nd-1];    
    if( y!=t && y!=x && y>=a && y<=b) {
      if(t<y) s.insert(make_pair(t, y));
      else s.insert(make_pair(y, t));
    }
    x = y;
  }
}

int main(int argc, char** argv) {
  int t, a, b, r;
  ifstream fin(argv[1]);
  fin >> t;
  for(int i=1; i<=t; ++i) {
    fin >> a >> b;
    set<pair<int, int> > s;
    for(int x=a; x<=b; ++x) {
      cycle(a, b, x, s);
    }
    cout << "Case #" << i << ": " << s.size() << endl;
  }  
  fin.close();
  return 0;
}
