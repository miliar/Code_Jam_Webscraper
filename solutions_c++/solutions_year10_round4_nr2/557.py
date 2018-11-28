#include <iostream>
#include <vector>
#include <map>
using namespace std;

int solve(void)
{
  int P;
  cin >> P;
  int N = 1 << P;
  vector< map<int,int> > p0, p1;
  for( int i = 0 ; i < N ; ++i ) {
    int m; cin >> m;
    map<int,int> t;
    t.insert(pair<int,int>(m, 0));
    p0.push_back(t);
  }

  for( int i = 0 ; i < P ; ++i ) {
    int M = 1 << (P - i - 1);
    p1.clear();
    for( int j = 0 ; j < M ; ++j ) {
      int price;
      cin >> price;
      map<int,int>& t0 = p0[2*j];
      map<int,int>& t1 = p0[2*j+1];
      map<int,int> win;
      for( map<int,int>::iterator it0 = t0.begin() ; it0 != t0.end() ; ++it0 ) {
        for( map<int,int>::iterator it1 = t1.begin() ; it1 != t1.end() ; ++it1 ) {
          int mis = (it0->first < it1->first) ? (it0->first) : (it1->first);
          int prc = (it0->second) + (it1->second);

          if( win.find(mis) == win.end() ) {
            win.insert(pair<int,int>(mis, prc+price));
          } else {
            if( win[mis] > prc + price ) win[mis] = prc + price;
          }

          if( mis > 0 ) {
            if( win.find(mis-1) == win.end() ) {
              win.insert(pair<int,int>(mis-1, prc));
            } else {
              if( win[mis-1] > prc ) win[mis-1] = prc;
            }
          }
        }
      }
      p1.push_back(win);
    }
    p0 = p1;
  }

  int min = 0xfffffff;
  for( map<int,int>::iterator it = p0[0].begin() ; it != p0[0].end() ; ++it ) {
    if( min > it->second ) min = it->second;
  }
  
  return min;
}

int main(void)
{
  int T;
  cin >> T;
  for( int t = 1 ; t <= T ; ++t ) {
    cerr << "Case #" << t << "\n";
    cout << "Case #" << t << ": " << solve() << "\n";
  }
  return 0;
}
