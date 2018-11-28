#include <iostream>
#include <set>

using namespace std;

typedef multiset<pair<int, int> > tt;

int t;

void reduce(int last, tt &a, tt &b){
  tt::iterator iter = a.lower_bound(make_pair(last, 0));
  if(iter != a.end()){
    last = iter->second + t;
    a.erase(iter);
    reduce(last, b, a);
  }
}

int main(void){
  int c;

  cin >> c;
  for(int k = 0; k < c; ++k){
    int na, nb, h, m;
    char ch;
    tt ab, ba;
    cin >> t >> na >> nb;

    for(int i = 0; i < na; ++i){
      cin >> h >> ch >> m; int from = 60*h + m;
      cin >> h >> ch >> m; int to = 60*h + m;
      ab.insert(make_pair(from, to));
    }

    for(int i = 0; i < nb; ++i){
      cin >> h >> ch >> m; int from = 60*h + m;
      cin >> h >> ch >> m; int to = 60*h + m;
      ba.insert(make_pair(from, to));
    }

    int a = 0, b = 0;
    while(!ab.empty() && !ba.empty())
      if(ab.begin()->first < ba.begin()->first)
        reduce(0, ab, ba), ++a;
      else
        reduce(0, ba, ab), ++b;

    a += ab.size();
    b += ba.size();

    cout << "Case #" << k+1 << ": " << a << ' ' << b << endl;
  }

  return 0;
}
