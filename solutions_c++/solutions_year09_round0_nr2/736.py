#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define Int signed long long int  /* 64b Unix : %lld , %llu  */
// #define Int __int64            /* 64b win  : %I64d, %I64u */

// #define DEBUG
#define DB(x) { cout << __LINE__ << ": " << #x << " " << x << endl; }
#define HERE { cout << "HERE\n"; }

#define INF 1000000000

#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define RET return
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) __typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) BEG(c), END(c)
#define POS(c,x) ((c).find(x) != END(c))
#define CLEAR(a, v, b) memset(a, v, b)
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SIZE(c) ((int) (c).size())
#define SSORT(c) stable_sort(ALL(c))
#define REP(i,e) for(int i = 0; i < (e); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";

template <class T> T* make1DArray (int C, T val) {
  T *A = new T [C]; CLEAR(A,val,sizeof(T)*C); return A;
}

template <class T> T** make2DArray (int R, int C, T val) {
  T **A; A = new T *[R]; FORU(r,0,R-1) {
    *(A+r) = make1DArray(C,val); } return A;
}

char basin;
 int **M; // input map
char **C; // basin map

char dfs (int r, int c) {
	if (C[r][c] != '*') return C[r][c];

	int dN = M[r-1][c];
	int dW = M[r][c-1];
	int dE = M[r][c+1];
	int dS = M[r+1][c];
	int dir = min (min(dN,dW), min(dE,dS));

	if (dir < M[r][c]) {
	  if (dir == dN) {
	    if (C[r-1][c] != '*') { return C[r-1][c]; }
	  	else { return dfs (r-1, c); }
	  } else {
	    if (dir == dW) {
	  	  if (C[r][c-1] != '*') { return C[r][c-1]; }
	  		else { return dfs (r, c-1); }
	  	} else {
	  	  if (dir == dE) {
	  	    if (C[r][c+1] != '*') { return C[r][c+1]; }
	  			else { return dfs (r, c+1); }
	  		} else {
	  		  if (C[r+1][c] != '*') { return C[r+1][c]; }
	  			else { return dfs (r+1, c); }
	  		}
	  	}
	  }
	}

	C[r][c] = basin++;
	return C[r][c];
}

int main() {

  int T;
  int H,W;

  scanf("%d\n",&T);
  FORU(testcase,1,T) {
  	scanf("%d %d\n",&H,&W);
  	M = make2DArray(1+H+1,1+W+1,0);
  	C = make2DArray(1+H+1,1+W+1,'*');

  	FORU(c,0,W+1) M[0][c] = 10000;
  	FORU(c,0,W+1) M[H+1][c] = 10000;
  	FORU(r,1,H) M[r][0] = 10000;
  	FORU(r,1,H) M[r][W+1] = 10000;

  	FORU(r,1,H) {
  		FORU(c,1,W) {
  			scanf("%d",&M[r][c]);
  		}
  	}

  	basin = 'a';

  	FORU(r,1,H) {
  		FORU(c,1,W) {
  			if (C[r][c] == '*') C[r][c] = dfs(r,c);
  		}
  	}

  	printf("Case #%d:\n",testcase);
  	FORU(r,1,H) {
			FORU(c,1,W) {
				printf("%c ",C[r][c]);
			} printf("\n");
		}
  }

  return 0;
}
