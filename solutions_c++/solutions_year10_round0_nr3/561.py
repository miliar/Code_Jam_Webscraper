#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751

long long T, R, S, N;

long long Sol(vector<long long> G) {
   int Next[N];
   long long Value[N];  
   for(int i = 0; i < N; i++) {
     long long v = 0;
     for(int j = i; j < i+N; j++) {
         if(v + G[j%N] > S) {
           Next[i] = j%N;
           Value[i] = v;
           v += G[j%N];
           break;
         }
         v += G[j%N];
     }
     if(v <= S) {Next[i] = i; Value[i] = v;}
   }

   long long V2[N];
   int NB[N];
   for(int i = 0; i < N; i++) V2[i] = -1;

   int pos = 0;
   int nb = 0;
   long long val = 0;

//   cerr << pos << " " << V2[pos] << " " << R << " " << Next[pos] << endl;

   for(; V2[pos] == -1 && nb < R; pos = Next[pos]) {
 //    cerr << "# " << pos << " " << nb << " " << val << endl;
     V2[pos] = val;
     NB[pos] = nb;
     val += Value[pos];
     nb++;
  //   cerr << "# " << pos << " " << nb << " " << val << endl;
   }

   if(nb == R) return val;

   long long cycle = nb - NB[pos];
   long long cycle_val = val - V2[pos];

   long long nb_cycle = (R - nb)/cycle;
   nb += cycle * nb_cycle;
   val += cycle_val * nb_cycle;

   for(; nb < R; pos = Next[pos]) {
     val += Value[pos];
     nb++;
//     cerr << pos << " " << nb << " " << val << endl;
   }

   return val;
}


int main() {
  cout.precision(16);
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> R >> S >> N;
    vector<long long> G(N);
    for(int j = 0; j < N; j++) cin >> G[j];
    cout << "Case #" << i << ": " << Sol(G) << endl;
  }
}
