#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;

void test()
{
  string org, next;
  cin >> org;
  next = org;
  if( !next_permutation(next.begin(), next.end()) ) {
    next = next.substr(0, 1) + "0" + next.substr(1);
  }
  if( next[0] == '0' ) {
    int i;
    for( i = 0 ; i < next.size() ; ++i ) {
      if( next[i] != '0' ) break;
    }
    cout << next[i];
    for( int j = 0 ; j < next.size() ; ++j ) {
      if( j == i ) continue;
      cout << next[j];
    }
    cout << "\n";
  } else {
    cout << next << "\n";
  }
}

int main(void)
{
  string str;
  int T;
  cin >> T;
  getline(cin, str); // trim
  for( int ca = 1 ; ca <= T ; ++ca ) {
    cout << "Case #" << ca << ": ";
    test();
  }
  return 0;
}
