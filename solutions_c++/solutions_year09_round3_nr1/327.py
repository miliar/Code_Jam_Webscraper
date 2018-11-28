
#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int N;
string x;

long long solve(string x) {
//  cout << "arde!\n";

  map<char,int> mp;
  set<int> se;
    
  for ( int i = 0; i < x.size(); ++i ) {
    if ( !mp.count( x[i] ) ) {
      if ( !i ) {
        mp[ x[i] ] = 1;
        se.insert(1);
      } else {
        for ( int j = 0; ; ++j )
          if ( se.find(j) == se.end() )  {
            mp[ x[i] ] = j;
            se.insert(j);
            break;
          }
      }
    }
  }
  
  long long base = mp.size();
  long long res = 0;
  
  if ( base == 1 ) {
    return (1LL<<(x.size()))-1;
  }
  
//  cout << "base = " << base << endl;  
//  for ( map<char, int>::iterator it = mp.begin(); it != mp.end(); ++it )
//    cout << it->first << " : " << it->second << endl;
  
  for ( int i = 0; i < x.size(); ++i ) {
    res *= base;
    res += (long long)mp[ x[i] ];
  }
  
  return res;
}

int main() {
//  freopen("A.in", "r", stdin);
//  freopen("A.out", "w", stdout);

//  freopen("A-small-attempt2.in", "r", stdin);
//  freopen("A-small-attempt2.out", "w", stdout);

  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

  cin >> N;
  
  for ( int i = 1; i <= N; ++i ) {
    cout << "Case #" << i << ": ";
    cin >> x;
    cout << solve(x) << endl;
  }

  return 0;
}
