#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int main(void)
{
  int tc, cnt = 0;
  cin >> tc;
  while( tc-- ){
    int time = 0;
    int n;
    cin >> n;
    queue<int> O, B;
    pair<char, int> p[n];
    for(int i=0; i<n; ++i){
      char c;
      int no;
      cin >> c >> no;
      if(c == 'O')O.push(no);
      if(c == 'B')B.push(no);
      p[i] = make_pair( c, no );
    }
    
    int o = 1, b = 1;
    int idx = 0;
    while( O.size() + B.size() ){
      bool flg = false;
      if( O.size() ){
        if( o == O.front() && p[idx].first == 'O' ){
          flg = true;
          O.pop();
        }
        else if( o < O.front() )++o;
        else if( o > O.front() )--o;
      }
      if( B.size() ){
        if( b == B.front() && p[idx].first == 'B' ){
          flg = true;
          B.pop();
        }
        else if( b < B.front() )++b;
        else if( b > B.front() )--b;
      }
      if( flg )++idx;
      ++time;
    }

    cout << "Case #" << ++cnt << ": " << time << endl;
  }
  return 0;
}
