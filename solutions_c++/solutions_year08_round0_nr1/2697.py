#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define REP(i, n) for(register typeof(n) i=0; i<(n); ++i)
typedef vector<int> V;
const int INF = 1<<30;

int main(){
  int N, S, Q;
  cin >> N;
  REP(n,N){
    string s;

    cin >> S; getline(cin,s);
    string servers[S];
    REP(i,S) {
      getline(cin,servers[i]);
    }

    cin >> Q; getline(cin,s);
    V d(S, 0);
    REP(i,Q){
      string query;
      getline(cin,query);
      V d2 = d;
      d.assign(S, INF);
      REP(j, S) REP(k, S){
        int cost = (query == servers[k]) ? INF : (j==k ? d2[j] : d2[j]+1);
        d[k] = cost < d[k] ? cost : d[k];
      }
    }

    int m=INF;
    REP(i,S) m = min(m,d[i]);
    cout << "Case #" << (n+1) << ": " << m << endl;
  }
}
