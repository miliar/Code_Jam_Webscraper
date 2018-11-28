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
#include<iostream>

#define SC(a) scanf("%d", &a)
#define SCC(a) scanf("%c", &a)
#define SC2(a, b) scanf("%d%d", &a, &b)
#define SC3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define PR(a) printf("%d\n", a)
#define FORE(a, b, c) for(int c=int(a); c<= int(b); ++c)
#define FORD(a, b, c) for(int c=int(a); c>= int(b); --c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 
#define ALL(a) a.begin(), a.end()

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
typedef long long ll;
typedef long double ld;
typedef unsigned int uint;

const int sto = 103;

char c, t[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int tn;
string s, s2;

void compute(int ti) {
  getline(cin, s);
  s2 = s;
  FORE(0, s.size() - 1, i)
    if (s[i] == ' ')
      s2[i] = ' ';
    else
      s2[i] = t[s[i] - 'a'];
  cout << "Case #" << ti << ": " << s2 << endl;
}

int main() {
  SC(tn);
  getline(cin, s);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

