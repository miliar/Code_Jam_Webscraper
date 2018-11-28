#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

vector< vi > edges;
int N;
vector < int > in;


int main()
{
  int tests = GETINT;
  for(int t = 1; t <= tests; t++) {
    N = GETINT;
    edges.clear(); FOR(i, N) edges.pb(vi());
    in.clear(); FOR(i, N) in.pb(0);
    FOR(i, N) {
      int p = GETINT;
      FOR(j, p) {
	int q = GETINT;
	q--;
	edges[i].pb(q);
	in[q]++;
      };
    }
    vi top;
    FOR(i, N) {
      FOR(j, N) {
	if(in[j] == 0) {
	  FOR(k, edges[j].size()) in[edges[j][k]]--;
	  top.pb(j);
	  in[j] = -1;
	}
      }
    }
    assert(top.size() == N);
    ll paths[N][N];
    FOR(i, N) FOR(j, N) paths[i][j] = 0;
    FOR(v, N) {
      int i = top[N-1-v];
      FOR(j, edges[i].size()) {
	int l = edges[i][j];
	paths[i][l]++;
	FOR(k, N) paths[i][k] += paths[l][k];
      }
    }
    bool diamond = false;
    FOR(i, N) FOR(j, N) diamond = diamond || (paths[i][j] > 1);
    cout << "Case #" << t << ": " << (diamond ? "Yes" : "No") << endl;
  }
  return 0;
}
