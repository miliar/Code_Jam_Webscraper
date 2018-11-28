#include <iostream>
#include <list>
#include <string>
using namespace std;

void solve()
{
  int n;
  cin >> n;
  list<int> len;
  int length;

  // Data input
  for( int i = 0 ; i < n ; ++i ) {
    string str;
    cin >> str;
    int j;
    length = -1;
    for( j = n - 1 ; j >= 0 ; --j ) {
      if( str[j] == '1' ) {
        length = j;
        break;
      }
    }
    len.push_back(length);
  }

  int score = 0;
  for( int i = 0 ; i < n ; ++i ) {
    list<int>::iterator p;
    for( p = len.begin() ; p != len.end() ; ++p ) {
      if( *p <= i ) break;
      ++score;
    }
    len.erase(p);
  }
  cout << score << "\n";
}

int main(void)
{
  int T;
  cin >> T;
  for( int i = 1 ; i<= T ; ++i ) {
    cout << "Case #" << i << ": ";
    solve();
  }
}
