#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<cstring>
#include<iostream>
#include<sstream>
using namespace std;
 
#define PB push_back
#define FORE(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();++i)
#define SZ(x) int((x).size())
#define REP(i,n) for(int i=0,_=(n);i<_;++i)
#define FOR(i,a,b) for(int i=(a),_=(b);i<=_;++i)
#define FORD(i,a,b) for(int i=(a),_=(b);i>=_;--i)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int INF=1e9+9;

void inline jeden() {
	int n;
	scanf("%d", &n);
	int czas[2] = {};
	int gdzie[2] = {1, 1};
	int wynik=0;
	char skto[2];
	int dokad;
	REP (i, n) {
	  scanf("%s%d", skto, &dokad);
	  int kto = -1;
	  if (skto[0] == 'B') {
	    kto = 0;
	  } else {
	    kto = 1;
	  }
	  int najw = max(czas[1 - kto] + 1, czas[kto] + abs(gdzie[kto] - dokad) + 1);
	  wynik = najw;
	  gdzie[kto] = dokad;
	  czas[kto] = najw;
	}
	printf("%d\n", wynik);
}

int main() {
	int z;scanf("%d",&z);FOR(i, 1, z) {
	  printf("Case #%d: ", i);
	jeden();
	}
}
