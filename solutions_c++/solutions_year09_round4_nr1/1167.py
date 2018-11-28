#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
using namespace std;

#define FOR(i, n) for (int i = 0; i < n; i++)

#define all(v) (v).begin(), (v).end()
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pi;
typedef long long ll;

vector<ll> V(61, 0);

int Solve(vector<ll> &A)
{
  int step = 0;
  const int N = A.size();
  while (true) {
    int req = -1;
    FOR(i, N) {
      if (A[i] > V[i]) {
        req = i; break;
      }
    }
    if (req >= 0) {
      int nextIndex = req+1;
      while (A[nextIndex] > V[req])
        ++nextIndex;
      for (int i = nextIndex; i > req; i--) {
        ll t = A[i]; A[i] = A[i-1];
        A[i-1] = t; ++step;
      }
    } else {
      break;
    }
  }

  return step;
}

int main(int argc, char **argv)
{
  if (argc < 2) {
    cerr << "Usage: " << argv[0] << " <input file>\n"; return 1;
  }
  ifstream fin(argv[1]);
  if (!fin) {
    cerr << "Could not open file " << argv[1] << endl; return 1;
  }

  const ll t = 1;
  for (ll i = 0; i < V.size(); i++) {
    V[i] |= (t << i);
  }
  
  int T;
  fin >> T;
  FOR(i, T) {
    int N;
    fin >> N >> ws;
    vector<ll>  A(N, 0);
    ll val;
    char buf[100];
    memset(buf, 0, 100);
    FOR(j, N) {
      val = 0;
      fin.getline(buf, 100);
      for (int k = N-1; k >= 0; k--) {
        if (buf[k] == '1') {
          val |= (t<<k); break;
        }
      }
      A[j] = val;
    }
    cout << "Case #" << i+1 << ": ";
    cout << Solve(A) << endl;
  }
  return 0;
}
