#include <string>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

#define INF 100000000

int main()
{
  int N, T = 1;
  cin >> N;
  while( N > 0 ) {
    
    int S, Q;
    vector <string> engines;
    map <string, int> m;
    vector <int> prvs;
    vector <int> cur;
    int ans = INF;

    cin >> S; cin.ignore();
    engines.resize(S);
    prvs.resize(S);
    cur.resize(S);
    for(int i = 0 ; i < S ; ++i ) getline(cin, engines[i]);
    for(int i = 0 ; i < S ; ++i ) m[engines[i]] = i;
    
    cin >> Q; cin.ignore();
    for(int i = 0 ; i < Q ; ++i ) {
      string s;
      getline(cin, s);
      int ind = m[s];
      for(int j = 0 ; j < S ; ++j ) {
	cur[j] = INF;
	if(j == ind) continue;
	for(int k = 0 ; k < S ; ++k )
	  {
	    if(j == k) cur[j] = min(cur[j], prvs[k]);
	    else cur[j] = min(cur[j], prvs[k] + 1);
	  }
      }
      prvs = cur;
    }

    for(int i = 0 ; i < S ; ++i ) ans = min( ans, prvs[i] );
    
    cout <<"Case #"<< T <<": " << ans << endl;
    
    --N; ++T;
  }
  
  return 0;
}
