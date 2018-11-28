#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <cassert>
using namespace std;

#define x X
#define y Y
#define VV vector
#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND = 0;

#define DB(x) { if (COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }

#define SZ 7000

#define PII pair<int, int>

int dx[] = { -1, 0, 1, 0};
int dy[] = { 0, -1, 0, 1};

int main(int argc, char **argv) {
  COND = argc >= 2 && argv[1][0] == 'q';
  ios::sync_with_stdio(false);
  int T;
 cin >> T; 
  FOR (my, 1, T) {
    int L; 
    cin >> L;
    ll MA[SZ];
    ll MI[SZ];
    CLR(MA,0xf0);
    CLR(MI,0x10);
    ll MALE[SZ]; ll MARI[SZ]; 
    CLR(MALE,0xf0); CLR(MARI, 0xf0);
    ll MILE[SZ], MIRI[SZ];
    CLR(MILE, 0x10); CLR(MIRI, 0x10);

    PII cur(0, 0);;
    ll field = 0; int d = 0;
    REP (j, L) {
      string S; int k;
      cin >> S >> k;
      REP (i, k) {
        REP (g, (int)S.size()) { int it = S[g];
          if (it == 'L') d = (d - 1 + 4) % 4;
          else if (it == 'R') d= (d + 1) % 4;
          else {
            PII ncur = PII(cur.x + dx[d], cur.y + dy[d]);
            field += cur.x * ncur.y - cur.y * ncur.x;
            cur = ncur;
            DB(cur.x<< " "<<cur.y);
            MI[cur.x + SZ / 2] = min(MI[cur.x + SZ / 2], (ll)cur.y);
            MA[cur.x + SZ / 2] = max(MA[cur.x + SZ / 2], (ll)cur.y);
          }
        }
      }
    }
    field = abs(field);
    ll conv = 0;
    
    FOR (i, 1, SZ - 2) {
      MILE[i] = min(MI[i], MILE[i-1]);
      MALE[i] = max(MA[i], MALE[i-1]);
    }
     
    FORD (i, SZ - 1, 1) {
      MIRI[i] = min(MI[i], MIRI[i+1]);
      MARI[i] = max(MA[i], MARI[i+1]);
    }

    FOR (i, 1, SZ - 2) {
      MI[i] = max(MILE[i], MIRI[i]);
      MA[i] = min(MALE[i], MARI[i]);
    }

    FOR (i, 0, SZ - 2) {
      ll top = min(MA[i], MA[i+1]);
      ll bot = max(MI[i], MI[i+1]);
      if (top > bot) {
        int hei = top - bot;
         
         conv += max((ll)0, (ll)hei);
         DB(top - bot);    
      }
    } 
     DB(field<<" "<<conv); 
    printf("Case #%d: %lld\n", my, abs(conv  - field / 2));
  }


  return 0;
}
