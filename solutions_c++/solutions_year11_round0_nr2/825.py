#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>

#define SC(a) scanf("%d", &a)
#define SCC(a) scanf("%c", &a)
#define SC2(a, b) scanf("%d%d", &a, &b)
#define SC3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define PR(a) printf("%d\n", a)
#define FORE(a, b, c) for(int c=a; c<=b; ++c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(1) 
#define prd dbg printf

const int sto = 103;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef vector<char> vch;
typedef long long ll;
typedef long double ld;

char c[4], ch, comb[256][256];
int n, t, op[256][256], num[256];

vch compute() {
  FORE(0, 255, j)
    FORE(0, 255, h)
      comb[j][h] = op[j][h] = 0;
      
  FORE(0, 255, j)
    num[j] = 0;
      
  SC(n);
  FORE(1, n, j) {
    FORE(0, 3, h)
      SCC(c[h]);
      
    comb[c[1]][c[2]] = comb[c[2]][c[1]] = c[3];
  }
  
  SC(n);
  FORE(1, n, j) {
    FORE(0, 2, h)
      SCC(c[h]);
      
    op[c[1]][c[2]] = op[c[2]][c[1]] = 1;
  }
  
  SC(n);
  SCC(ch);
  vch out;
  
  FORE(1, n, j) {
    SCC(ch);
    int shit = 0;
    
    if(!out.empty() && comb[ch][out.back()]) {
      --num[out.back()];
      *out.rbegin() = comb[ch][out.back()];
      shit = 1;
    }
      
    else FORE(0, 255, h) {
      if (num[h] && op[h][ch]) {
        out.clear();
        shit = 1;
        FORE(0, 255, h)
          num[h] = 0;
        break;
      }
    }
      
    if(!shit) {
      ++num[ch];
      out.pb(ch);
    }
  }
  
  return out;
}  

int main() {
  SC(t);
  FORE(1, t, i) {
      vch vec = compute();
      printf("Case #%d: [", i);
      if (!vec.empty()) for(int j = 0; j <= vec.size() - 1; ++j) {
        //prd("(%d %d)", j, vec.size() - 1);
        printf("%c", vec[j]);
        if (j != vec.size() -1)
          printf(", ");
        }
      printf("]\n");
  }
  return 0;
}

