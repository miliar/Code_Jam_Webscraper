// solution by Peter Ondruska

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstring>

#include <iostream>
#include <sstream>
#include <complex>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long ll;

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORTO(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)
#define FORDTO(i,a,b) for(int i=(a);i>=(b);i--)
#define FOREACH(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)

#define DEBUG(x) cout<<'>'<<#x<<':'<<x<<endl
#define SIZE(X) int(X.size())

int T, X, Y;

char board[77][77];

bool place(int x, int y) {
	if (x > X-2 || y > Y-2)
		return false;
	if (board[y][x] != '#') return false;
	board[y][x] = '/';
	if (board[y+1][x] != '#') return false;
	board[y+1][x] = '\\';
	if (board[y][x+1] != '#') return false;
	board[y][x+1] = '\\';
	if (board[y+1][x+1] != '#') return false;
	board[y+1][x+1] = '/';
	return true;
}

int main() {
	scanf("%d", &T);
    FORTO(t,1,T) {
    	scanf("%d %d\n", &Y, &X);
    	FOR(y,Y) scanf("%s", board[y]);
    	bool fail = false;
    	FOR(y,Y) FOR(x,X) {
    		if (board[y][x] == '#' && !place(x,y)) {
    			fail = true;
			}
    	}
    	printf("Case #%d:\n", t);
    	if (fail) {
    		printf("Impossible\n");
		} else {
			FOR(y,Y) printf("%s\n", board[y]);
		}
	}
	return 0;
}

