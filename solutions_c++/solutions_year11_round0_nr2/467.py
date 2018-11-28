// By mirosuaf and rogrog v.3.1
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=200;
int c,d,n;
vector<pair<pair<char, char>, char > > form;
vector<pair<char,char> > oppose;

vector<char> zrob(){
  form.clear();
  oppose.clear();
  cin >> c;
  REP(i,c){
    string tmp;
    cin >> tmp;
    form.PB(MP(MP(tmp[0]-'A', tmp[1]-'A'), tmp[2]-'A'));
    form.PB(MP(MP(tmp[1]-'A', tmp[0]-'A'), tmp[2]-'A'));
  }
  cin >> d;
  REP(i,d){
    string tmp;
    cin >> tmp;
    oppose.PB(MP(tmp[0]-'A', tmp[1]-'A'));
  }
  cin >> n;
  string invoke;
  cin >> invoke;
  vector<char> stack;
  REP(i,n){
    char curr = invoke[i]-'A';
    bool ok = false;
    if(SIZE(stack)>0){
      REP(j,SIZE(form)){
        if(form[j].ST.ST == curr && stack[SIZE(stack)-1]==form[j].ST.ND){
          stack[SIZE(stack)-1] = form[j].ND;
          ok=true;
          break;
        }
      }
    }
    if(!ok) stack.PB(curr);
    curr=stack[SIZE(stack)-1];
    REP(j,SIZE(stack)-1){
      REP(k,SIZE(oppose)){
        if( (oppose[k].ST == curr && oppose[k].ND == stack[j]) ||
            (oppose[k].ND == curr && oppose[k].ST == stack[j])){
         stack.clear();
         break;
        }
      }
    }
  }
  return stack;
}

int main() {
	int T; scanf("%d", &T); FOR(i,1,T) {
	  vector<char> res = zrob();
	  printf("Case #%d: [", i);
	  REP(i,SIZE(res)){
	    if(i!=0) printf(", ");
	    printf("%c", res[i]+'A');
	  }
	  printf("]\n");
	}
	return 0;
}

