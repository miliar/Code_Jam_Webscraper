#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(void)
{
  int n;
  cin >> n;
  for( int cas = 0 ; cas < n ;  ) {
    cout << "Case #" << (++cas) << ": ";
    vector<string> engines;
    vector<string>::iterator p;
    string str;
    int i, m, nEng;

    // Engines
    for( cin >> m, getline(cin, str) ; m > 0 ; --m ) {
      getline(cin, str);
      engines.push_back(str);
    }
    nEng = engines.size();
    
    int sw = 0, nOn = nEng;
    vector<bool> flags(engines.size());
    fill(flags.begin(), flags.end(), true);
    // Queries
    for( cin >> m, getline(cin, str) ; m > 0 ; --m ) {
      getline(cin, str);
      p = find(engines.begin(), engines.end(), str);
      if( p == engines.end() ) continue;
      // Found
      for( i = 0 ; i < nEng ; ++i ) {
        if( flags[i] && engines[i] == str ) {
          flags[i] = false;
          --nOn;
          break;
        }
      }
      // at query that all engine cannot use
      if( nOn == 0 ) {
        ++sw;
        fill(flags.begin(), flags.end(), true);
        flags[i] = false;
        nOn = nEng - 1;
      }
    }

    // Output
    cout << sw << "\n";
  }
  return 0;
}
