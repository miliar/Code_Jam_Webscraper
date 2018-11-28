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


int compsize(int Perm[], int k, string S) {


  string S2 = S;
  REP(i, S.len) {

//    cout << (i / k)* << " " << i%k << " " << Perm[i % k] << " " << i << endl;
    S2[k*(i / k) + Perm[i % k]] = S[i];
  }

  int size = 1;
  for(int i = 1; i < S2.len; i++) if(S2[i] != S2[i-1]) size++;

 // cout << S << " " << S2 << " " << size<< " ";
 // REP(i, k) cout << Perm[i] << " ";
 // cout << endl;



  return size;
}

int compress(int k, string S) {

  int best = INF;
  int Perm[k];
  memset(Perm, -1, sizeof(Perm));
  int pos = 0;
  while(pos >= 0) {    
    if(pos == k) {

      int NB[k];
      memset(NB, 0, sizeof(NB));
      for(int j = 0; j < k; j++) NB[Perm[j]]++;
      bool ok = true;
      REP(j, k) ok = ok && NB[j] == 1;

      if(ok) {
        int nb = compsize(Perm, k, S);
        if(nb < best) best = nb;
      }
      pos--;
      continue;
    }
    if(Perm[pos] == k-1) {
      Perm[pos] = -1; 
      pos--;
      continue;
    }
    Perm[pos]++;
    pos++;
  }

  return best;




}

int main() {
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    int k;
    string S;
    cin >> k >> S;
    cout << "Case #" << i << ": " << compress(k, S) << endl;

  }
}
