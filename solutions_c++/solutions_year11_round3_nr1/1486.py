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

char t[55][55];

void inline jeden() {
	int a, b;
	scanf("%d%d", &a, &b);
	REP (i, a) {
	  scanf("%s", t[i]);
	}
	REP (i, a - 1) {
	  REP (j, b - 1) {
	    bool mal = true;
	    REP (di, 2) {
	      REP (dj, 2) {
	        if (t[i + di][j + dj] != '#') {
	          mal = false;
	          break;
	        }
	        if (!mal) {
	          break;
	        }
	      }
	    }
	    if (mal) {
	      t[i][j] = '/';
	      t[i][j + 1] = '\\';
	      t[i + 1][j] = '\\';
	      t[i + 1][j + 1] = '/';
	    }
	  }
	}
	bool ok = true;
	REP (i, a) {
	  REP (j, b) {
	    if (t[i][j] == '#') {
	      ok = false;
	      break;
	    }
	  }
	}
	if (ok) {
	  REP (i, a) {
	    REP (j, b) {
	      putchar(t[i][j]);
	    }
	    puts("");
	  }
	} else {
	  puts("Impossible");
	}
}

int main() {
	int z;scanf("%d",&z);
	FOR (i, 1, z) {
	  printf("Case #%d:\n", i);
	  jeden();
	}
}
