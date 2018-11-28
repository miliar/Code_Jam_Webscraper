#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-11
#define INF 1000000000000ll

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

struct item{
  string feature;
  double p;
  int l,r;
};

item tree[1000];
int n,D,L,TT,A;
string inp,name;
set<string> S;

//prve miesto na zatvorku
string parsefrom(int w, string k){
  int depth=0;
  string vratim="";
  int ww=w;
  while (k[ww] != '(') ww++;
  while (true){
    vratim += k[ww];
    if (k[ww] == '(') depth++;
    if (k[ww] == ')') depth--;
    if (depth == 0)break;
    ww++;
  }
  return vratim;
}

void parse(string s,int n){
  string rr="";
  int w1=0; int w2 = s.size()-1;
  while(s[w1] != '('){ w1++; if (w1 >= s.size()) return; }
  while(s[w2] != ')'){ w2--; if (w2 < 0) return; }
  int w = w1; while (w <= w2){rr+=s[w]; w++;}

  string f="";

  //
  //cout << "...'" << rr << "'..." << endl;
  //

  w = 1;
  while (rr[w] != '0' && rr[w]!='1') w++;
  string pp="";
  while ( (rr[w] >= '0' && rr[w] <= '9') || (rr[w]=='.')){ pp+=rr[w]; w++;  }
  istringstream is(pp);
  is >> tree[n].p;
  while (rr[w] == ' ') w++;
  while ( rr[w] >= 'a' && rr[w] <= 'z'){ f+=rr[w]; w++; }
  tree[n].feature = f;
 
  
  tree[n].l = 0;
  tree[n].r = 0;
  
  while (rr[w] != '('){w++; if (w > rr.length()) return; }
  string left = parsefrom(w, rr);
  tree[n].l = 1;
  w+=left.length()+1; 
  parse(left, 2*n);
  string right = parsefrom(w,rr);
  parse(right, 2*n+1);
  tree[n].r = 1;
  return; 
}

double getp(int n, double p){
  double vratim = p * tree[n].p;
  bool jef = true;
  if (S.find(tree[n].feature) == S.end()) jef = false;
  if ((tree[n].l == 1) && (jef)) vratim=getp(n*2,vratim);
  if ((tree[n].r == 1) && (!jef)) vratim=getp(n*2+1,vratim);

  //cout << "prehladavam node " << n << " a vraciam " << vratim << endl;

  return vratim;
}

int main(){
  cin >> TT;
  FOR(tt,TT){
//    cin >> L;
    scanf("%d ",&L);
    inp = "";
    FOR(i,L){
      char c;
      scanf("%c",&c);
      while (c != '\n'){
        inp+=c;
        scanf("%c",&c);
      }
      inp+=' ';
    }

    //
    //cout << inp << endl;
    //

    parse(inp,1);

    /*
    FOR(i,3){
      cout << "node " << i+1 << endl;
      cout << "f : " << tree[i+1].feature << endl;
      cout << "p: " << tree[i+1].p << endl;
      cout << "l: " << tree[i+1].l << " , r = " << tree[i+1].r << endl;
    }
    */

    cin >> A;
    cout << "Case #" << tt+1 << ":" << endl;
    FOR(i,A){
      S.clear();
      cin >> name;
      cin >> n;
      FOR(j,n){
        string temp;
        cin >> temp;
        S.insert(temp);
      }
      double pp = getp( 1, 1.0 );
      printf("%.10f\n",pp);
    }
  }
}



