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
#define FORE(a, b, c) for(int c=a; c<=(int) b; ++c)
#define FORD(a, b, c) for(int c=a; c>=(int) b; --c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0) 
#define prd dbg printf
#define koniec dbg {SCC(c);SCC(c);} return 0;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef unsigned long long ll;
typedef long double ld;
typedef unsigned int uint;

const int sto = 103;

char c, str[sto];
int n, tn, s, pot[sto];
si ask;

ll getnum(int b) {
  int k = 1;
  string str2(str);
  
  FORIT(si, ask, sit) {
    if((b & k) == k)
      str2[*sit] = '1';
    else
      str2[*sit] = '0';
    k *= 2;
  }
  
  ll out = 0, kl = 1;
  FORD(str2.size() - 1, 0, i) {
    out += kl * (str2[i] == '1');
    kl *= 2;
  }
  
  prd("getnum %d = %d\n", b, (int) out);
  return out;
}

void wypisz(int b) {
  int k = 1;
  string str2(str);
  
  FORIT(si, ask, sit) {
    if((b & k) == k)
      str2[*sit] = '1';
    else
      str2[*sit] = '0';
    k *= 2;
  }
  
  FORE(0, str2.size() - 1, i)
    printf("%c", str2[i]);
  printf("\n");
}
    
void compute(int ti) {
  scanf("%s", str);
  string str3(str);
  ask.clear();
  
  FORE(0, str3.size() - 1, i)
    if(str[i] == '?')
      ask.insert(i);
      
  printf("Case #%d: ", ti);
  fprintf(stderr, "Case #%d: ", ti);
  
  s = ask.size();
  FORE(0, pot[s] - 1, b) {
    ll num = getnum(b);
    ll start = 1, stop = num;
    while(start < stop) {
      ll mid = (start + stop) / 2;
      if (num / mid > mid)
        start = mid + 1;
      else
        stop = mid;
    }
    if(num / start == start && (num + start - 1) / start == start) {
      wypisz(b);
      break;
    }
  }    
}

int main() {
  pot[0] = 1;
  FORE(1, 20, i)
    pot[i] = 2 * pot[i - 1];
  
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

