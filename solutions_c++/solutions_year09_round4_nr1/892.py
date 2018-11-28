#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <sstream>
using namespace std;

#define mp make_pair
#define pb push_back

const int inf = 1000 * 1000 * 1000;

typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vll;
typedef set<int> si;

template<typename T>
void readvector(int N, vector<T> &v, istringstream& iss = cin) {
  v.clear();
  v.resize(N);
  for (int i = 0 ; i < N ; i++)
    iss >> v[i];
}
const int maxN = 8;

int main() {
  int T; cin>>T; cin.ignore();
  for (int test = 1 ; test <= T ; test++) {
    int N; cin>>N; cin.ignore();
    vector<string> A;
    for (int i = 0 ; i < N ; i++) {
      string s;
      getline(cin,s);
      A.pb(s);
    }
    int p[maxN];
    for (int i = 0 ; i < N ; i++)
      p[i] = i;
    int best = inf;
    do {
      //      cout << "perm" << endl;
      //      for (int i = 0 ; i < N ; i++) { cout << p[i] << " ";}
      //      cout << endl;

      int cur = 0;
      bool ok = true;
      for (int i = 0 ; i < N; i++) {
	int maxL = N-1;
	while (maxL >= 0 && A[i][maxL] == '0') maxL--;
	//	cout << "maxJ for " << i << " : " << maxJ << endl;
	if (maxL > p[i]) {
	  //	  cout << "not ok "<< endl;
	  ok = false;
	}
	for (int j = i+1 ; j < N ; j++) {
	  cur += p[j] < p[i];
	}
      }
      if (!ok) continue;
      best = min(best, cur);
    } while(next_permutation(p, p+N));
    
    cout << "Case #" << test << ": " << best << endl;
  }
}
